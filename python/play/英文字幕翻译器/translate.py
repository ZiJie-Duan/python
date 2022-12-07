import urllib
import hashlib
import random
import requests
import time
import sys

#使用message box格式化输出
from MessageBox import*
mp, print, orprint, printe, printse,\
printnn, printmid, print_mode_mute,\
print_mode_init = init_env()

@MessageBox(mp)
class StrRWriter:
    #文件读取写入器
    def __init__(self):
        self.subtitle_path = ""
        self.new_subtitle_path = ""
        self.file_subtitle = None
        self.file_new_subtitle = None
        self.line_tem = None
        self.init_file()
    
    def init_file(self):
        #根据启动参数，将字幕文件路径分割，并重新生成新的字幕路径
        self.subtitle_path = sys.argv[1]
        if self.subtitle_path[0] == '"' and self.subtitle_path[-1] == '"':
            self.subtitle_path = self.subtitle_path[1:-1]
        path_list_t = self.subtitle_path.split("\\")
        new_path_list = path_list_t[:-1]
        new_file_name = "cn_" + path_list_t[-1]
        new_path_list += [new_file_name]
        self.new_subtitle_path = "\\".join(new_path_list)

    def open(self):
        self.file_subtitle = open(self.subtitle_path,"r",encoding='utf-8')
        self.file_new_subtitle = open(self.new_subtitle_path,"w",encoding='utf-8')
    
    def close(self):
        self.file_subtitle.close()
        self.file_new_subtitle.close()
    
    def read_line(self):
        self.line_tem = self.file_subtitle.readline()
        return self.line_tem
    
    def write_line(self):
        self.file_new_subtitle.write(self.line_tem)

@MessageBox(mp)
class SUBTRANSLATE:

    def __init__(self,srw):
        self.srw = srw
        self.apiurl = ""
        self.appid = ""
        self.secretyKey = ""
        self.locate_state = 0
        self.end_sign = 0
        self.gap = 0.2

    def translate(self):
        #翻译循环
        self.srw.open()
        while True:
            if self.locate_sentence(self.srw.read_line()): #判断当前行是否为有效数据
                message = self.remove_enter(self.srw.line_tem)
                while self.locate_sentence(self.srw.read_line()): #如果有多行字幕，将其拼接
                    message += " "+self.remove_enter(self.srw.line_tem)
                new = self.translate_sentence(message)
                self.srw.line_tem = new+"\n\n" 
                #因为拼接字幕，使得数据序列中一个“\n”没有被记录
                #所以，此处new 后加入了两个换行符
                orprint("'{}' -> '{}'\n".format(message,new))

            if self.end_sign:
                break
            else:
                self.srw.write_line()
        self.srw.close()
        print("Translate Finish...")
        input()

    def translate_sentence(self,content):
        #翻译函数 带有错误处理
        cont_err = 0
        while cont_err < 3:
            cont_err += 1
            new = self.translateBaidu(content)
            if new == "-233":
                printe("Translate Error")
                print("function restart")
            else:
                break
        else:
            printse("Unsolvable Translate Error")
            print("Subtitle use original language and sign of error")
            new = self.srw.line_tem + " [ERROR FOR TRANSLATE]"
        return new

    def locate_sentence(self,content):
        #字幕语句定位器
        if len(content) == 11: #判定结束标记
            if content == "End End End":
                self.end_sign = 1
                return 0
        if len(content) == 30: #判定时间标记，时间标记后往往就是字幕
            if content[13:16] == "-->":
                self.locate_state = 1
                return 0
        if self.locate_state:
            if content=="\n":
                self.locate_state = 0
                return 0
            else:
                return 1
        return 0

    def remove_enter(self,content):
        #移除原始语句中的换行符，防止api翻译时出现问题
        if content:
            if content[-1] == "\n":
                content = content[:-1]
        return content

    def translate_check(self):
        orprint("\n\nTRANSLATE CHECK...")
        orprint("API: Baidu")
        orprint("Source file: " + self.srw.subtitle_path)
        orprint("Processed file: " + self.srw.new_subtitle_path)
        orprint("Language: EN -> CH")
        input("Press Enter to Start......")

    def translateBaidu(self, content, fromLang='en', toLang='zh'):
        salt = str(random.randint(32768, 65536))
        sign = self.appid + content + salt + self.secretyKey
        sign = hashlib.md5(sign.encode('utf-8')).hexdigest()

        apiurln = self.apiurl + '?appid=' + self.appid + '&q=' + urllib.parse.quote(
            content) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + salt + '&sign=' + sign
        try:
            time.sleep(self.gap)
            res = requests.get(apiurln)
            json_res = res.json()
            dst = str(json_res['trans_result'][0]['dst'])
            return dst

        except Exception as e:
            return "-233"

@MessageBox(mp,"normal")
def main():
    srw = StrRWriter()
    subt = SUBTRANSLATE(srw=srw)
    subt.apiurl = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
    subt.appid = "" #check baidu account
    subt.secretyKey = ''
    subt.translate_check() 
    subt.translate()
    input("[END OF THE PROGRAM]")


if __name__ == "__main__":
    main()