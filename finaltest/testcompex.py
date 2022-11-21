import sys
import os
import os.path
import time
#import pdb
#pdb.set_trace()
#read number of lines first to check if need to more copy later

storred_num_lines = 0
num_lines = 0
with open(firstlogfile.txt, 'r') as x:
    for line in x:
        num_lines += 1
    if  num_lines > storred_num_lines:
        with open('firstlogfile.txt','r') as mainlog, open('unilogfile.txt','w') as unilog:
            for line in mainlog:
                unilog.write(line)
    else:
        
#with open('firstlogfile.txt','r') as mainlog, open('unilogfile.txt','w') as unilog:
#    for line in mainlog:
#        unilog.write(line)
