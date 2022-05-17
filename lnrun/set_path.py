import argparse

from lnrun.config import save_script_path


def parse_args(additional: bool = False) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    if additional:
        parser.add_argument('COMMAND', help='command to use')
    parser.add_argument('script_path', help='your script path')
    return parser.parse_args()


def main(additional: bool = False) -> None:
    args = parse_args(additional)
    save_script_path(args.script_path)


if __name__ == '__main__':
    main()
