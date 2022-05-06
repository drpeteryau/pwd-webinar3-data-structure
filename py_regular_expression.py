#Regular expression
#About Regular Expression (RE): https://en.wikipedia.org/wiki/Regular_expression
#Example Log from: https://www.ibm.com/docs/en/zos/2.3.0?topic=problems-example-log-file

import re

#A string that we are going to search from a text contents
#search = '9.37'
#search = '9.37.*'
#search = '.*9.37'
#search = '.*9.37.*'
#search = '.*9.67.100'
#search = '.*9.67.102'

contents = '03/22 08:51:06 TRACE  :...read_physical_netif: Home list entries returned = 7,'\
'03/22 08:51:06 INFO   :...read_physical_netif: index #0, interface VLINK1 has address 129.1.1.1, ifidx 0,'\
'03/22 08:51:07 INFO   :...read_physical_netif: index #1, interface TR1 has address 9.37.65.139, ifidx 1,'\
'03/22 08:51:10 INFO   :...read_physical_netif: index #2, interface LINK11 has address 9.67.100.1, ifidx 2,'\
'03/22 08:51:11 INFO   :...read_physical_netif: index #3, interface LINK12 has address 9.67.101.1, ifidx 3,'\
'03/22 08:51:12 INFO   :...read_physical_netif: index #4, interface CTCD0 has address 9.67.116.98, ifidx 4,'\
'03/22 08:51:55 INFO   :...read_physical_netif: index #5, interface CTCD2 has address 9.67.117.98, ifidx 5,'\
'03/22 08:51:55 INFO   :...read_physical_netif: index #6, interface LOOPBACK has address 127.0.0.1, ifidx 0,'\
'03/22 08:51:56 INFO   :....mailslot_create: creating mailslot for timer,'\
'03/22 08:51:59 INFO   :...mailbox_register: mailbox allocated for timer,'

#Compare
result = re.match(search, contents)

if result:
  print("Found")
else:
  print("Not Found")	
