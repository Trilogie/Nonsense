import re

a = b'Last login: Wed Apr 22 05:11:44 2020 from 10.10.10.1\r\r\n\r\nenable\r\nterminal length 0\r\n\nenable\nterminal length 0\nArista3>\r\nArista3>enable\r\nArista3#terminal length 0\r\nPagination disabled.\r\nArista3#\r\nconfig t\r\nArista3#config t\r\nArista3(config)#show ip int bri\r\nInterface              IP Address         Status     Protocol         MTU\r\nLoopback0              3.3.3.3/24         up         up             65535\r\nManagement1            10.10.10.4/24      up         up              1500\r\nArista3(config)#'
b = a.split('\r\n')
c = b[14]
print(str(c))