#! /bin/env python
# -*- coding: utf-8 -*-
import os,sys,string,re,threading,subprocess,math,time,socket,logging,getopt,glob,shlex, MySQLdb

pm =MySQLdb.connect(host='localhost',user='root',db='mnt')
cur =pm.cursor()

for line in open('./current-nodes.txt'):
	try:
		ip = [socket.gethostbyname(line.strip())]
		print ip[0], line
		time.sleep(0.2)
		cur.execute("replace into planetlab_node values ('{0}', '{1}')".format(line.strip(), ip[0]) )
	except:
		print 'error', line
