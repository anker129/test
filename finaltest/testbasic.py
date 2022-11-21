#import pdb
#pdb.set_trace()
with open('firstlogfile.txt','r') as mainlog, open('unilogfile.txt','w') as unilog:
    for line in mainlog:
        unilog.write(line)
