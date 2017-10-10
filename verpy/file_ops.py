"""Version file operations"""

import os
import re
from verpy.version import Version

def version_filename():
    """Retrieve the path and filename for the destination version file"""

    return os.path.join(os.getcwd(), 'version.py')

def write_version_to_file(version_to_write):
    """Write version to file"""

    template_filename = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'version.template.py'
    )

    with open(template_filename, 'r') as template_file:
        template_content = ''.join(template_file.readlines())

    template_content = template_content.replace('VERSION_TO_WRITE', str(version_to_write))
    version_filename_cache = version_filename()

    with open(version_filename_cache, 'w') as destination_file:
        destination_file.writelines(template_content)

    return str(version_to_write)

def initialize_version_file():
    """Create the base version file"""

    # initialize with base version (the Version class defaults)
    return write_version_to_file(Version())

def parse_version_from_file():
    """Parse the version from the current file"""

    with open(version_filename(), 'r') as version_file:
        version_file_content = ''.join(version_file.readlines())

    return re.search(r'(\d+\.\d+\.\d+)', version_file_content).group(1)

def increment_version_major():
    """Increment the major version"""

    parsed_version = Version.parse(parse_version_from_file())
    new_version = parsed_version.increment_major()
    write_version_to_file(new_version)
    return str(new_version)

def increment_version_minor():
    """Increment the minor version"""

    parsed_version = Version.parse(parse_version_from_file())
    new_version = parsed_version.increment_minor()
    write_version_to_file(new_version)
    return str(new_version)

def increment_version_patch():
    """Increment the patch version"""

    parsed_version = Version.parse(parse_version_from_file())
    new_version = parsed_version.increment_patch()
    write_version_to_file(new_version)
    return str(new_version)

def get_current_version():
    """Get the current version stored in the file"""

    return Version.parse(parse_version_from_file())
