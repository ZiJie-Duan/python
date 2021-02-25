from selenium import webdriver
import pyperclip
import xlrd
import xlwt


class WebDriver:
    """
    用于驱动chrome 采集药物信息的class
    """

    def __init__(self):
        self.driver_path = "/Users/lucy/Desktop/chromedriver"
        self.driver = webdriver.Chrome(self.driver_path)
        self.page_handle = {}
        self.search_list = []
        self.data = {
            "重量": "",
            "药物类型": "",
            "剂型": "",
            "说明书": "",
            "规格": ""
        }

    def init_data(self):
        self.data = {
            "重量": "",
            "药物类型": "",
            "剂型": "",
            "说明书": "",
            "规格": ""
        }

    def start(self, url):
        # 获取页面
        self.driver.get(url)

    def creat_url(self):
        # 生成url
        url_head = "https://search.jd.com/Search?keyword="
        url_middle = "&enc=utf-8&wq="
        url_end = "&pvid=533b86b10704452b995a8ff46cdb754b"
        url_body = '%20'.join(self.search_list)
        jd_url = url_head + url_body + url_middle + url_body + url_end

        url_head = "https://search.jianke.com/prod?wd="
        url_end = "&lg=1"
        url_body = '%20'.join(self.search_list)
        jianke_url = url_head + url_body + url_end

        url_head = "https://search.360kad.com/?pageText="
        url_body = "+".join(self.search_list)
        kad_url = url_head + url_body

        url_head = "https://www.baidu.com/s?wd="
        url_body = '%20'.join(self.search_list)
        baidu_url = url_head + url_body

        url_dir = {
            "jd_url": jd_url,
            "jianke_url": jianke_url,
            "kad_url": kad_url,
            "baidu_url": baidu_url
        }
        return url_dir

    def find_jd_good(self):
        # 查找京东 指定商品
        search_list = self.search_list
        goods = self.driver.find_elements_by_class_name("gl-i-wrap")
        for single_good_but in goods:
            elements = single_good_but.find_elements_by_class_name("skcolor_ljg")
            for element in elements:
                for v_element in search_list:
                    if v_element in element.text:
                        search_list.remove(v_element)
            if not search_list:
                return single_good_but

    def get_jd_information(self):
        # 获取详细信息
        js = "var q=document.documentElement.scrollTop=700"
        self.driver.execute_script(js)
        information_data_first_page = [data.text for data in
                                       self.driver.find_elements_by_css_selector("div>div>div>ul>li")]
        for data in information_data_first_page:
            if "商品毛重" in data:
                self.data["重量"] = data.split("：")[1]

        self.driver.find_element_by_css_selector("""[clstag="shangpin|keycount|product|pcanshutab"]""").click()
        information_name_list = [s_e.text for s_e in self.driver.find_elements_by_css_selector("div>div>dl>dl>dt")]
        information_data_list = [s_e.text for s_e in self.driver.find_elements_by_css_selector("div>div>dl>dl>dd")]

        for i in range(len(information_name_list)):
            if "药品分类" in information_name_list[i]:
                if "非处方药" in information_data_list[i]:
                    while 1:
                        user_c = input("[WebDriver.get_jd_information] 输入药物类型颜色(red/green)[r/g]>>")
                        if user_c == "r":
                            self.data["药物类型"] = "0"
                            break
                        elif user_c == "g":
                            self.data["药物类型"] = "2"
                            break
                        else:
                            print("[WebDriver.get_jd_information] 输入错误！")
                elif "处方药" in information_data_list[i]:
                    self.data["药物类型"] = "1"
                else:
                    self.data["药物类型"] = ""

            if "产品规格" in information_name_list[i]:
                self.data["规格"] = information_data_list[i]
            if "剂型" in information_name_list[i]:
                self.data["剂型"] = information_data_list[i]

        if self.data["剂型"] == "":
            print("未成功获取剂型，请手动填写")
            while True:
                u_in = input("请输入剂型：>>")
                if u_in:
                    self.data["剂型"] = u_in
                    break

        if self.data["药物类型"] == "":
            print("未成功获取药物类型，请手动填写")
            while True:
                u_in = input("请输入药品类型[r=0,g=2,none=1]：>>")
                if u_in:
                    self.data["药物类型"] = u_in
                    break

    def get_jd_guide(self):
        # 获取说明书
        # self.driver.find_element_by_css_selector("""[clstag="shangpin|keycount|product|shangpinjieshao_2"]""").click()
        # data_list = []
        # while True:
        #     data_in = input("[WebDriver.get_jd_guide] [c:continue]>>")
        #     data_list.append(pyperclip.paste())
        #     print("\n[WebDriver.get_jd_guide] 内容已读取！\n")
        #     if data_in != "c":
        #         break
        # data = "\n".join(data_list)

        # self.data["说明书"] = data
        self.data["说明书"] = ""

    def open_new_page(self, url, name):
        js = 'window.open("{}");'.format(url)
        self.driver.execute_script(js)
        self.page_handle[name] = self.driver.window_handles[-1]

    def open_other_web(self, url_dir):
        js = 0
        for _, url in url_dir.items():
            js += 1
            self.open_new_page(url=url, name="other_web_" + str(js))
            print(self.driver.current_window_handle)

    def add_page(self, name):
        self.page_handle[name] = self.driver.window_handles[-1]

    def del_page(self, name):
        self.driver.switch_to.window(self.page_handle[name])
        self.driver.close()
        del self.page_handle[name]

    def clean_page(self):
        handle_list = self.driver.window_handles
        for handle in handle_list:
            if handle == self.page_handle["search-page"]:
                pass
            else:
                self.driver.switch_to.window(handle)
                self.driver.close()
        handle = self.page_handle["search-page"]
        self.page_handle = {"search-page": handle}

    def change_page(self, name):
        self.driver.switch_to.window(self.page_handle[name])


class KZFMedicineData:

    def __init__(self):
        self.excel_path = "/Users/lucy/Desktop/药品信息采集/test1.xls"
        self.table = None
        self.main_row = 2
        self.newbook = xlwt.Workbook(encoding='utf-8')
        self.newsheet = self.newbook.add_sheet('My Worksheet')
        self.location = {
            "商品": 2,
            "品牌": 4,
            "state": 5,
            "规格": 7,
            "剂型": 10,
            "药物类型": 11,
            "重量": 14,
            "说明书": 15
        }
        self.data = {
            "商品": "",
            "品牌": "",
            "state": "",
            "规格": "",
            "剂型": "",
            "药物类型": "",
            "重量": "",
            "说明书": ""
        }

    def init_data(self):
        self.data = {
            "商品": "",
            "品牌": "",
            "state": "",
            "规格": "",
            "剂型": "",
            "药物类型": "",
            "重量": "",
            "说明书": ""
        }

    def load_table(self):
        data = xlrd.open_workbook(self.excel_path)
        self.table = data.sheet_by_name("Sheet1")

    def load_data(self):
        row = self.main_row
        for name, col in self.location.items():
            self.data[name] = self.table.cell(row, col).value

    def write_data(self):
        row = self.main_row
        for name, col in self.location.items():
            self.newsheet.write(row, col, self.data[name])

    def save_table(self):
        self.newbook.save("/Users/lucy/Desktop/数据测试版本aba.xls")

    def movedown(self):
        self.main_row += 1
        self.data = {
            "商品": "",
            "品牌": "",
            "state": "",
            "规格": "",
            "剂型": "",
            "药物类型": "",
            "重量": "",
            "说明书": ""
        }


class SystemCore:
    """
    程序中层驱动
    """

    def __init__(self):
        self.main_data = KZFMedicineData()
        self.main_data.load_table()
        self.web = WebDriver()
        self.urls = {}

    def printl(self, mod):
        # 格式化输出函数
        if mod == "search":
            for key, value in self.main_data.data.items():
                if key == "商品" or key == "品牌":
                    print("{} : {}".format(key, value))
        elif mod == "no_guide":
            for key, value in self.main_data.data.items():
                if key == "说明书":
                    print("{} : {}".format(key, value[:20]))
                else:
                    print("{} : {}".format(key, value))
        elif mod == "all":
            for key, value in self.main_data.data.items():
                print("{} : {}".format(key, value))

    def prepare_search(self):
        print("[prepare_search]:即将开始数据预处理")
        self.main_data.load_data()
        self.printl(mod="search")
        self.main_data.load_data()
        self.web.search_list = [self.main_data.data["商品"], self.main_data.data["品牌"]]
        self.urls = self.web.creat_url()
        print("[prepare_search]:数据预处理完成!")

    def jd_find_inventory(self):
        # 用于查找货物的函数
        print("[jd_find_inventory]:即将开始搜索")
        self.web.start(url=self.urls["jd_url"])
        self.web.add_page(name="search-page")
        goods_but = self.web.find_jd_good()
        if not goods_but:
            print("[jd_find_inventory]:没有！找到商品！")
            return False
        print("[jd_find_inventory]:已找到商品")
        return goods_but

    def jd_get_detail(self, goods_but, mod="auto"):
        # 用于获取信息的函数
        if mod == "auto":
            goods_but.click()
        if mod == "human":
            pass
        self.web.add_page(name="goods")
        self.web.change_page(name="goods")
        self.web.get_jd_information()
        self.web.get_jd_guide()
        print("[jd_get_detail]: 信息收集完成！")

    def roll_back(self, mod="jd"):
        if mod == "jd":
            self.web.del_page("goods")
            self.web.change_page(name="search-page")
            self.main_data.init_data()
            self.web.init_data()
        if mod == "other_web":
            self.web.clean_page()
            self.web.change_page(name="search-page")
            self.main_data.init_data()
            self.web.init_data()

    def save_change(self):
        self.main_data.write_data()
        self.main_data.movedown()
        self.main_data.save_table()
        self.web.clean_page()
        self.web.change_page(name="search-page")
        print("\n [save_change] 保存完成！\n")
        self.web.init_data()

    def search_by_human(self):
        # 用于辅助人类搜索的函数
        print("辅助性搜索！")
        self.web.open_other_web(self.urls)

        for detail in ["剂型", "药物类型"]:
            while True:
                u_in = input("[search_by_human] {}:>>".format(detail))
                if u_in:
                    u_in2 = input("[search_by_human] {} = {}, 是否正确？[y/n]".format(detail, u_in))
                    if u_in2 == "y":
                        self.main_data.data[detail] = u_in
                        break
        self.main_data.data["重量"] = "0.1kg"
        self.main_data.data["说明书"] = ""

    def verify_final_data(self, mod="jd"):
        self.printl(mod="no_guide")

        while True:
            us_tate = input("[verify_final_data] 数据是否合格[y/n]：")
            if us_tate == "n":
                self.main_data.data["state"] += '/数据不合格'
                break
            elif us_tate == "y":
                self.main_data.data["state"] += '/数据校验合格'
                break
            else:
                print("[verify_final_data] 输入错误！")

        while True:
            us_tate = input("[verify_final_data] 回滚数据roll_back/保存数据save/跳过录入skip [r/s/sk]：")
            if us_tate == "r":
                self.roll_back(mod=mod)
                break
            elif us_tate == "s":
                self.save_change()
                break
            elif us_tate == "sk":
                self.pass_inventory()
                break
            else:
                print("[verify_final_data] 输入错误！")

    def verify_jd_goods_by_human(self):
        while True:
            u_in = input("[verify_jd_goods_by_human] 是否包含商品？[y/n]>>")
            if u_in == "y":
                input("[verify_jd_goods_by_human] 请点击目标商品，并按下回车，开始采集")
                return True
            elif u_in == "n":
                input("[verify_jd_goods_by_human] 按下回车，开启其他页面")
                return False

    def verify_web_data(self):
        # 用于验证数据是否正确的函数

        # print("[verify_final_data] 开始验证数据！")
        # while True:
        #     u_in = input(
        #         "[verify_final_data] {} = {}, 是否正确[y/n]：".format(self.web.data["规格"], self.main_data.data["规格"]))
        #     if u_in == "n":
        #         self.main_data.data["state"] += "/产品规格不匹配"
        #         break
        #     elif u_in == "y":
        #         break
        #     else:
        #         print("[verify_final_data] 输入错误！")

        self.main_data.data["剂型"] = self.web.data["剂型"]
        self.main_data.data["药物类型"] = self.web.data["药物类型"]
        self.main_data.data["重量"] = self.web.data["重量"]
        self.main_data.data["说明书"] = self.web.data["说明书"]

    def pass_inventory(self):
        self.web.clean_page()
        self.web.change_page(name="search-page")
        self.main_data.init_data()
        self.main_data.data["state"] += "/跳过录入"
        self.main_data.write_data()
        self.main_data.movedown()
        self.main_data.save_table()
        print("\n [pass_inventory] 跳过保存完成！\n")


def main():
    print("康中福信息收集脚本 V1.3")
    core = SystemCore()
    while True:
        core.prepare_search()
        but = core.jd_find_inventory()
        if but:
            core.jd_get_detail(goods_but=but)
            core.verify_web_data()
            core.verify_final_data()
        else:
            if core.verify_jd_goods_by_human():
                core.jd_get_detail(goods_but=but, mod="human")
                core.verify_web_data()
                core.verify_final_data()
            else:
                core.search_by_human()
                core.verify_final_data(mod="other_web")

main()
