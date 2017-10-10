"""Test the main verpy code"""

from verpy import Version

def test_init():
    """Test version initialization"""

    version = Version()

    assert version.major == 1, 'major version should initialize correctly'
    assert version.minor == 0, 'minor version should initialize correctly'
    assert version.patch == 0, 'patch version should initialize correctly'

def test_parse_version():
    """Test version parsing"""

    version_initial = '1.2.3'
    version_final = Version.parse(version_initial)
    assert version_final.major == 1, 'major version parse matching'
    assert version_final.minor == 2, 'minor version parse matching'
    assert version_final.patch == 3, 'patch version parse matching'

def test_increment_version_major():
    """Test version major increment"""

    version_initial = '1.2.3'
    version_final = Version.parse(version_initial).increment_major()
    assert version_final.major == 2, 'major version should increment'
    assert version_final.minor == 0, 'minor version should be zero\'d out'
    assert version_final.patch == 0, 'patch version should be zero\'d out'

def test_increment_version_minor():
    """Test version minor increment"""

    version_initial = '1.2.3'
    version_final = Version.parse(version_initial).increment_minor()
    assert version_final.major == 1, 'major version should stay the same'
    assert version_final.minor == 3, 'minor version should increment'
    assert version_final.patch == 0, 'patch version should be zero\'d out'

def test_increment_version_patch():
    """Test version patch increment"""

    version_initial = '1.2.3'
    version_final = Version.parse(version_initial).increment_patch()
    assert version_final.major == 1, 'major version should stay the same'
    assert version_final.minor == 2, 'minor version should stay the same'
    assert version_final.patch == 4, 'patch version should increment'
