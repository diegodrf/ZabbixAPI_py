# ZabbixAPI

Esta biblioteca foi criada com o intuito de facilitar as consultas junto a API do Zabbix.

* Utilizando como base o Zabbix 3.4.


## Como utilizar:

`pip install ZabbixAPI-py`

`from ZabbixAPI_py import Zabbix`

`zabbix = Zabbix('server')` _# 'server' é o endereço de acesso web do seu servidor. Ex.: http://127.0.0.1/zabbix_

`zabbix.login('user', 'password')` _# Deve ser utilizado um usuário com acesso a interface web e que possua as permissões desejadas._

`zabbix.host(method='get', query={'output': 'hostid'})` _# Caso o login tenha sido realizado com sucesso, retornará o ID de todos os hosts. (É recomendável utilizar o parâmetro "query" apenas com o valor de output desejado. Consulte a documentação da Zabbix SIA para obter detalhes. )_

`zabbix.host('get')` _# Retornará a lista de todos os hosts com todas as propriedades disponíveis (Dependendo da sua base, esta consulta pode demanadar muita carga do banco.)_

##

**O valor padrão para o parâmetro q****uery é {"output": "extend"}. Ou seja, se nada for passado neste parâmetro, a consulta será feita utilizando este modo de retorno na API.**