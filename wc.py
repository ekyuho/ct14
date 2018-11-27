import requests
import re
r = requests.get("https://yoondongju.yonsei.ac.kr/poet/poem.asp?ID=1")
r.encoding='euckr'
data = r.text
data = data[data.find('죽는 날까지'):data.find('바람에 스치운다.')+9]
data = re.sub('<br/*>',' ', data)
data = data.replace('.', ' ')
data = data.replace(',', ' ')
data = data.split()
print(data)

mydict = {}
for w in data:
    if w in mydict: mydict[w] += 1
    else: mydict[w] = 1

print(mydict)
for k in sorted(mydict, key=mydict.__getitem__, reverse=True):
    print(k, mydict[k])
