import sys, os, json

import_file = open(sys.argv[1])
users_data = json.load(import_file)
import_file.close()
result_file=sys.argv[2]


print("\"id\": "  + "\""+str(users_data.get("id"))+"\",")
print("\"number\": " + "\""+str(users_data.get("number"))+"\"")
print("\"committer_name\": "  + "\""+str(users_data.get("committer_name"))+"\",")
print("\"committer_email\": " + "\""+str(users_data.get("committer_email"))+"\"")


jdata={}
jdata['result']=[]
jdata['result'].append({
    'id': str(users_data.get("id")),
    'number': str(users_data.get("number")),
    'committer_name':str(users_data.get("committer_name")),
    'committer_email':str(users_data.get("committer_email"))
})

with open(sys.argv[2], 'w') as outfile:
    json.dump(jdata, outfile)


"""for attempt in users_data['matrix']:
	if float(users_data.get("id"))>0:
		print (str(float(users_data.get("id"))))
	else:
		print("error")"""