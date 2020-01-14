'''
封装一个requests方法
'''
import requests
from urllib import parse
from test_interface_auto.common.conf import Conf

class Login():

    def __init__(self,username,password):
        self.username=username
        self.password=password

    def login(self):
        login_header={'Content-Type':'application/x-www-form-urlencoded',
                      'charset':'UTF-8',
                      'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}
        body={'username':self.username,'password':self.password,'rememberMe':'false'}
        body_encode=parse.urlencode(body)
        login_url=Conf.test_url+"/login"
        s=requests.session()
        res=s.post(login_url,data=body_encode,headers=login_header)
        s.headers["User-Agent"]="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"
        s.headers["Cookie"]=res.headers["Set-Cookie"]
        return s

if __name__ == '__main__':
    s=Login(username="15637887286",password="1234qwer").login()
    print(s.headers)

