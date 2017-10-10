validate_version() {
    if [[ "$1" == "$2" ]]; then
        return 0
    else
        return 1
    fi
}

mkdir integration/test_dir

. venv/bin/activate

cd integration/test_dir

echo running init integration test
python ../../verpy.py init

if [[ ! -f version.py ]]; then
    echo version file expected but not existing
    exit 1
fi

echo displaying current version
python ../../verpy.py version

if [[ ! -f version.py ]]; then
    echo displaying current version failed
    exit 1
fi

echo running version major increment integration test
python ../../verpy.py version major

if [[ $? -ne 0 ]]; then
    echo failed incrementing version major
    exit 1
else
    VERSION_OUTPUT=$(python ../../verpy.py version)
    echo $VERSION_OUTPUT
    EXPECTED="2.0.0"
    validate_version "$VERSION_OUTPUT" "$EXPECTED"
    if [[ $? -ne 0 ]]; then
        echo expected $EXPECTED but got $VERSION_OUTPUT
        exit 1
    fi
fi

echo running version minor increment integration test
python ../../verpy.py version minor

if [[ $? -ne 0 ]]; then
    echo failed incrementing version minor
    exit 1
else
    VERSION_OUTPUT=$(python ../../verpy.py version)
    echo $VERSION_OUTPUT
    EXPECTED="2.1.0"
    validate_version "$VERSION_OUTPUT" "$EXPECTED"
    if [[ $? -ne 0 ]]; then
        echo expected $EXPECTED but got $VERSION_OUTPUT
        exit 1
    fi
fi

echo running version patch increment integration test
python ../../verpy.py version patch

if [[ $? -ne 0 ]]; then
    echo failed incrementing version patch
    exit 1
else
    VERSION_OUTPUT=$(python ../../verpy.py version)
    echo $VERSION_OUTPUT
    EXPECTED="2.1.1"
    validate_version "$VERSION_OUTPUT" "$EXPECTED"
    if [[ $? -ne 0 ]]; then
        echo expected $EXPECTED but got $VERSION_OUTPUT
        exit 1
    fi
fi

exit 0
