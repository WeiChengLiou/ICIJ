#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from pymongo import MongoClient
import logging
logging.basicConfig(level=logging.INFO,
                    filename='logtest.txt',
                    format='[%(levelname)s] %(asctime)s - %(message)s')
logger = logging.getLogger('logtest')


def init(fi=None):
    "init"
    if fi is None:
        fi = ':memory:'
    client = MongoClient('localhost', 27017)
    cn = client.virgin
    return cn
cn = init()


def badmark():
    return u'暫缺', u'缺額', u'懸缺', u'死亡', u'補選', u'禁止',\
        u'解任', u'請辭', u'註銷', u'停權', u'禁止', u'法拍',\
        u'撤銷', u'當然任', u'不存在', u'臨時', u'辭職'


def bad_board(cn):
    condic = {'$or': [
        {'name': {'$regex': key}} for key in badmark()]}
    ret = list(cn.boards.find(condic, ['name']).distinct('name'))
    ret.extend([u'', u'缺'])
    return ret


def getname(id):
    ret = cn.cominfo.find_one({'id': id}, ['name'])
    if ret:
        return ret['name']
    else:
        return id


def getid(name):
    ret = cn.iddic.find_one({'name': name})
    if len(ret['id']) == 1:
        return ret['id'][0]
    else:
        print u'Warnning: duplicte id - {0}'.format(name)
        return ret['id'][0]


def badstatus(cn):
    status = set()
    status.update(cn.cominfo.find(
        {'status': {'$not': re.compile(u'核准')}}).distinct('status'))
    status.update(cn.cominfo.find(
        {'$or': [{'status': {'$regex': u'停業'}},
         {'status': {'$regex': u'解散'}}]}).distinct('status'))
    return status
