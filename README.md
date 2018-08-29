# ZabbixAPI

Esta biblioteca foi criada com o intuito de facilitar as consultas junto a API do Zabbix.

Foi criada utilizando como base o Zabbix 3.4.

Como utilizar:

from zabbixapi import Zabbix

zabbix = Zabbix('server') # 'server' é o endereço de acesso web do seu servidor. Ex.: http://127.0.0.1/zabbix

zabbix.login('user', 'password') # Deve ser utilizado um usuário com acesso a interface web e que possua as permissões desejadas.

zabbix.host(method='get', query={'output': 'hostid'}) # Caso o login tenha sido realizado com sucesso, retornará o ID de todos os hosts. (É recomendável utilizar o parâmetro "query" apenas com o valor de output desejado. Consulte a documentação da Zabbix SIA para obter detalhes. )

zabbix.host('get') # Retornará a lista de todos os hosts com todas as propriedades disponíveis (Dependendo da sua base, esta consulta pode demanadar muita carga do banco.)

O valor padrão para o parâmetro query é {"output": "extend"}. Ou seja, se nada for passado neste parâmetro, a consulta será feita utilizando este modo de retorno na API.