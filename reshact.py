import os
import sys
import click
import platform

from detect_secrets import SecretsCollection
from detect_secrets.settings import default_settings

__version__ = '0.1.0'

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
    '-f',
    '--force',
    is_flag=True
)
@click.option(
    '-v',
    '--version',
    is_flag=True
)
def main(force, version):
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

            print(secret['type'])
            print(secret['filename'])
            print(secret['line_number'])
            print(line_data)
            print()
            input()

            lines_seen.append(line_data)


if __name__ == '__main__':
    main()
