# -*- encoding:utf-8 -*-
#  ur10的相关操作与反馈

#本地主机地址，服务器地址端口
host_ip = "192.168.3.88"
target_ip = ("192.168.3.99",30003)

###------------30003的事实反馈与解析----------------------###

class get_the_30003():
    def __init__(self):
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
    #    for key,value in dic.items():
    #        print('{key}:{value}'.format(key=key,value=value))
    #    print("Tool_vector_actual:",dic['Tool_vector_actual'])

    def get_the_tcp_pose（）：
        return dic['Tool_vector_actual']

    def get_the_tcp_speed():
        return dic['TCP speed actual']

###------------------获得返回信息-------------------------###
class get_info_ur():
    #发送一条命令：获得关节实际角度???
    def get_joint_positions():
		sk2= socket.socket()
		sk2.connect(target_ip)
		send_data1 ='def svt():\n get_actual_joint_positions()\nend\n'
		sk2.send(send_data1.encode('utf-8'))
		sk2.close()

###------------------运动与控制--------------------------###
class motion():
    #发送一条命令：设置免驱模式
    def freedrive_mode():
		sk2= socket.socket()
		sk2.connect(target_ip)
		send_data1 ='def svt():\n freedrive_mode()\nend\n'
		sk2.send(send_data1.encode('utf-8'))
		sk2.close()
    #发送一条命令：结束免驱模式
    def end_freedrive_mode():
		sk2 = socket.socket()
		sk2.connect(target_ip)
		send_data1 ='def svt():\n end_freedrive_mode()\nend\n'
		sk2.send(send_data1.encode('utf-8'))
		sk2.close()

    #发送一条命令：移动d距离
    def movel(pose,a1,v1):
        sk = socket.socket()
        sk.connect(target_ip)
        send_data1 = 'def svt():\n movel(pose,a=a1, v=v1, t=0, r=0)\nend\n'
        #send_data1 = 'def svt():\n movel(p[0.651,-0.210,0.421,3.217,0.124,-0.07],a=0.4, v=0.02, t=0, r=0)\nend\n'
        sk.send(send_data1.encode('utf8'))
        sk.close()

    #发送一条命令：移动d距离
    def stop():
        sk = socket.socket()
        sk.connect(target_ip)
        send_data1 = 'def svt():\n stop(2)\nend\n'
        sk.send(send_data1.encode('utf8'))
        sk.close()

    def move_distance():
        pass

    def move_continiue():
        pass


class ur_set():
    def powerdown():
        pass

    def set_payload(d):
        pass

    def set_tcp(pose):
        pass
