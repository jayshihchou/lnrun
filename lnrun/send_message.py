import argparse
import urllib.parse
from urllib.request import Request, urlopen

from lnrun.config import get_config, get_token


def parse_args(additional: bool = False) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    if additional:
        parser.add_argument('COMMAND', help='command to use')
    parser.add_argument('message', help='message to send')
    return parser.parse_args()


def send_message(message: str) -> None:
    token = get_token()
    if token is None:
        print('line_token is not setted, run "lnrun set_config line_token your_token" to set your token')
        exit()

    urldata = urllib.parse.urlencode({
        'message': message,
    }).encode()

    req = Request(
        url='https://notify-api.line.me/api/notify',
        headers={
            'Authorization': 'Bearer ' + token,
        },
        data=urldata,
    )

    try:
        content = urlopen(req)
    except Exception as e:
        print('Run urllib.request.urlopen with Exception:')
        print(e)
        exit()

    if get_config('verbose'):
        print(content.read())


def main(additional: bool = False) -> None:
    args = parse_args(additional)
    send_message(args.message)


if __name__ == '__main__':
    main()
