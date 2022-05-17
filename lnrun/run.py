import subprocess

import tempfile
import sys

from lnrun.send_message import send_message
from lnrun.config import is_script_path_setted


def main(_: bool = False):
    if not is_script_path_setted():
        print('script path is not setted, run "lnrun set_path https://your.path.here" to set your path')
        exit()

    cmds = sys.argv[1:]
    if cmds[0] == 'run':
        cmds = cmds[1:]

    file = tempfile.NamedTemporaryFile()
    popen = subprocess.Popen(cmds, stderr=file)
    return_code = popen.wait()
    if return_code:
        file.seek(0)
        lines = file.readlines()
        lines = [line.decode() for line in lines]
        lines = ''.join(lines)

    file.close()

    message = f'lnrun done running : {cmds}'
    if return_code:
        message += f'\nwith error:\n{lines}'
        print(lines)
    else:
        message += ' without errors'
        print('cmd run without errors')

    send_message(message)


if __name__ == '__main__':
    main()
