from typing import List, Dict
import os
from urllib.parse import urlparse, urljoin
from urllib.request import urlretrieve, urlcleanup
import json
import requests
import signal

from bs4 import BeautifulSoup

stop = False


def normalize_link(base_url: str, link: str) -> str:
    parsed_url = urlparse(base_url)
    prefix = f"{parsed_url.scheme}://{parsed_url.netloc}"

    if link.startswith('/'):
        return f"{urljoin(prefix, link)}"
    elif link.startswith(('#', '?')):
        return f"{base_url}{link}"
    else:
        return link


def follow_redirects(url: str) -> str:
    try:
        r = requests.get(url)
        return r.url
    except:
        return url


def link_allowed(url: str) -> bool:
    return url.startswith(("https://www.mongodb.com/docs/",
                           "http://www.mongodb.com/docs/",
                           "https://mongodb.com/docs/",
                           "http://mongodb.com/docs/",
                           "https://docs.mongodb.com/",
                           "http://docs.mongodb.com/")) and not url.endswith(('.tar', '.tar.gz', '.tgz', '.gz', '.7zip', '.zip', '.rar', '.json', '.csv'))


def extract_links(url: str, file_path: str) -> List[str]:
    with open(file_path, "r") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
        raw_links = [
            a['href'] for a in soup.find_all('a', href=True)
        ]
        all_links = [
            normalize_link(url, link) for link in raw_links
        ]
        links_without_anchors = [
            link.split('#')[0] for link in all_links]
        links = list(set(links_without_anchors))
        return links


def local_path(url: str) -> str:
    parsed_url = urlparse(url)
    local = parsed_url.path.removeprefix('/')
    if local.endswith('/'):
        local += "index.html"
    local = os.path.join(f"./data", local)
    new_pattern = local
    i = 0
    while os.path.exists(new_pattern):
        new_pattern = f"{local.removesuffix('.html')}_{i}.html"
        i += 1
    return new_pattern


def metadata_path(p: str) -> str:
    return p.removesuffix('.html') + '_metadata.json'


def load_metadata(url: str) -> Dict:
    lp = local_path(url)
    mp = metadata_path(lp)
    if os.path.exists(mp):
        with open(mp, "r") as f:
            return json.load(f.read())
    return {
        'local_path': lp,
        'url': url,
    }


def save_metadata(data: Dict) -> None:
    mp = metadata_path(data['local_path'])
    d = os.path.dirname(mp)
    os.makedirs(d, exist_ok=True)
    with open(mp, "w") as f:
        return json.dump(data, f, indent=2)


def process_docs(url: str) -> None:
    global stop

    state = load_state()

    if len(state['to_visit']) == 0:
        state['to_visit'] += [url]
        save_state(state)
    while len(state['to_visit']) > 0:
        if stop:
            print('exiting')
            exit(0)
        url = state['to_visit'].pop()
        if url in state['already_visited']:
            save_state(state)
            continue
        print(f'processing {url} ({len(state['already_visited']) +
              1} of {len(state['already_visited']) + len(state['to_visit']) + 1})')
        state['already_visited'] += [url]
        new_url = follow_redirects(url)
        if new_url != url:
            if link_allowed(new_url):
                state['to_visit'] += [new_url]
            save_state(state)
            continue
        metadata = load_metadata(url)
        p = metadata['local_path']
        if os.path.exists(p) and url not in state['failed']:
            save_state(state)
            continue
        try:
            d = os.path.dirname(p)
            os.makedirs(d, exist_ok=True)

            urlretrieve(url, p)
            urlcleanup()

            new_links = extract_links(url, p)
            new_links = [link for link in new_links if link_allowed(link)]
            metadata['links'] = new_links
            new_links = [
                link for link in new_links if link not in state['already_visited']]
            new_links = [
                link for link in new_links if link not in state['to_visit']]
            state['to_visit'] += new_links

            save_metadata(metadata)
        except:
            state['failed'] += [url]
        save_state(state)


def path_state() -> str:
    return os.path.abspath("./data/state.json")


def load_state() -> Dict:
    state = {
        'to_visit': [],
        'already_visited': [],
        'failed': [],
    }

    state_path = path_state()
    if os.path.exists(state_path):
        with open(state_path, "r") as f:
            state = json.load(f)
    return state


def save_state(state: Dict) -> None:
    state_path = path_state()
    d = os.path.dirname(state_path)
    os.makedirs(d, exist_ok=True)

    with open(state_path, "w") as f:
        json.dump(state, f, indent=2)


def signal_handler(sig, frame):
    global stop
    print('exiting requested')
    stop = True


def main() -> None:
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    signal.signal(signal.SIGABRT, signal_handler)

    process_docs("https://www.mongodb.com/docs/")


main()
