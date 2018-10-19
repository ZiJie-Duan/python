# -- coding:utf-8--
import json
import paramiko
import re
import os
from urllib import request

server_ip = "0000.0000.0000.0000"
server_password = "0000000"


def get_st(bd,wl):
	#用于从server下载文件的函数
	ps = server_password
	transport = paramiko.Transport((server_ip, 22))
	transport.connect(username='root', password=ps)
	
	sftp = paramiko.SFTPClient.from_transport(transport)
	
	cs_1 = 0
	cs_2 = 0
	for bd_1 in bd:
		cs_1 += 1
		cs_2 = 0
		for wl_1 in wl:
			cs_2 += 1
			if cs_1 == cs_2:
				sftp.get(bd_1, wl_1)
	
	transport.close()



def put_st(bd,wl):
	#用于上传文件到server的函数
	ps = server_password
	transport = paramiko.Transport((server_ip, 22))
	transport.connect(username='root', password=ps)
	 
	sftp = paramiko.SFTPClient.from_transport(transport)
	
	cs_1 = 0
	cs_2 = 0
	for bd_1 in bd:
		cs_1 += 1
		cs_2 = 0
		for wl_1 in wl:
			cs_2 += 1
			if cs_1 == cs_2:
				sftp.put(bd_1, wl_1)
	 
	transport.close()



def local_path_name(file_dir):
	#用于获取某路径下所有子文件文件完整的路径
	local_path_lb = []
	for root, dirs, files in os.walk(file_dir):

		#print(root) #当前目录路径  
		#print(dirs) #当前路径下所有子目录  
		#print(files) #当前路径下所有非目录子文件

		for file in files:
			local_path = root + "\\" + file
			local_path_lb.append(local_path)
	return local_path_lb



def download(url,bd):
	request.urlretrieve(url,bd)


def file_list(file_dir):
	#用于获取相对路径下的文件目录
	row = local_path_name(file_dir)
	for x in row:
		re.sub(file_dir, "", row)
	
	