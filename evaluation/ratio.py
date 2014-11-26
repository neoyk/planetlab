#! /usr/bin/python
import urllib2, math, os, sys, subprocess, shlex, re, time, socket, MySQLdb
pm =MySQLdb.connect(host='localhost',user='root',db='mnt')
cur =pm.cursor()

cur.execute("select vantage_rtt/node_rtt,dns_rtt/node_rtt from web_dns_comp")
entry = cur.fetchone()
file = open('ratio.txt','w')
while entry:
	file.write(str(entry[0])+','+str(entry[1])+'\n')
	entry = cur.fetchone()
file.close()
