import sys

from lnrun import __version__, get_path, run, send_message, set_path


def print_help():
    print(
        f'lnrun({__version__}): Line Notify after running shell commands.'
        '\nUsage: lnrun [COMMAND] [OPTIONS]'
        '\nor     lnrun [SYSTEM COMMAND]'
        '\n\nCommands:'
        '\n     run [SYSTEM COMMAND]     notify after run commands'
        '\n     send_message             send test message'
        '\n     get_path                 get GAS web path'
        '\n     set_path                 set GAS web path'
        '\n     -v, --version            show version'
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
        cmds['run'].main()
    else:
        cmds[sys.argv[1]].main(True)


if __name__ == '__main__':
    main()