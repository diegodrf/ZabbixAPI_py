import requests
from bs4 import BeautifulSoup

url = 'https://www.zabbix.com'


res = requests.get(url + '/documentation/3.4/manual/api/reference')
res.raise_for_status()

soup = BeautifulSoup(res.text, 'html.parser')
index = soup.select('.wikilink1')
for i in index:
    #print(url + i.get('href'))
    link = requests.get(url + i.get('href'))
    soup1 = BeautifulSoup(link.text, 'html.parser')
    getMethod = soup1.select('.wikilink1')
    for n in getMethod:
        if n.text.endswith('.get'):

            i = str(n.text).replace('.get','')

            print("def {}(self, method, query={}, element='{}'):\n\treturn self.__data(method, query, element)\n\n".format(i, "{'output': 'extend'}",i))


            """def host(self, method, query):
                self.data['method'] = 'host.{}'.format(method)
                self.data['params'] = query
                response = requests.post(self.server, json.dumps(self.data), headers=self.headers).json()
                return response.json()"""