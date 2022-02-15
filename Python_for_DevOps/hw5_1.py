import os
import sqlite3

db = os.path.join(os.path.dirname(__file__), 'demo.db')
sql_update = '''update ServerPorts set port_number=222 where servers_id in (select servers_id from ServerProjects where projects_id in (select id from Projects where proj_name="Project3" )) and servers_id in (select id from Servers where servertypes_id in (select id from ServerTypes where type_name="apache"));'''
sql_select = '''select * from ServerPorts where servers_id in (select servers_id from ServerProjects where projects_id in (select id from Projects where proj_name="Project3" )) and servers_id in (select id from Servers where servertypes_id in (select id from ServerTypes where type_name="apache"));'''


with sqlite3.connect(db) as conn:
    print("Ports before update")
    cur = conn.cursor()
    cur.execute(sql_select)    
    for result in cur:
        print(result)
    print("Ports after update")
    cur.execute(sql_update)
    cur.execute(sql_select)
    for result in cur:
        print(result)
