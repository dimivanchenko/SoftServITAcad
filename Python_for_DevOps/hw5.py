import os, sys
import sqlite3


path_to_db = sys.argv[1]
#db = os.path.join(os.path.dirname(__file__), 'demo.db')
sql_update = '''update ServerPorts set port_number=111 where servers_id in (select servers_id from ServerProjects where projects_id in (select id from Projects where proj_name="Project3" )) and servers_id in (select id from Servers where servertypes_id in (select id from ServerTypes where type_name="apache"));'''
sql_select = '''select * from ServerPorts where servers_id in (select servers_id from ServerProjects where projects_id in (select id from Projects where proj_name="Project3" )) and servers_id in (select id from Servers where servertypes_id in (select id from ServerTypes where type_name="apache"));'''


conn = sqlite3.connect(path_to_db)
#conn = sqlite3.connect(db)
select_row = conn.execute(sql_select).fetchall() 

for row in select_row:
    print('id=' + str(row[0]) + '; servers_id=' + str(row[1]) + '; port_type=' + str(row[2]) + '; port_number=' + str(row[3])) 

input ('Pres any key') 

update_port = conn.execute(sql_update).fetchall()
select_row = conn.execute(sql_select).fetchall()


for row in select_row:
    print('id=' + str(row[0]) + '; servers_id=' + str(row[1]) + '; port_type=' + str(row[2]) + '; port_number=' + str(row[3]))

conn.commit()
conn.close()