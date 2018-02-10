import os
import time
import datetime
ljx = os.getcwd()

def times():
	now_time = time.strftime('%Y%m%d')
	return now_time

def wltimes():
	timelb = []
	for z in range(1,8):
		nowtime=datetime.datetime.now()
		detaday=datetime.timedelta(days=z)
		da_days=nowtime+detaday
		wltime = da_days.strftime('%Y%m%d')
		timelb.append(wltime)
	now_time = time.strftime('%Y%m%d')
	timelb.append(now_time)
	return timelb

def jznow_time():
	hi = times()
	hii = hex(int(hi))
	return hii

def jzwl_time():
	jztimelb = []
	hi_1 = wltimes()
	for hii_1 in hi_1:
		hiii = hex(int(hii_1))
		jztimelb.append(hiii)
	return jztimelb


def put_time():
	timexx = jzwl_time()
	jdlj = os.path.join(ljx,'lucycore','sym.txt')
	with open(jdlj,'w') as x:
		x.write(str(timexx))

def corez():
	z = jznow_time()
	my = z + hex(20020531)
	return my
	


