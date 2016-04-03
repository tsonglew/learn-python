#!/bin/sh

sudo pip install virtualenv
virtualenv ENV
cd ENV
source ./bin/activate
cd ..
sudo pip install -r requirements
