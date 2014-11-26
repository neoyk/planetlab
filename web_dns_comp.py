#! /usr/bin/python
import urllib2, math, os, sys, subprocess, shlex, re, time, socket, MySQLdb
pm =MySQLdb.connect(host='localhost',user='root',db='mnt')
cur =pm.cursor()
pm1 =MySQLdb.connect(host='localhost',user='root',db='mnt')
cur1 =pm1.cursor()
cur.execute("select a.ip, vantage, dns_ip from proximity_rtt as a, proximity_dns as b where a.ip=b.ip and vantage!='127.0.0.1'")
entry = cur.fetchone()
pattern =re.compile(r"^.*flags=SA.*rtt=(.*)\sms$")
pattern_ping =re.compile(r"^.*time=(.*)\sms$")

num = 0
print num,time.time()
while entry:
	num += 1
	if(num%50==0): print num,time.time()
	comp = []
	cmd_list = []
	ip, vantage, dns = entry
	cmd_list.append('hping3 -c 5 -S -p 22 '+ip)
	cmd_list.append('hping3 -c 5 -S -p 80 '+vantage)
	cmd_list.append('ping -c 5 '+dns)	# DNS resolver doesn't respond to hping3
	for cmd in  cmd_list:	
		rtt = []
		subp = subprocess.Popen(shlex.split(cmd),stdout=subprocess.PIPE,stderr=subprocess.PIPE)
		for msg in subp.stdout:
			result = pattern.search(msg)
			result_ping = pattern_ping.search(msg)
			if result:
				rtt.append(float(result.group(1)) )
			if result_ping:
				rtt.append(float(result_ping.group(1)) )
		if len(rtt):
			rtt.sort()
			idx =int( math.floor(len(rtt)/2) )
			comp.append( rtt[idx] )
	if len(comp)==3:
		sql = "replace into web_dns_comp values('{0}',{1},'{2}',{3},'{4}',{5})".format(entry[0],comp[0],entry[1],comp[1],entry[2],comp[2])
		print sql
		cur1.execute(sql)
	else:
		print entry, comp
	entry = cur.fetchone()
