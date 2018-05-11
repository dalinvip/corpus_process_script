# @Author : bamtercelboo
# @Datetime : 2018/3/27 9:50
# @File : stoke.py
# @Last Modify Time : 2018/3/27 9:50
# @Contact : bamtercelboo@{gmail.com, 163.com}

"""
    FILE :  stoke.py
    FUNCTION : None
    EXAMPLE:
        Source:
        中
        TO:
        中: 丨フ一丨
"""

import urllib.request as urllib2
import urllib
from bs4 import BeautifulSoup
# solve encoding
from imp import reload
import sys
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)


class Stoke(object):
    # dictionary_filepath = "./default_stoke.txt"
    dictionary_filepath = "./Stoke/default_stoke.txt"
    # baiduhanyu_url = 'http://hanyu.baidu.com/zici/s?ptype=zici&wd=%s'
    hanzi5_url = "http://www.hanzi5.com/bishun/%s.html"

    def __init__(self):
        self.dictionary = {}
        self.read_dictionary()

    def read_dictionary(self):
        self.dictionary = {}
        with open(self.dictionary_filepath, encoding="UTF-8") as f:
            for line in f:
                line = line.strip("\n")
                line = line.split(" ")
                self.dictionary[line[0]] = line[1:]
        f.close()
        # print(self.dictionary)

    def get_stoke(self, word):
        if word in self.dictionary:
            return self.dictionary[word]
        else:
            print("From hanzi5:    word {}".format(word), end=" ")
            word = hex((ord(word)))[2:]
            word = urllib.parse.quote(word)
            return self.get_stoke_from_hanzi5(word)

    def get_stoke_from_hanzi5(self, word):
        url = self.hanzi5_url % word
        # print("url", url)
        html = self.post_baidu(url)
        # print(html)
        if html is None:
            return None
        char_stoke = self.anlysis_stoke_from_html(html)
        if char_stoke is not None:
            self.dictionary[word] = char_stoke
        # print("char_stoke {}".format(char_stoke))
        return char_stoke

    def anlysis_stoke_from_html(self, html_doc):
        soup = BeautifulSoup(html_doc, 'html.parser')
        li = soup.find("div", {"class", "site-article-content hanzi5-article-hanzi-info"})
        for tabb in li.findAll('table'):
            for trr in tabb.findAll('tr')[3:4]:
                for tdd in trr.findAll('td')[1:2]:
                    zh_stoke = tdd.contents
        zh_stoke_list = []
        for st in zh_stoke[0]:
            zh_stoke_list.append(st)
        return zh_stoke_list

    def post_baidu(self, url):
        try:
            timeout = 5
            request = urllib2.Request(url)
            request.add_header('User-agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36')
            request.add_header('connection','keep-alive')
            request.add_header('referer', url)
            response = urllib2.urlopen(request, timeout=timeout)
            html = response.read()
            response.close()
            return html
        except Exception as e:
            print('URL Request Error:', e)
            return None


if __name__ == "__main__":
    print("extract character stoke from [http://www.hanzi5.com/bishun/]")

    stoke = Stoke()
    print("中", stoke.get_stoke("中"))
    print("王", stoke.get_stoke("王"))
    print("像", stoke.get_stoke("像"))





