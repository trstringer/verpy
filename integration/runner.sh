#!/bin/bash

cleanup() {
    rm -rf integration/test_dir
}

# run a basic integration test start to finish
./integration/basic.sh
EXIT_STATUS=$?

if [[ $EXIT_STATUS -ne 0 ]]; then
    echo failed running basic integration test
    cleanup
    exit $EXIT_STATUS
fi

cleanup
exit 0
