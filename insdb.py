#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import os
from pdb import set_trace
from utils import *
from work import *


def chkfile(fi):
    with open(fi, 'rb') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=';', quotechar='"')
        for i, row in enumerate(csvreader):
            print u', '.join([x.decode('utf8') for x in row])
            if i >= 10:
                break


def filespec(path, fis):
    fspec = open('filespec.txt', 'wb')
    for fi in fis:
        fspec.write('#%s\n' % fi)
        with open(os.path.join(path, fi), 'rb') as csvfi:
            rows = csv.reader(csvfi, delimiter=';', quotechar='"')
            for row in rows:
                fspec.write(u',\n'.join([unicode(x).decode('utf8') for x in row]))
                break
        fspec.write(u',\n\n')
    fspec.close()


def insdb(coll, fi):
    with open(fi) as csvfi:
        rows = csv.reader(csvfi, delimiter=';', quotechar='"')
        cols = None
        for row in rows:
            if cols is None:
                cols = [x for x in row]
            else:
                dic = {k: v.decode('utf8') for k, v in zip(cols, row)}
                coll.insert(dic)
                #print dic
                #break


def refreshDB():
    path = '../csv 2014 01 23'
    fis = ['countriesNW.csv',
           'edges_1DNW.csv',
           'node_countriesNW.csv',
           'nodesNW.csv']
    tbls = [cn.nations, cn.edges, cn.nodenations, cn.nodes]

    filespec(path, fis)

    for tbl, fi in zip(tbls, fis):
        fi1 = os.path.join(path, fi)
        print fi1
        chkfile(fi1)
        insdb(tbl, fi1)
        #print 'press enter...'
        #raw_input()


if __name__ == '__main__':
    refreshDB()

