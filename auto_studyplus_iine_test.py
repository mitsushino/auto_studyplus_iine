# -*- coding: utf-8 -*-

import unittest
from auto_studyplus_iine import get_config_info


class ConfigTest(unittest.TestCase):
    'test config file functions'

    def test_read_config(self):
        file_name = 'config.ini'
        self.assertEqual(get_config_info(file_name, 'URL', 'url'),
                         'https://studyplus.jp/users/59ba237e6c0711e4ae3222000a78049b/studylog')
        self.assertEqual(get_config_info(file_name, 'LOGIN', 'mail'),
                         'ddmailrk@yahoo.co.jp')


if __name__ == '__main__':
    unittest.main()
