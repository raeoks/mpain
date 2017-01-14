from __future__ import print_function

import argparse

import config
import metadata


def main():
    prog_parser = argparse.ArgumentParser(prog=metadata.NAME, description=metadata.DESCRIPTION)
    prog_version = "%(prog)s Version: " + metadata.VERSION
    prog_parser.add_argument('-v', '--version', action='version', version=prog_version)
    prog_parser.add_argument('-c', '--config', action='store', nargs=1, help='%(prog)s config file')
    prog_args = prog_parser.parse_args()
    config.load(prog_args.config or "config.toml")
    print(config.CONFIG)


if __name__ == '__main__':
    main()
