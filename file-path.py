import os.path
if os.path.isfile('ew.txt'):
    print('存在')
    file=open('new.txt','a')
    file.write('123456789')
    file.close()
    
    
else:
    print('no')
    file=open('ne.txt','w')
    file.write('123456789')
    file.close()
