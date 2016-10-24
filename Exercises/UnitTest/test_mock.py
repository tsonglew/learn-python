# -*- coding: utf-8 -*-

import unittest

import mock
import client


class TestClient(unittest.TestCase):
    def setUp(self):
        self.result = {'review': {'author': 'dongwm'}}

    def test_response(self):
        api_result = mock.Mock(return_value=self.result)
        client.api_request = api_result
        self.assertEqual(client.get_review_author(
            'http://api.dongwm.com/review/123'), 'dongwm')

    def test_patch_request(self):
        api_result = mock.Mock(return_value=self.result)
        with mock.patch('client.api_requst', api_result):
            self.assertEqual(client.get_review_author(
                'http://api.dongwm.com/review/123'), 'dongwm')
