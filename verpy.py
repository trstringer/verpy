"""Main verpy code module"""

import sys
from verpy import file_ops
from version import VERSION

def display_app_help():
    """Display app usage"""

    print('verpy Usage:')
    print()
    print('  verpy init                         initialize versioning for current directory')
    print('  verpy version                      display the current version')
    print('  verpy version {major,minor,patch}  increment version section')
    print()
    print(' Global params:')
    print('  --help     display application help')
    print('  --version  display application version')

def initialize_current_directory():
    """Initialize the versioning in the current directory"""

    print(file_ops.initialize_version_file())

def display_or_change_version(cli_args_version_info):
    """Display or change the current working directory version"""

    if cli_args_version_info['major']:
        print(file_ops.increment_version_major())
    elif cli_args_version_info['minor']:
        print(file_ops.increment_version_minor())
    elif cli_args_version_info['patch']:
        print(file_ops.increment_version_patch())
    else:
        print(file_ops.get_current_version())

def args():
    """Handle command line arguments"""

    root_cmd = '--help'
    try:
        root_cmd = sys.argv[1].lower()
    except IndexError:
        pass

    second_cmd = None
    try:
        second_cmd = sys.argv[2]
    except IndexError:
        pass

    cmd_matrix = dict(
        app_version=root_cmd == '--version',
        app_help=root_cmd == '--help',
        init=root_cmd == 'init',
        version=dict(
            major=second_cmd == 'major',
            minor=second_cmd == 'minor',
            patch=second_cmd == 'patch'
        ) if root_cmd == 'version' else False
    )

    return cmd_matrix

def main():
    """Main code execution"""

    cli_args = args()

    if cli_args['app_help']:
        display_app_help()
    elif cli_args['app_version']:
        print('verpy v{}'.format(VERSION))
    elif cli_args['version']:
        display_or_change_version(cli_args['version'])
    elif cli_args['init']:
        initialize_current_directory()

if __name__ == '__main__':
    main()
