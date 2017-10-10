#!/bin/bash

setup() {
    VERPY_DEF="
verpy() {
    docker pull trstringer/verpy:latest >> /dev/null
    docker run --rm \\
        -v \$(pwd):/usr/src/verpy/destination \\
        trstringer/verpy:latest \"\$@\"

    if [[ -f version.py ]]; then
        sudo chown \$USER:\$USER version.py
    fi
}"
    grep "source ~/.verpy" ~/.bashrc >> /dev/null
    if [ $? -ne 0 ]; then
        printf "adding .verpy sourcing to bashrc..."
        printf "\nsource ~/.verpy" >> ~/.bashrc
    else
        printf ".verpy sourcing already in bashrc..."
    fi

    printf "$VERPY_DEF" > ~/.verpy
    . ~/.bashrc
}

setup
