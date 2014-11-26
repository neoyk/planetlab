#! /usr/bin/python
import urllib2, math, os, sys, subprocess, shlex, re, time, socket, MySQLdb
pm =MySQLdb.connect(host='localhost',user='root',db='mnt')
cur =pm.cursor()

cur.execute("select rtt from proximity_rtt where vantage!='127.0.0.1'")
entry = cur.fetchone()
file = open('latency_web.txt','w')
while entry:
	file.write(str(entry[0])+'\n')
	entry = cur.fetchone()
file.close()
cur.execute("select rtt from proximity_dns where dns_ip!='127.0.0.1' ")
entry = cur.fetchone()
file = open('latency_dns.txt','w')
while entry:
	file.write(str(entry[0])+'\n')
	entry = cur.fetchone()
file.close()
cur.execute("select a.rtt/b.rtt as ratio from proximity_rtt as a, proximity_dns as b where a.ip = b.ip")
entry = cur.fetchone()
file = open('latency_ratio.txt','w')
while entry:
	file.write(str(entry[0])+'\n')
	entry = cur.fetchone()
file.close()
