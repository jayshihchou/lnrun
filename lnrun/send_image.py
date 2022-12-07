import argparse
import mimetypes
import random
import string
from urllib.request import Request, urlopen

from lnrun.config import get_config, get_token


def parse_args(additional: bool = False) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    if additional:
        parser.add_argument('COMMAND', help='command to use')
    parser.add_argument('image_path', help='image path to send')
    return parser.parse_args()


def random_string(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length + 1))


def encode_multipart_data(data: dict, files: dict):
    boundary = random_string(30)

    def get_content_type(filename):
        return mimetypes.guess_type(filename)[0] or 'application/octet-stream'

    def encode_field(field_name):
        return [f'--{boundary}',
                f'Content-Disposition: form-data; name="{field_name}"',
                '', str(data[field_name])]

    def encode_file(field_name):
        filename = files[field_name]
        with open(filename, 'rb') as f:
            return [f'--{boundary}',
                    f'Content-Disposition: form-data; name="{field_name}"; filename="{filename}"',
                    f'Content-Type: {get_content_type(filename)}',
                    b'', f.read()]

    lines = []
    for name in data:
        lines.extend(encode_field(name))
    for name in files:
        lines.extend(encode_file(name))
    lines.extend((f'--{boundary}--', ''))

    lines = [x.encode('utf-8') if isinstance(x, str) else x for x in lines]
    body = b'\r\n'.join(lines)

    headers = {'content-type': f'multipart/form-data; boundary={boundary}',
               'content-length': str(len(body))}

    return body, headers


def send_image(image_file: str, message: str = None) -> bool:
    token = get_token()
    if token is None:
        print('line_token is not setted, run "lnrun set_config line_token your_token" to set your token')
        return False

    if message is None:
        message = 'Image File'
    data = {
        'message': message,
    }
    files = {
        'imageFile': image_file
    }
    body, headers = encode_multipart_data(data, files)
    headers['Authorization'] = 'Bearer ' + token

    req = Request(
        url='https://notify-api.line.me/api/notify',
        headers=headers,
        data=body,
    )
    try:
        content = urlopen(req)
    except Exception as e:
        print('Run urllib.request.urlopen with Exception:')
        print(e)
        return False
    if get_config('verbose'):
        print(content.read())
    return True


def main(additional: bool = False) -> None:
    args = parse_args(additional)
    send_image(args.image_path)


if __name__ == '__main__':
    main()
