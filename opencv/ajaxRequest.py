from urllib import parse,request
import json
def get_distance():
    request_url='http://192.168.1.9/'
    header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',"Content-Type": "application/json",'X-Requested-With':'XMLHttpRequest'}
    param={'k':'w'}
    param=json.dumps(param).encode(encoding='utf-8')
    print("param:{0}".format(param))
    req=request.Request(url=request_url,data=param,headers=header_dict)
    res=request.urlopen(req)
    res=res.read()
    print("res:{0}".format(res))
    print("res_decode:{0}".format(res.decode(encoding='utf-8')))
    return res