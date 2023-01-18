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

#https://github.com/openai/whisper


SUB_TEXT = """[00:00.000 --> 00:08.000]  I'm actually having a party over here.
[00:08.000 --> 00:10.000]  You guys are more welcome to come with you guys.
[00:10.000 --> 00:11.000]  I know.
[00:11.000 --> 00:12.000]  Alright, for sure.
[00:12.000 --> 00:17.000]  Yeah, I got another box I got to get, but I'll be over there in just a minute.
[00:17.000 --> 00:18.000]  Alright, yeah.
[00:18.000 --> 00:31.000]  For sure.
[00:31.000 --> 00:34.000]  Let's make a toast to the neighbor.
[00:34.000 --> 00:35.000]  Well, thank you.
[00:35.000 --> 00:36.000]  Cheers.
[00:36.000 --> 00:38.000]  Welcome to the neighbor's house.
[00:38.000 --> 00:40.000]  Get ready to party.
[00:40.000 --> 00:41.000]  Uh-huh.
[00:41.000 --> 00:46.000]  And you can't even peek around my trailer.
[00:46.000 --> 00:49.000]  You came to the right place.
[00:49.000 --> 01:15.000]  Thank you."""

@MessageBox(mp)
class StrRWriter_Single:
    #文件读取写入器
    def __init__(self):
        self.subtitle_path = ""
        self.file_subtitle = None
    def open(self):
        self.file_subtitle = open(self.subtitle_path,"a",encoding='utf-8')
    
    def close(self):
        self.file_subtitle.close()
    
    def write_line(self,data):
        data += "\n"
        self.file_subtitle.write(data)


@MessageBox(mp)
class Whisper_Transformer:
    # Whisper result transfor to STR File structure
    def __init__(self):
        self.result_text = ""
        self.subtitles = []
        self.sub_index = -1
        self.sub_index_max = 0
        
    def format_subtitles(self):
        sub_list = self.result_text.split("\n")
        self.sub_index_max = len(sub_list)

        for single_sub_text in sub_list:
            sub_unit = []

            single_sub_text = single_sub_text[1:]
            temp = single_sub_text.split("]  ")

            temp_for_time = temp[0].split(" --> ")
            temp_for_time[0] = temp_for_time[0].replace(".",",")
            temp_for_time[0] = "00:" + temp_for_time[0]
            temp_for_time[1] = temp_for_time[1].replace(".",",")
            temp_for_time[1] = "00:" + temp_for_time[1]
            temp[0] = " --> ".join(temp_for_time)

            sub_unit.append(temp[0])
            sub_unit.append(temp[1])
            self.subtitles.append(sub_unit)
    
    def read_a_line(self):
        self.sub_index += 1
        if (self.sub_index < self.sub_index_max):
            #here sub_index_max is the num of lines in subtitle list
            #but the sub_index is a index
            return self.subtitles[self.sub_index]
        else:
            return ["ENDSIGN","ENDSIGN"]


@MessageBox(mp)
class TRANSLATOR:
    def __init__(self):
        self.apiurl = ""
        self.appid = ""
        self.secretyKey = ""
        self.gap = 0.2

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
            new = "[ERROR FOR TRANSLATE]"
        return new

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


class SUBTITLE_MAKER:

    def __init__(self,sw,wt,translator):
        self.subt_wr = sw
        self.whisper_transf = wt
        self.translator = translator 
        self.subt_index = 0

    def init_resource(self):
        self.whisper_transf.format_subtitles()
    
    def close_resource(self):
        pass

    def make(self):
        while True:
            self.subt_wr.open()

            line = self.whisper_transf.read_a_line()
            if line[0] == "ENDSIGN":
                break
            
            new = self.translator.translate_sentence(content=line[1])

            self.subt_index += 1
            self.subt_wr.write_line(data="")
            self.subt_wr.write_line(data=str(self.subt_index))
            self.subt_wr.write_line(data=str(line[0]))
            self.subt_wr.write_line(data=str(new))
            self.subt_wr.write_line(data=str(line[1]))

            self.subt_wr.close()

            print("")
            print(str(self.subt_index))
            print(str(line[0]))
            print(str(new))
            print(str(line[1]))


def main():
    wt = Whisper_Transformer()
    wt.result_text = SUB_TEXT

    sw = StrRWriter_Single()
    sw.subtitle_path = "sub.srt"

    trans = TRANSLATOR()
    trans.apiurl = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
    trans.appid = "" #check baidu account
    trans.secretyKey = ''

    subt_maker = SUBTITLE_MAKER(sw=sw,wt=wt,translator=trans)
    subt_maker.init_resource()
    subt_maker.make()
    subt_maker.close_resource()

if __name__ == "__main__":
    main()