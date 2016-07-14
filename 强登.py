import os
import sys
import time
import json
import requests
import webbrowser
import urllib.error
import urllib.request
import urllib.parse
import  http.cookiejar
import tkinter.messagebox
from tkinter import *


root = Tk(className='somnus')
w=1


def callback(event):
    global w
    if w>0:
        
        tkinter.messagebox.showinfo(
        "提示",
        "Are you sure ?\n点击确定后\n请等待20s"
        )


        runing = True
        w-=1
        i=0
        k=0
        PC = "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        PHONE =  'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25'
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

            time.sleep(0.3)

            r=r.read().decode("utf-8")    
            r=json.loads(r)

            if r["info"]=="认证失败, 请检查密码及账户状态":
                k+=1
                s = s2
                pw = pw2
                if k>1:  
                    tkinter.messagebox.showinfo(
                    "提示",
                    "本地账号全不可用！\n请联系作者更新账号"
                    )
                    break
            
            if r["info"]=="认证失败, 并发登录超过最大限制":
                if UA == PC:
                    domain = "studentphone"
                    UA = PHONE
                else:
                    domain = "student"
                    UA = PC
                

            values={}

            logUrl="http://n.njcit.cn/index.php/index/logout"

            cook=http.cookiejar.CookieJar()

            openner=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cook))

            openner.addheaders = [('User-agent', UA)]

            r=openner.open(logUrl,urllib.parse.urlencode(values).encode())
            i+=1


            time.sleep(0.3)

  
            if i>80:

                tkinter.messagebox.showinfo(
                "提示",
                "登录失败\n你今天的运气貌似不怎么好哦！"
                )

                break

            
            def getStatusCode(url):
                r = requests.get(url, allow_redirects = False)
                return r.status_code
             
            if getStatusCode('http://www.baidu.com')==200:
                runing = False
                url = 'http://www.baidu.com'
                webbrowser.open(url)

                tkinter.messagebox.showinfo(
                    "提示",
                    "登录成功！"
                    )

                break

root.bind("<Motion>", callback)
    
photo = PhotoImage(file="i.png")
Label(root, image=photo).pack()

mainloop()

