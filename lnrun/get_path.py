from lnrun.config import get_script_path


def main(_: bool = False) -> None:
    path = get_script_path()
    if path is None:
        print('path not setted')
    else:
        print(path)


if __name__ == '__main__':
    main()
