from typing import Iterator, Dict, List
import os
import json

SYSTEM_PROMPT = "You are MongoDB Atlas CLI Help Assistant, you know atlas cli command reference. You should assume atlas cli is properly installed. When you don't know the answer say you don't know it, do not try to make up an answer. Format your answers in Markdown."


def walk_files(path: str) -> Iterator[str]:
    for (dirpath, dirnames, filenames) in os.walk(path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            yield filepath


def print_prompt(prompt: str, response: str, system_prompt: str = SYSTEM_PROMPT) -> None:
    print(json.dumps({"messages": [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt},
        {"role": "assistant", "content": response}
    ]}))


def generate_description_prompt(content: Dict) -> None:
    description = content['Short']
    if content.get('Long') is not None:
        description += f"""
Synopsis:

{content['Long']}
"""
    print_prompt(f'What does the command `{content['CommandPath']}` do?', f"""This is the definition of the command `{content['CommandPath']}`:
    {description}""")


def generate_flags_prompt(content: Dict) -> None:
    if (content.get('InheritedFlags') is None or content.get('InheritedFlags').strip() == '') and (content.get('Flags') is None or content.get('Flags').strip() == ''):
        return

    flag_response = f"""Here are the flags for `{content['CommandPath']}`:
"""
    if content.get('Flags') is not None and content['Flags'] != '':
        flag_response += f"""
Flags:
{content['Flags']}"""

    if content.get('InheritedFlags') is not None and content['InheritedFlags'] != '':
        flag_response += f"""
Inherited Flags:
{content['InheritedFlags']}"""

    print_prompt(f'What are the flags for command `{content['CommandPath']}`?', flag_response)


def generate_example_prompt(content: Dict) -> None:
    if content.get('Example') is None or content.get('Example') == '':
        return None

    example = content['Example']

    for path_alias in content['CommandPathAliases']:
        if path_alias == content['CommandPath']:
            continue
        example = example.replace(
            path_alias, content['CommandPath'])

    example = example.split('\n')
    example = [line.strip() for line in example]
    example = [line.replace(
        '# ', '- ') if line.startswith('# ') else line for line in example]
    example = '\n'.join(example)

    print_prompt(f'Can you give me some examples for the command `{content['CommandPath']}`?', f"""Certainly.
{example}""")


def generate_aliases_prompt(content: Dict) -> None:
    if content.get('CommandPathAliases') is None:
        return
    print_prompt(f'Are there any aliases or shortcuts to command `{content['CommandPath']}`?', f"""Yes, here are some of the aliases:
{'\n'.join([f'- {alias}' for alias in content['CommandPathAliases']])}""")


def generate_prompts(content: Dict) -> None:
    if not content['Runnable']:
        return
    generate_description_prompt(content)
    generate_flags_prompt(content)
    generate_example_prompt(content)
    generate_aliases_prompt(content)


def main() -> None:
    print_prompt('How to get stared?', "To get started use `atlas setup`")
    
    print_prompt('How to create a local cluster?',
                 'You can use the command `atlas deployments setup` and you can also pass the flag `--type LOCAL` to create local deployments')

    print_prompt('How to create a local dev environment?',
                 'You can use the command `atlas deployments setup` and you can also pass the flag `--type LOCAL` to create local deployments')

    print_prompt('Where can I find atlas cli documentation and manuals?',
                 'You can use `atlas --help`, `atlas <command> --help` or navigate to https://www.mongodb.com/docs/atlas/cli/stable')

    for filepath in walk_files('./data/json/raw'):
        with open(filepath, 'r') as f:
            content = json.load(f)
            generate_prompts(content)

if __name__ == '__main__':
    main()
