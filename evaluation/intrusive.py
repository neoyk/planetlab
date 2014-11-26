#! /usr/bin/python
import urllib2, math, os, sys, subprocess, shlex, re, time, socket, MySQLdb
pm =MySQLdb.connect(host='localhost',user='root',db='webserver')
cur =pm.cursor()

cur.execute("select distinct a.webip, b.pagesize, b.bw*10 as iperf from ipv4prefix2vantage as a, ipv4candidate as b where a.webip=b.ip and a.webdomain=b.webdomain")
entry = cur.fetchone()
file = open('intrusive.txt','w')
while entry:
	file.write(str(entry[1])+','+str(entry[2])+'\n')
	entry = cur.fetchone()
file.close()
