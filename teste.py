from zabbixapi import Zabbix
from time import time


start = time()

zabbix = Zabbix('http://10.241.0.4/zabbix')

zabbix.login(user='API', password='APIzabbix')

hosts = [host['hostid'] for host in zabbix.host('get', {'output': 'hostid', 'groupids': '4'})]

n = [print(interface) for interface in zabbix.hostinterface('get', {'output': 'extend', 'hostids': hosts})]

end = time() - start
print('Time elapsed: {}'.format(round(end, 4))) #1.589