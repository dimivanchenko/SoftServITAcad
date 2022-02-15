import sys
import paramiko
import os

#host_addr = sys.argv[1]
#ssh_port = int(sys.argv[2])
#uname = sys.argv[3]
#path_to_folder = sys.argv[4]
#folder_prefix = sys.argv[5]
#folder_count = int(sys.argv[6])
#folder_mode = int(sys.argv[7])

passwd = 'admin'
host_addr = '192.168.1.8'
ssh_port = 22
uname='diva'
path_to_folder = '/SoftServ/Python'
folder_prefix = 'usr'
folder_count = 5
folder_mode = 551


print (host_addr)
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=host_addr, port=ssh_port, username=uname, password=passwd) 
for i in range (folder_count):
    command = "cd ~"+path_to_folder+ "&& mkdir -m "+str(folder_mode)+" "+folder_prefix+str(i+1)
    stdin, stdout, stderr = ssh.exec_command(command)
    if len(stderr.read())>0:
        print ("Error. Folder ~"+path_to_folder+"/"+folder_prefix+str(i+1)+" alredy exist")
    else:
        print ("Folder ~"+path_to_folder+"/"+folder_prefix+str(i+1)+" is created")


print (stdout.read())
print (stderr.read())

ssh.close()