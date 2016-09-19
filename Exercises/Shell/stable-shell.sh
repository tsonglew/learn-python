#!/usr/bin/env bash

# Some advice for writing stable shell script
# URL: https://segmentfault.com/a/1190000006900083

# print the commands been executed
set -x
# end the program when crash an error
set -e

# shellcheck helps
# Github: https://github.com/koalaman/shellcheck

# Deal with Parameter
# https://segmentfault.com/a/1190000002539169

# parameters are global in default
# define local parameter:
local hello="world"
# echo ${hello}; would cause an error

# invoke Function sighandler when received SIGINT
trap sighandler INT

echo "Hello world!";

# allow invoke functions when script ends
trap func EXIT

# allow invoke functions when errors come up
trap func ERR
