from test_interface_auto.common.Login import Login

# 编辑联系人接口调用

s=Login("15637887286","1234qwer").login()
linkmanEditUrl="https://cccrmtest.taxchina.com/crm/linkman/edit"
linkmanEditBody={
                    "custId":"1761",
                    "lkmId": "2854",
                    "lkmName":"相同名字",
                    "lkmSex":"0",
                    "lkmMobile":"18010465347",
                    "lkmTel":"",
                    "lkmPostion":"相同名字",
                    "lkmWebchat":"联系人微信号",
                    "lkmQq":"",
                    "lkmEmail":"974106919@qq.com",
                    "lkmAddr":"2",
                    "lkmRemake":"",
                    "isMainLkm":"0",
}
# print(s.headers)
getWeekCustomerForMainPage_url="https://cccrmtest.taxchina.com/crm/finance/notice/userNoticeList"
for i in range(100):
    linkmanEditBody["lkmAddr"]=i
    res=s.post(linkmanEditUrl,data=linkmanEditBody)
    print(res.text)