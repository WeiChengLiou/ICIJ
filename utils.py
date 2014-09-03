#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pymongo import MongoClient
import logging
logging.basicConfig(level=logging.INFO,
                    filename='logtest.txt',
                    format='[%(levelname)s] %(asctime)s - %(message)s')
logger = logging.getLogger('logtest')


def init(fi=None):
    "initialize"
    client = MongoClient('localhost', 27017)
    cn = client.virgin
    return cn
cn = init()

