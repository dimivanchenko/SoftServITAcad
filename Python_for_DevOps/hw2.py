import os
import sys
import json

file_name = str(sys.argv[1])
json_file_name = sys.argv[2]
test_file = sys.argv[3]

result = {
    'id': 0,
    'number': '0',
    'committer_name': '',
    'committer_email': ''
}
current_file = open(file_name)
json_data = json.load(current_file)
if json_data['matrix'] != 0:
    if int(json_data['number']) > int(result['number']):
        result['id'] = json_data['id']
        result['number'] = json_data['number']
        result['committer_name'] = json_data['committer_name']
        result['committer_email'] = json_data['committer_email']
current_file.close()


with open(sys.argv[3], 'w') as outfile:
    json.dump(result, outfile)
    
json_file_descriptor = open(json_file_name, 'w+')
json_file_descriptor.write(json.JSONEncoder().encode(result))
json_file_descriptor.close()