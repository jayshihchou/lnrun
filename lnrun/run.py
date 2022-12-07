import os
import subprocess
import sys
import tempfile

from lnrun.config import get_config, get_config_value, is_token_setted
from lnrun.send_message import send_message
from lnrun.send_image import send_image


def main(_: bool = False):
    if not is_token_setted():
        print('script path is not setted, run "lnrun set_config script_path https://your.path.here" to set your path')
        exit()

    cmds = sys.argv[1:]
    if cmds[0] == 'run':
        cmds = cmds[1:]

    send_errors = get_config('send_errors')

    if send_errors:
        file = tempfile.NamedTemporaryFile()
        process = subprocess.run(cmds, stderr=file)
    else:
        process = subprocess.run(cmds)
    return_code = process.returncode
    # popen = subprocess.Popen(cmds, stderr=file)
    # return_code = popen.wait()

    message = f'lnrun done running : {cmds}'
    if send_errors:
        if return_code:
            file.seek(0)
            lines = file.readlines()
            try:
                lines = [line.decode(errors='replace') for line in lines]
                lines = ''.join(lines)
            except Exception:
                pass
            file.close()
            message += f'\nwith error:\n{lines}'
        else:
            message += ' without errors'
    else:
        message += ' with error' if return_code else ' without error'
    print(message)
    image_path = get_config_value('image_path')
    message_sent = False
    if image_path is not None:
        if os.path.exists(image_path):
            if send_image(image_path, message):
                message_sent = True
        else:
            print(f'try send image but is not existed: {image_path}')

    if not message_sent:
        send_message(message)


if __name__ == '__main__':
    main()
