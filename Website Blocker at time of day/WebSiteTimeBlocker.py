"""
This program is designed to block certain websites passed in the "website list" during particular times between 8am-4pm (configurable)
Python accesses the hosts file, and appends it during that time. Subsequently after that time is over, it removes those entries from the host file as well

This has been created with a view that this can be set as a task scheduler on Windows. All customization have been made based on that enhancement

__author__: Arvind
__date__: 09/20/2017
"""
import time
from datetime import datetime as dt

#It should always be relative path when schedules
hosts_temp='hosts'
#host_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com"]
while True:
	if dt(dt.now().year,dt.now().month,dt.now().day,8)<dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
		#print("Working hours")
		with open(hosts_temp,'r+') as hostfile:
			content=hostfile.read()
			for website in website_list:
				if website in content:
					pass
				else:
					hostfile.write(redirect+" "+website+"\n")
	else:
 		#print("Fun Hours")
 		with open(hosts_temp,'r+') as hostfile:
 			#Readlines has been used to access the entire line
 			content=hostfile.readlines()
 			#Setting the pointer to the starting of the file
 			hostfile.seek(0)
 			for line in content:
 				if not any(website in line for website in website_list):
 					hostfile.write(line)
 			#Truncating the file of all the appends that are constantly being added
 			hostfile.truncate()
 	
 	#Sleep time has been set to 5 seconds		
	time.sleep(5)
