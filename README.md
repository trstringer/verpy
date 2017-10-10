# Verpy

Python CLI versioning tool

![Demo](demo.gif)

## Setup

This is a Docker-native application (i.e. I developed this with the conscious effort to run it as a container). With that being said, to run it in Docker you'll of course have to have Docker installed and running.

To create the necessary components, simply from `$ . install.sh` from the root of the repo.

## Usage

- Initialize the version file (`version.py`): `$ verpy init`
- Display the current version: `$ verpy version`
- Increment the *major* component of the version: `$ verpy version major`
- Increment the *minor* component of the version: `$ verpy version minor`
- Increment the *patch* component of the version: `$ verpy version patch`

- Display help: `$ verpy --help` or `$ verpy`
- Display the Verpy version: `$ verpy --version`


## Updates

This happens automatically. If you run `$ type verpy` you'll see that the shell function does a `docker pull`.
