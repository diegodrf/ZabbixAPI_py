import requests
import json


class Zabbix:
    def __init__(self, server):
        self.server = '{}/api_jsonrpc.php'.format(server)
        self.headers = {'Content-Type': 'application/json-rpc'}
        self.id = '1'
        self.data = {'jsonrpc': '2.0',
                     'method': '',
                     'id': self.id,
                     'params': {},
                     }

    def apiinfo(self):
        self.data['method'] = 'apiinfo.version'
        response = requests.post(self.server, json.dumps(self.data), headers=self.headers)

        return response.json()['result']

    def login(self, user, password):
        self.data['method'] = 'user.login'
        self.data['params'] = {'user': user, 'password': password}

        response = requests.post(self.server, json.dumps(self.data), headers=self.headers)

        self.data.setdefault('auth', response.json()['result'])
        self.id = response.json()['id']

        return response.json()['result']

    def __data(self, method, query, element):
        self.data['method'] = '{}.{}'.format(element, method)
        self.data['params'] = query
        return requests.post(self.server, json.dumps(self.data), headers=self.headers).json()['result']

    def host(self, method, query={'output': 'extend'}, element='host'):
        return self.__data(method, query, element)

    def history(self, method, query={'output': 'extend'}, element='history'):
        return self.__data(method, query, element)

    def trend(self, method, query={'output': 'extend'}, element='trend'):
        return self.__data(method, query, element)

    def event(self, method, query={'output': 'extend'}, element='event'):
        return self.__data(method, query, element)

    def problem(self, method, query={'output': 'extend'}, element='problem'):
        return self.__data(method, query, element)

    def host(self, method, query={'output': 'extend'}, element='host'):
        return self.__data(method, query, element)

    def hostgroup(self, method, query={'output': 'extend'}, element='hostgroup'):
        return self.__data(method, query, element)

    def hostinterface(self, method, query={'output': 'extend'}, element='hostinterface'):
        return self.__data(method, query, element)

    def usermacro(self, method, query={'output': 'extend'}, element='usermacro'):
        return self.__data(method, query, element)

    def maintenance(self, method, query={'output': 'extend'}, element='maintenance'):
        return self.__data(method, query, element)

    def item(self, method, query={'output': 'extend'}, element='item'):
        return self.__data(method, query, element)

    def application(self, method, query={'output': 'extend'}, element='application'):
        return self.__data(method, query, element)

    def trigger(self, method, query={'output': 'extend'}, element='trigger'):
        return self.__data(method, query, element)

    def graph(self, method, query={'output': 'extend'}, element='graph'):
        return self.__data(method, query, element)

    def graphitem(self, method, query={'output': 'extend'}, element='graphitem'):
        return self.__data(method, query, element)

    def template(self, method, query={'output': 'extend'}, element='template'):
        return self.__data(method, query, element)

    def discoveryrule(self, method, query={'output': 'extend'}, element='discoveryrule'):
        return self.__data(method, query, element)

    def itemprototype(self, method, query={'output': 'extend'}, element='itemprototype'):
        return self.__data(method, query, element)

    def triggerprototype(self, method, query={'output': 'extend'}, element='triggerprototype'):
        return self.__data(method, query, element)

    def graphprototype(self, method, query={'output': 'extend'}, element='graphprototype'):
        return self.__data(method, query, element)

    def hostprototype(self, method, query={'output': 'extend'}, element='hostprototype'):
        return self.__data(method, query, element)

    def correlation(self, method, query={'output': 'extend'}, element='correlation'):
        return self.__data(method, query, element)

    def action(self, method, query={'output': 'extend'}, element='action'):
        return self.__data(method, query, element)

    def alert(self, method, query={'output': 'extend'}, element='alert'):
        return self.__data(method, query, element)

    def service(self, method, query={'output': 'extend'}, element='service'):
        return self.__data(method, query, element)

    def dashboard(self, method, query={'output': 'extend'}, element='dashboard'):
        return self.__data(method, query, element)

    def screen(self, method, query={'output': 'extend'}, element='screen'):
        return self.__data(method, query, element)

    def screenitem(self, method, query={'output': 'extend'}, element='screenitem'):
        return self.__data(method, query, element)

    def templatescreen(self, method, query={'output': 'extend'}, element='templatescreen'):
        return self.__data(method, query, element)

    def templatescreenitem(self, method, query={'output': 'extend'}, element='templatescreenitem'):
        return self.__data(method, query, element)

    def map(self, method, query={'output': 'extend'}, element='map'):
        return self.__data(method, query, element)

    def httptest(self, method, query={'output': 'extend'}, element='httptest'):
        return self.__data(method, query, element)

    def drule(self, method, query={'output': 'extend'}, element='drule'):
        return self.__data(method, query, element)

    def dcheck(self, method, query={'output': 'extend'}, element='dcheck'):
        return self.__data(method, query, element)

    def dhost(self, method, query={'output': 'extend'}, element='dhost'):
        return self.__data(method, query, element)

    def dservice(self, method, query={'output': 'extend'}, element='dservice'):
        return self.__data(method, query, element)

    def user(self, method, query={'output': 'extend'}, element='user'):
        return self.__data(method, query, element)

    def usergroup(self, method, query={'output': 'extend'}, element='usergroup'):
        return self.__data(method, query, element)

    def mediatype(self, method, query={'output': 'extend'}, element='mediatype'):
        return self.__data(method, query, element)

    def usermedia(self, method, query={'output': 'extend'}, element='usermedia'):
        return self.__data(method, query, element)

    def iconmap(self, method, query={'output': 'extend'}, element='iconmap'):
        return self.__data(method, query, element)

    def image(self, method, query={'output': 'extend'}, element='image'):
        return self.__data(method, query, element)

    def usermacro(self, method, query={'output': 'extend'}, element='usermacro'):
        return self.__data(method, query, element)

    def proxy(self, method, query={'output': 'extend'}, element='proxy'):
        return self.__data(method, query, element)

    def script(self, method, query={'output': 'extend'}, element='script'):
        return self.__data(method, query, element)
