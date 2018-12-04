import os
os.chdir('D:\\OneDrive\bus')

#with open('routestation20181204_2.txt', encoding='euckr')as f: d = f.read()
#d = d.split()

#stations = []
#for k in d:
#    j = k.split('|')
#    if j[0] == '234000002':
#        stations.append(k)

#for k in stations:
#    print(k)

with open('station20181204_2.txt', encoding='euckr') as f: d = f.read()
d = d.split()

def lookup(sid):
    for k in d:
        j = k.split('|')
        if j[0] == sid: print(j[0], j[7][:2]+'-'+j[7][2:],j[1], j[7])

#for k in stations:
#    sta = k.split('|')
#    lookup(sta[1])

print("===== this is it ======")
want = set(('206000182', '206000328', '277103678', '277103441', '101000026'))
for k in want:
    lookup(k)
