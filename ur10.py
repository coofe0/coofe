# -*- encoding:utf-8 -*-
import socket		#导入socket模块
import struct		#导入模块处理二进制数据（C语言中的结构体）
import math
#import numpy as np

#本地主机地址，服务器地址端口
host_ip = "192.168.3.88"
target_ip = ("192.168.3.99",30003)

#打开socket,#链接服务端
#s=socket.socket(socket,AF_INET,socket.STREAM)
s=socket.socket()
s.connect(target_ip)

#将字节所表示的名称和字节类型放入字典中（字节数共有1060个）
dic={'MessageSize':'i','Time':'d','q_target':'6d','qd target':'6d',
    'qdd target':'6d','qddd target':'6d','M target':'6d','q actual':'6d',
    'qd actual':'6d','I actual':'6d','I control':'6d','Tool_vector_actual':'6d',
    'TCP speed actual':'6d','TCP_force':'6d','Tool vector target':'6d','TCP speed target':'6d',
    'Digital input bits':'d','Motor temperatures':'6d','Controller Timer':'d','Test value':'d',
    'Robot Mode':'d','Joint Modes':'6d','Safety Mode':'d','software only':'6d',
    'Tool Accelerometer':'3d','Robots software only':'6d','Speed scaling':'d','Linear momentum norm':'d',
    'Robots software':'d','Used Robots':'d','V main':'d','V robot':'d',
    'I robot':'d','V actual':'6d','Digital outputs':'d','Program state':'d'
    }

#按照字典的格式解析,解析之后的数据再放入字典中
data=s.recv(1060)
names=[]
ii=range(len(dic))
for key,i in zip(dic,ii):
    format_size=struct.calcsize(dic[key])                   #calcsize格式占多少个字节
    data1,data=data[0:format_size],data[format_size:]       #列表第一个分割出来
    format='!'+dic[key]                            #“！”对齐方式：network
    names.append(struct.unpack(format,data1))       #解包，加到names列表中
#    dic[key]=dic[key],struct.unpack(format,data1)
    dic[key]=struct.unpack(format,data1)
#print(names)
#print(dic)
for key,value in dic.items():
    print('{key}:{value}'.format(key=key,value=value))

print("*"*20)
print("Tool_vector_actual:",dic['Tool_vector_actual'])
print("*"*20)
print("TCP_force:",dic['TCP_force'])
