import time
import json
import requests
import webbrowser
import urllib.error
import urllib.request
import urllib.parse
import http.cookiejar



time1 = 0.9
time2 = 1
runing = True
i=0
k=0
PC = "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
UA = PC
s1 = "KETX15132"
s2 = "21421P19"
s = s1
domain = "student"
pw1 = "OTcwNTAx"
pw2 = "MTIzNTM4"
pw = pw1        

while runing:           
    values={"username":s,"domain":domain,"password":pw,"enablemacauth":"0"}

    logUrl="http://n.njcit.cn/index.php/index/login"

    cook=http.cookiejar.CookieJar()

    openner=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cook))

    openner.addheaders = [('User-agent',UA)]

    r=openner.open(logUrl,urllib.parse.urlencode(values).encode())

    r=r.read().decode("utf-8")    

    r=json.loads(r)

    if r["info"]=="设备未响应":
        if requests.get('http://www.baidu.com').status_code==200:
            runing = False
            url = 'http://www.baidu.com'
            webbrowser.open(url)
            break
        else:
            continue
        
    if r["info"]=="认证失败, 请检查密码及账户状态" or r["info"]=="认证失败, 并发登录超过最大限制":
        k+=1
        s = s2
        pw = pw2
        if k>1:
            print("本地账号全不可用！请联系作者更新账号")
            break
        else:
            continue
        
    time.sleep(time1)
    values={}

    logUrl="http://n.njcit.cn/index.php/index/logout"

    cook=http.cookiejar.CookieJar()

    openner=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cook))

    openner.addheaders = [('User-agent', UA)]

    r=openner.open(logUrl,urllib.parse.urlencode(values).encode())

    r=r.read().decode("utf-8")    

    r=json.loads(r)

    if r["info"]=="设备未响应":
        if requests.get('http://www.baidu.com').status_code==200:
            runing = False
            url = 'http://www.baidu.com'
            webbrowser.open(url)
            break
        else:
            continue

    i+=1
    print('第%d次尝试......' %i)
    
    time.sleep(time2)
    if i>40:
        time1 = 0.5
        time2 = 0.6
        print("尝试修改时间...")
    if i>80:
        runing = False
        print("登录失败你今天的运气貌似不怎么好哦！")
        break

