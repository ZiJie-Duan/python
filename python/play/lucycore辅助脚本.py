#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#os.system()

import os
import sys
import re
import paramiko

#工作路径
gzlj = os.getcwd()

server_ip = ""
server_port = ""
username = ""
password = ""


def help():
	print("")
	print("gso ------- 存入服务器信息")
	print("kky ------- 清除主机密钥")
	print("ssh ------- ssh连接服务器")
	print("dwj ------- 从服务器下载文件")
	print("pwj ------- 向服务器上传文件")
	print("scmd ------ 服务器终端命令运行")
	print("")
	print(":q -------- 退出脚本")


def D_way(x):
	way = os.path.join(gzlj, "Desktop", x)
	return way


def server_message():
	global server_ip
	global server_port
	global username
	global password
	print("服务器信息采集")
	server_ip = input("服务器ip：")
	server_port = input("端口：")
	username = input("用户名：")
	password = input("password:")



def kill_key():
	cmd = "ssh-keygen -R " + server_ip
	os.system(cmd)


def ssh_server():
	cmd = "ssh -p" + server_port + " " + username + "@" + server_ip
	print(password)
	os.system(cmd)


def download_wj():
	lj = input("way:")
	name = input("name:")
	bd_lj = D_way(name)
	print(password)
	cmd = "scp -P" + server_port + " " + username + "@" + server_ip + ":" + lj + " " + bd_lj
	os.system(cmd)
	
def put_wj():
	lj = input("way:")
	name = input("name:")
	bd_lj = D_way(name)
	print(password)
	cmd = "scp -P" + server_port + " " + bd_lj + " " + username + "@" + server_ip + ":" + lj
	os.system(cmd)


def server_cmd():
	cmd = input("cmd:")
	ps = password
	client = paramiko.SSHClient()

	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

	client.connect(server_ip, username='root', password=ps, timeout=5)

	client.exec_command(cmd)


def start():

	core = input("core:")

	if core == ":q":
		print("退出lucycore辅助脚本！")
		sys.exit()


	if core == "sgo":
		server_message()


	if core == "kky":
		kill_key()


	if core == "ssh":
		ssh_server()


	if core == "dwj":
		download_wj()


	if core == "pwj":
		put_wj()


	if core == "scmd":
		server_cmd()


	if core == "help":
		help()

	start()


start()

