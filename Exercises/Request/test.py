#!/usr/bin/env python
#-*- coding: utf-8 -*-

import requests

# Get a webpage, eg: GitHub's public timeline
# The Response object `r`
r = requests.get('https://api.github.com/events')

# Make an HTTP POST request
r = requests.post('http://httpbin.org/test', data = {'key': 'value'})

# HTTP PUT
r = requests.put('http://httpbin.org/put', data = {'key': 'value'})

# HTTP DELETE
r = requests.delete('http://httpbin.org/delete')

# HTTP HEAD
# get only the head of a webpage
r = requests.head('http://httpbin.org/get')

# HTTP OPTIONS
# get the methods surppoted by the server
r = requests.options('http://httpbin.org/get')


# Passing Parameters In URLS
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('http://httpbin.org/get', params=payload)
