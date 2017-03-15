from personal_python_collections.cmd_utility import *
from personal_python_collections.networking import *
from personal_python_collections.regexp_string import *


# personal_python_collections.regexp_string的使用
def regexp_demo():
    # 查询的例子
    def search():
        print(RegExpString('windows 98').search_with_pattern(r'\d+').search_result)

    # 替换的例子
    def replace():
        print(RegExpString('windows 98').replace_with_pattern(r'\d+', 'XP').replace_result)

    # 遍历
    def item_list():
        for item in RegExpString('48 29 29 10').find_all(r'\d+').item_list:
            print(item)

    search()
    replace()
    item_list()


# personal_python_collections.networking的使用
def networking_demo():
    # get请求
    def get():
        web_text = Networking("http://www.cnblogs.com/").get().response.text
        print(web_text)

    # post请求
    def post():
        web_text = Networking("http://www.cnblogs.com/").post().response.text
        print(web_text)

    # 下载
    def download():
        def download_report(block_num, block_size, size):
            per = 100.0 * block_num * block_size / size
            print("%2.2f%%" % per)

        url = "http://hiphotos.baidu.com/mgzcalice/pic/item/ed96859676e2607dd0135ee4.jpg"
        dst = '/Users/YouXianMing/Desktop/ed96859676e2607dd0135ee4.jpg'

        network = Networking(url, dst, download_report).download()
        print(network.message)
        print(network.file_path)

    get()
    post()
    download()


# personal_python_collections.cmd_utility import的使用
def cmd_demo():

    def normal():

        print(Process("""cd / && ls | grep 'U'""").run().output)

    def special():

        print(Process('ping www.cnblogs.com').run(timeout=3).output)

    normal()
    special()


# regexp_demo()
# networking_demo()
# cmd_demo()