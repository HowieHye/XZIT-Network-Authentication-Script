import requests
import os

url = "http://172.16.49.2:801/eportal/"

welcome = """Hi there, I'm Howie.
Welcome to use echo XZIT-Network-Authentication-Script.
You can find me here. https://github.com/HowieHye"""
print(welcome)
inputusername = "请输入学号："
inputpasswd = "请输入密码："
selectoperator = """1：中国移动
2：中国联通
3：中国电信
请选择运营商："""

if os.path.exists('wifi.txt'):
    with open('wifi.txt', 'r') as f:
        lines = f.readlines()
        username = str(lines[0]).replace("\n", "").replace("\r", "")
        print("Your Username:" + username)
        passwd = str(lines[1]).replace("\n", "").replace("\r", "")
        print("Your Password:" + passwd)
        operatorcode = str(lines[2]).replace("\n", "").replace("\r", "")
        # print(operatorcode)
else:
    username = input(inputusername)
    passwd = input(inputpasswd)
    operatorcode = input(selectoperator)

if operatorcode == "1":
    operator = "cmcc"
elif operatorcode == "2":
    operator = "unicom"
elif operatorcode == "3":
    operator = "telecom"
else:
    print("运营商选择错误")
print("Your Operator:" + operator)
data = {
    "c": "ACSetting",
    "a": "Login",
    "loginMethod": "1",
    "protocol": "http:",
    "DDDDD": ",0," + username + "@" + operator,  # 电信 telecom 联通 unicom 移动 cmcc
    "upass": passwd,
    "R1": "0",
    "R2": "0",
    "R3": "0",
    "R6": "0",
    "pare": "00",
    "0MKKey": "123456"
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-CN;q=0.8,en;q=0.7",
    "Connection": "keep-alive",
    # "Cookie": "PHPSESSID=4kr1raa671ssetosan503bccv4",
    "Host": "172.16.49.2:801",
    "Referer": "http://172.16.49.2/",
    "Upgrade-Insecure-Requests": "1"
}

response = requests.get(url, data, headers=headers).status_code

# print(response.text)
if str(response) == "200":
    print("登陆成功！")
else:
    print("登陆失败！请检查是否已经连接到无线网！或者稍后重试")
input("按任意键退出...")
