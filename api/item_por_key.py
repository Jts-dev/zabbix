from logon import login_no_zabbix

def pesquisa_items_por_key(key):

    zapi=login_no_zabbix()
    return (f"procurar por {key}")