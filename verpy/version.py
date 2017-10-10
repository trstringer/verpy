"""Version class definition"""

import re

class Version:
    """This class stores version information and handles necessary parsing"""

    def __init__(self, major=1, minor=0, patch=0):
        """Initialize the object"""

        self.major = major
        self.minor = minor
        self.patch = patch

    @staticmethod
    def parse(version):
        """Parse the Version from a version string"""

        version_re_match = re.search(r'^(\d+)\.(\d+)\.(\d+)$', version)
        return Version(
            major=int(version_re_match.group(1)),
            minor=int(version_re_match.group(2)),
            patch=int(version_re_match.group(3))
        )

    def increment_major(self):
        """Increment the major part of the version"""

        return Version(
            major=self.major + 1,
            minor=0,
            patch=0
        )

    def increment_minor(self):
        """Increment the minor part of the version"""

        return Version(
            major=self.major,
            minor=self.minor + 1,
            patch=0
        )

    def increment_patch(self):
        """Increment the patch part of the version"""

        return Version(
            major=self.major,
            minor=self.minor,
            patch=self.patch + 1
        )

    def __str__(self):
        """Format the Version to a string"""

        return '{}.{}.{}'.format(
            self.major,
            self.minor,
            self.patch
        )
