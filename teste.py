from models import Zabbix

zabbix = Zabbix('http://10.241.0.4/zabbix')

zabbix.login(user='API', password='APIzabbix')

for n in zabbix.proxy('get'):
    print(n)