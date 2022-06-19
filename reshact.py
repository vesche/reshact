#!/usr/bin/env python

import os
import sys
import click
import platform

from detect_secrets import SecretsCollection
from detect_secrets.settings import default_settings

__version__ = '0.1.1'

sc = SecretsCollection()

HISTORY_FILES = [
    '.bash_history',
    '.local/share/fish/fish_history',
    '.python_history',
    '.zsh_history',
]

import json

@click.command()
@click.option(
    '-v',
    '--version',
    is_flag=True
)
def main(version):
    if version:
        print(f'v{__version__}, https://github.com/vesche/reshact')
        return

    plat = platform.system()
    user = os.getlogin()
    if plat == 'Linux':
        prefix = f'/home/{user}'
    elif plat == 'Darwin':
        prefix = f'/Users/{user}'
    else:
        print(f'Error! Sorry, reshact does not work on {plat}.')
        sys.exit(1)

    if os.geteuid() == 0:
        prefix = '/root'

    all_secrets = dict()
    for f in HISTORY_FILES:
        file_path = os.path.join(prefix, f)
        print(f'Processing {file_path} ...')
        if os.path.isfile(file_path):
            with default_settings():
                sc.scan_file(file_path)
                all_secrets = all_secrets | sc.json()

    for history_file_path, secrets in all_secrets.items():
        with open(history_file_path) as f:
            data = f.read().splitlines()

        lines_seen = list()
        for secret in secrets:
            line_data = data[secret['line_number']-1]
            # ignore fish false positives
            if '  when: ' in line_data:
                continue
            # ignore lines already seen
            if line_data in lines_seen:
                continue
            lines_seen.append(line_data)

        secrets_found = len(lines_seen)
        print(f'{secrets_found} secret(s) found in {history_file_path}')

        if secrets_found == 0:
            continue

        if input('reshact all (y/n)? ').lower().startswith('y'):
            if not history_file_path.endswith('fish_history'):
                for line in lines_seen:
                    data = list(filter(lambda x: x != line, data))
            else:
                for line in lines_seen:
                    data[:] = [i if i != line else '- cmd: [reshact]' for i in data]
            with open(history_file_path, 'w') as f:
                f.write('\n'.join(data) + '\n')


if __name__ == '__main__':
    main()
