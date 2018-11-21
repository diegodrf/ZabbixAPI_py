import requests
import json
from colorama import Fore, Style

class Zabbix:
    def __init__(self, server='http://URL_FOR_SERVER/zabbix'):
        self.server = '{}/api_jsonrpc.php'.format(server)
        self.headers = {'Content-Type': 'application/json-rpc'}
        self.id = '1'
        self.data = {'jsonrpc': '2.0',
                     'method': '',
                     'id': self.id,
                     'params': {},
                     }

    def apiinfo(self):
        # Retorna a versão da API. O usuário não pode estar autenticado para requisitar este método.
        self.data['method'] = 'apiinfo.version'
        response = requests.post(self.server, json.dumps(self.data), headers=self.headers)
        return response.json()['result']

    def login(self, user, password):
        self.data['method'] = 'user.login'
        self.data['params'] = {'user': user, 'password': password}
        try:
            response = requests.post(self.server, json.dumps(self.data), headers=self.headers)
        except Exception as error:
            print(error)
            return exit(1)

        try:
            self.data.setdefault('auth', response.json()['result'])
            self.id = response.json()['id']

            return response.json()['result']
        except:
            error_message = 'Error: {}\nMessage: {}'.format(response.json()['error']['message'],
                                                            response.json()['error']['data'])
            return Fore.RED + error_message + Style.RESET_ALL

    def logout(self):
        self.data['method'] = 'user.logout'
        self.data['params'] = {}
        response = requests.post(self.server, data=json.dumps(self.data), headers=self.headers)
        try:
            return response.json()['result']
        except:
            error_message = 'Error: {}\nMessage: {}'.format(response.json()['error']['message'],
                                                            response.json()['error']['data'])
            return Fore.RED + error_message + Style.RESET_ALL

    def __data(self, method, query, element):
        self.data['method'] = '{}.{}'.format(element, method)
        self.data['params'] = query
        response = requests.post(self.server, json.dumps(self.data), headers=self.headers)
        try:
            return response.json()['result']
        except:
            error_message = 'Error: {}\nMessage: {}'.format(response.json()['error']['message'],
                                                            response.json()['error']['data'])
            return Fore.RED + error_message + Style.RESET_ALL

    def host(self, method, query=None, element='host'):
        if query is None:
            query = {'output': 'extend'}
        return self.__data(method, query, element)

    def history(self, method, query=None, element='history'):
        if query is None:
            query = {'output': 'extend'}
        return self.__data(method, query, element)

    def trend(self, method, query=None, element='trend'):
        if query is None:
            query = {'output': 'extend'}
        return self.__data(method, query, element)

    def event(self, method, query=None, element='event'):
        if query is None:
            query = {'output': 'extend'}
        return self.__data(method, query, element)

    def problem(self, method, query=None, element='problem'):
        if query is None:
            query = {'output': 'extend'}
        return self.__data(method, query, element)

    def host(self, method, query=None, element='host'):
        if query is None:
            query = {'output': 'extend'}
        return self.__data(method, query, element)

    def hostgroup(self, method, query=None, element='hostgroup'):
        if query is None:
            query = {'output': 'extend'}
        return self.__data(method, query, element)

    def hostinterface(self, method, query=None, element='hostinterface'):
        if query is None:
            query = {'output': 'extend'}
        return self.__data(method, query, element)

    def usermacro(self, method, query=None, element='usermacro'):
        if query is None:
            query = {'output': 'extend'}
        return self.__data(method, query, element)

    def maintenance(self, method, query=None, element='maintenance'):
        if query is None:
            query = {'output': 'extend'}
        return self.__data(method, query, element)

    def item(self, method, query=None, element='item'):
        if query is None:
            query = {'output': 'extend'}
        return self.__data(method, query, element)

    def application(self, method, query=None, element='application'):
        if query is None:
            query = {'output': 'extend'}
        return self.__data(method, query, element)

    def trigger(self, method, query=None, element='trigger'):
        if query is None:
            query = {'output': 'extend'}
        return self.__data(method, query, element)

    def graph(self, method, query=None, element='graph'):
        if query is None:
            query = {'output': 'extend'}
        return self.__data(method, query, element)

    def graphitem(self, method, query=None, element='graphitem'):
        if query is None:
            query = {'output': 'extend'}
        return self.__data(method, query, element)

    def template(self, method, query=None, element='template'):
        if query is None:
            query = {'output': 'extend'}
        return self.__data(method, query, element)

    def discoveryrule(self, method, query=None, element='discoveryrule'):
        if query is None:
            query = {'output': 'extend'}
        return self.__data(method, query, element)

    def itemprototype(self, method, query=None, element='itemprototype'):
        if query is None:
            query = {'output': 'extend'}
        return self.__data(method, query, element)

    def triggerprototype(self, method, query=None, element='triggerprototype'):
        if query is None:
            query = {'output': 'extend'}
        return self.__data(method, query, element)

    def graphprototype(self, method, query=None, element='graphprototype'):
        if query is None:
            query = {'output': 'extend'}
        return self.__data(method, query, element)

    def hostprototype(self, method, query=None, element='hostprototype'):
        if query is None:
            query = {'output': 'extend'}
        return self.__data(method, query, element)

    def correlation(self, method, query=None, element='correlation'):
        if query is None:
            query = {'output': 'extend'}
        return self.__data(method, query, element)

    def action(self, method, query=None, element='action'):
        if query is None:
            query = {'output': 'extend'}
        return self.__data(method, query, element)

    def alert(self, method, query=None, element='alert'):
        if query is None:
            query = {'output': 'extend'}
        return self.__data(method, query, element)

    def service(self, method, query=None, element='service'):
        if query is None:
            query = {'output': 'extend'}
        return self.__data(method, query, element)

    def dashboard(self, method, query=None, element='dashboard'):
        if query is None:
            query = {'output': 'extend'}
        return self.__data(method, query, element)

    def screen(self, method, query=None, element='screen'):
        if query is None:
            query = {'output': 'extend'}
        return self.__data(method, query, element)

    def screenitem(self, method, query=None, element='screenitem'):
        if query is None:
            query = {'output': 'extend'}
        return self.__data(method, query, element)

    def templatescreen(self, method, query=None, element='templatescreen'):
        if query is None:
            query = {'output': 'extend'}
        return self.__data(method, query, element)

    def templatescreenitem(self, method, query=None, element='templatescreenitem'):
        if query is None:
            query = {'output': 'extend'}
        return self.__data(method, query, element)

    def map(self, method, query=None, element='map'):
        if query is None:
            query = {'output': 'extend'}
        return self.__data(method, query, element)

    def httptest(self, method, query=None, element='httptest'):
        if query is None:
            query = {'output': 'extend'}
        return self.__data(method, query, element)

    def drule(self, method, query=None, element='drule'):
        if query is None:
            query = {'output': 'extend'}
        return self.__data(method, query, element)

    def dcheck(self, method, query=None, element='dcheck'):
        if query is None:
            query = {'output': 'extend'}
        return self.__data(method, query, element)

    def dhost(self, method, query=None, element='dhost'):
        if query is None:
            query = {'output': 'extend'}
        return self.__data(method, query, element)

    def dservice(self, method, query=None, element='dservice'):
        if query is None:
            query = {'output': 'extend'}
        return self.__data(method, query, element)

    def user(self, method, query=None, element='user'):
        if query is None:
            query = {'output': 'extend'}
        return self.__data(method, query, element)

    def usergroup(self, method, query=None, element='usergroup'):
        if query is None:
            query = {'output': 'extend'}
        return self.__data(method, query, element)

    def mediatype(self, method, query=None, element='mediatype'):
        if query is None:
            query = {'output': 'extend'}
        return self.__data(method, query, element)

    def usermedia(self, method, query=None, element='usermedia'):
        if query is None:
            query = {'output': 'extend'}
        return self.__data(method, query, element)

    def iconmap(self, method, query=None, element='iconmap'):
        if query is None:
            query = {'output': 'extend'}
        return self.__data(method, query, element)

    def image(self, method, query=None, element='image'):
        if query is None:
            query = {'output': 'extend'}
        return self.__data(method, query, element)

    def proxy(self, method, query=None, element='proxy'):
        if query is None:
            query = {'output': 'extend'}
        return self.__data(method, query, element)

    def script(self, method, query=None, element='script'):
        if query is None:
            query = {'output': 'extend'}
        return self.__data(method, query, element)
