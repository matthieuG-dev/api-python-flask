#! /usr/bin/python
import os

basedir = os.path.abspath(os.path.dirname(__file__))
print('sqlite:///' + basedir + '/testdb.db')