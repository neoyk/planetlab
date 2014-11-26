#! /usr/bin/python
import urllib2, math, os, sys, subprocess, shlex, re, time, socket, MySQLdb
pm =MySQLdb.connect(host='localhost',user='root',db='mnt')
cur =pm.cursor()

cur.execute("select bw from d80 where id='iperf' and time > '2013-03-02 0:0:0' order by time")
entry = cur.fetchone()
file = open('iperf.txt','w')
while entry:
	file.write(str(entry[0])+'\n')
	entry = cur.fetchone()
file.close()
cur.execute("select bw from d80 where id='ab-website1' and time > '2013-03-02 0:0:0' order by time")
entry = cur.fetchone()
file = open('iperf-web.txt','w')
while entry:
	file.write(str(entry[0])+'\n')
	entry = cur.fetchone()
file.close()
