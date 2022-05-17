import argparse
import subprocess

from lnrun.send_message import send_message


def parse_args(additional: bool = False) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    if additional:
        parser.add_argument('COMMAND', help='command to use')
    parser.add_argument('cmds', nargs='+', help='system command')
    return parser.parse_args()


def main(additional: bool = False):
    args = parse_args(additional)

    process_res = subprocess.run(args.cmds, capture_output=True)
    message = 'nrun done running : {}'.format(' '.join(args.cmds))
    print(process_res.stdout.decode())
    if len(process_res.stderr) > 0:
        message += f'\nwith error:\n{process_res.stderr.decode()}'
        print(process_res.stderr.decode())
    else:
        message += ' without errors'
        print('cmd run without errors')

    send_message(message)


if __name__ == '__main__':
    main()
