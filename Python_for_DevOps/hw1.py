import sys, os

folder_path=sys.argv[1]
prefix=sys.argv[2]
counts=int(sys.argv[3])
mode=int(sys.argv[4],base=8)

try:
   for i in range(counts):
       folder_name = os.path.join(os.path.expanduser('~'),folder_path,prefix+str(i+1))
       os.mkdir(folder_name,mode)
except OSError:
    print('Error. Folder alredy exist!')
else:
    print('Folder is created')
