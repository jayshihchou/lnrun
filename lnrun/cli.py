import sys

from lnrun import get_path, run, set_path, send_message
from lnrun import __version__


def print_help():
    print(
        'Notify after run'
        '\nUsage: lnrun [COMMAND] [OPTIONS]'
        '\n\nCommands:'
        '\n     run                notify after run commands'
        '\n     send_message        send test message'
        '\n     get_path            get GAS web path'
        '\n     set_path            set GAS web path'
        '\n     -v, --version       show version'
        '\n adding command to see more help info'
    )


def main():
    cmds = {
        'run': run,
        'send_message': send_message,
        'get_path': get_path,
        'set_path': set_path,
    }
    if len(sys.argv) == 1:
        print('Need to provide method to use.')
        print_help()
        exit()
    if sys.argv[1] == '-h' or sys.argv[1] == '--help':
        print_help()
        exit()
    if sys.argv[1] == '-v' or sys.argv[1] == '--version':
        print('lnrun', __version__)
        exit()
    all_not_in_cmd = True
    cmd = None
    for i in range(1, len(sys.argv)):
        cmd = sys.argv[i]
        if cmd in cmds:
            all_not_in_cmd = False
            break
    if all_not_in_cmd:
        print('Cannot find method in ', sys.argv)
        print_help()
        exit()

    cmds[sys.argv[1]].main(True)


if __name__ == '__main__':
    main()
