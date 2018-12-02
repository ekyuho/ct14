import requests

key = 'you own key please'
path = 'http://openapi.gbis.go.kr/ws/rest/buslocationservice';
route = '234000002'  # 9000번 버스

url = '%s?serviceKey=%s&routeId=%s'%(path, key, route)
print(url)
r = requests.get(url)
print('status= %s'%r.status_code)
print(r.text)

''' 성공하면 이런 답이 
<?xml version="1.0" encoding="UTF-8" standalone="yes"?><response><comMsgHeader><errMsg>NORMAL SERVICE.</errMsg><returnCode>00</returnCode></comMsgHeader><msgHeader><queryTime>2018-12-02 15:15:16.790</queryTime><resultCode>0</resultCode><resultMessage>정상적으로 처리되었습니다.</resultMessage></msgHeader><msgBody><busLocationList><endBus>0</endBus><lowPlate>0</lowPlate><plateNo>경기77바1117</plateNo><plateType>3</plateType><remainSeatCnt>30</remainSeatCnt><routeId>234000002</routeId><stationId>206000322</stationId><stationSeq>13</stationSeq></busLocationList><busLocationList><endBus>0</endBus><lowPlate>0</lowPlate><plateNo>경기77바1056</plateNo><plateType>3</plateType><remainSeatCnt>26</remainSeatCnt><routeId>234000002</routeId><stationId>277103678</stationId><stationSeq>48</stationSeq></busLocationList><busLocationList><endBus>0</endBus><lowPlate>0</lowPlate><plateNo>경기77바1015</plateNo><plateType>3</plateType><remainSeatCnt>18</remainSeatCnt><routeId>234000002</routeId><stationId>101000148</stationId><stationSeq>40</stationSeq></busLocationList><busLocationList><endBus>0</endBus><lowPlate>0</lowPlate><plateNo>경기77바1170</plateNo><plateType>3</plateType><remainSeatCnt>23</remainSeatCnt><routeId>234000002</routeId><stationId>277103679</stationId><stationSeq>24</stationSeq></busLocationList><busLocationList><endBus>0</endBus><lowPlate>0</lowPlate><plateNo>경기77바1340</plateNo><plateType>3</plateType><remainSeatCnt>44</remainSeatCnt><routeId>234000002</routeId><stationId>206000171</stationId><stationSeq>72</stationSeq></busLocationList><busLocationList><endBus>0</endBus><lowPlate>0</lowPlate><plateNo>경기77바1114</plateNo><plateType>3</plateType><remainSeatCnt>41</remainSeatCnt><routeId>234000002</routeId><stationId>101000059</stationId><stationSeq>32</stationSeq></busLocationList></msgBody></response>
'''
