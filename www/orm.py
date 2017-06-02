# orm.py
# coding:utf-8

__author__ = "dodonote"
import asyncio, logging
import aiomysql

def log(sql, args=()):
	logging.info('SQL: %s' % sql)