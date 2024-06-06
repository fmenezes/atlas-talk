from typing import List, Dict
import os
import uuid
from urllib.parse import urlparse
from urllib.parse import urljoin
from urllib.request import urlretrieve
import json
import requests
import signal
import sys

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
    r = requests.get(url)
    return r.url


def link_allowed(url: str) -> bool:
    return url.startswith(("https://www.mongodb.com/docs/",
        "http://www.mongodb.com/docs/",
        "https://mongodb.com/docs/",
        "http://mongodb.com/docs/",
        "https://docs.mongodb.com/",
        "http://docs.mongodb.com/")) and not url.endswith(('.tar', '.tar.gz', '.tgz', '.gz', '.7zip', '.zip', '.rar', '.json', '.csv'))


def extract_links(url: str, file_path: str) -> List[str]:
    with open(file_path) as f:
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


def process_docs(data: Dict, url: str) -> None:
    global stop

    to_visit = [url]
    already_visited = []
    while len(to_visit) > 0 and not stop:
        url = to_visit.pop()
        print(f'processing {url}')
        already_visited += [url]
        new_url = follow_redirects(url)
        if new_url != url:
            data['redirects'][url] = new_url
        url = new_url
        id = data['by_urls'].get(url) or str(uuid.uuid4())
        p = os.path.abspath(f"./data/html/{id}.html")
        failed = False
        if not os.path.exists(p):
            d = os.path.dirname(p)
            os.makedirs(d, exist_ok=True)
            data['by_urls'][url] = id
            data['by_ids'][id] = url
            try:
                urlretrieve(url, p)
            except:
                data['failed'] += [url]
                failed = True
            save_map(data)
        if failed:
            continue
        new_links = extract_links(url, p)
        new_links = [link for link in new_links if link_allowed(link)]
        new_links = [link for link in new_links if link not in already_visited]
        new_links = [link for link in new_links if link not in to_visit]
        to_visit += new_links


def cleanup(data: Dict) -> None:
    data['failed'] = []

    ids_to_remove = []
    urls_to_remove = []
    urls_to_promote = []
    for id in data['by_ids']:
        url = data['by_ids'][id]
        if url is None:
            ids_to_remove += [id]
    for url in data['by_urls']:
        id = data['by_urls'].get(url)
        if id is None:
            urls_to_remove += [url]
            continue
        new_url = data['redirects'].get(url)
        if new_url is not None:
            urls_to_remove += [url]
            urls_to_promote += [{
                'old_url': url,
                'new_url': new_url,
                'id': id,
            }]
            url = new_url
    for entry in urls_to_promote:
        old_url = entry['old_url']
        new_url = entry['new_url']
        id = entry['id']
        data['by_ids'][id] = new_url
        data['by_urls'][new_url] = id
        del data['by_urls'][old_url]
    for url in data['by_urls']:
        if not link_allowed(url):
            id = data['by_urls'][url]
            try:
                os.remove(f'./data/html/{id}.html')
            except:
                pass
            urls_to_remove += [url]
            ids_to_remove += [id]
    for id in ids_to_remove:
        try:
            del data['by_ids'][id]
        except:
            pass
    for url in urls_to_remove:
        try:
            del data['by_urls'][url]
        except:
            pass

    save_map(data)

    for name in os.listdir("./data/html/"):
        id = name.removesuffix('.html')
        if data['by_ids'].get(id) is None:
            p = f"./data/html/{name}"
            print(f"removing {p}")
            os.remove(p)


def path_map() -> str:
    return os.path.abspath("./data/map.json")


def load_map() -> Dict:
    data = {
        'by_ids': {},
        'by_urls': {},
        'failed': [],
        'redirects': {},
    }

    data_path = path_map()
    if os.path.exists(data_path):
        with open(data_path, "r") as f:
            data = json.load(f)
    return data


def save_map(data: Dict) -> None:
    data_path = path_map()
    with open(data_path, "w") as f:
        json.dump(data, f, indent=2)


def signal_handler(sig, frame):
    global stop
    print('exiting requested')
    stop = True


def main() -> None:
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    signal.signal(signal.SIGABRT, signal_handler)

    data = load_map()
    cleanup(data)
    process_docs(data, "https://www.mongodb.com/docs/")


main()
