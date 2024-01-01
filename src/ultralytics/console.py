# Console scripts

import sys

from .__init__ import __version__  # all imports require a dot when building package: '.__init__', etc.
from .utils.general import colorstr

prefix = colorstr("ultralytics: ")


def get_api_key():
    # Get a user's API key
    print(f"{prefix}You can find your API key in your browser here: https://ultralytics.com/key")
    return input(f"{prefix}Paste an API key from your profile and hit enter: ")  # key


# def main_with_argparse():
#     parser = argparse.ArgumentParser()
#     parser.add_argument('--login', nargs='?', const=True, default=False, help='ultralytics login API_KEY')
#     parser.add_argument('--hello', action='store_true', help='debug command')
#     opt = parser.parse_args()
#
#     if opt.login:
#         key = opt.login if isinstance(opt.login, str) else get_api_key()  # specified or most recent path
#         print(f'{prefix}Logging in with API key {key}')
#
#         # Login user with API key
#         # TODO: login operations here
#
#     elif opt.hello:  # alternate command
#         print(f'{prefix}Hello user!')


def main():
    if len(sys.argv) == 1 or sys.argv[1] == "version":  # usage: $ ultralytics version
        print(f"{prefix}version {__version__}")
        print(f"{prefix}for more info see https://pypi.org/project/ultralytics/")

    elif sys.argv[1] == "login":  # usage: $ ultralytics login {optional_key}
        key = sys.argv[2] if len(sys.argv) == 3 else get_api_key()  # get_api_key() if not supplied
        print(f"{prefix}Logging in with API key {key}")

        # Login user with API key
        # TODO: login operations here

    else:
        print(f"{prefix}argument no recognized")
        exit()


if __name__ == "__main__":
    main()
