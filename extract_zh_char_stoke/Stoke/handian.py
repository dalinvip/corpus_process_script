# @Author : bamtercelboo
# @Datetime : 2018/3/28 8:24
# @File : handian.py
# @Last Modify Time : 2018/3/28 8:24
# @Contact : bamtercelboo@{gmail.com, 163.com}

"""
    FILE :  handian.py
    FUNCTION : the simulation of handian action
"""

import requests
import time


class Handian(object):

    def __init__(self):

        self.headers = {
            "Host": "www.zdic.net",
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "zh-TW,zh-CN;q=0.8,zh;q=0.6,en;q=0.4,en-US;q=0.2",
            "Accept-Encoding": "gzip, deflate",
            "Referer": "http://www.zdic.net/z/15/js/4EBA.htm",
            "Cookie": "UM_distinctid=16264efc020144-0cdc7740ca36d5-4323461-1aeaa0-16264efc02125e; "
                      "ASPSESSIONIDCATTBADD=BIHGOGEBNPJNLMMGMHHJAKOP; ASPSESSIONIDCSSQSCSA=GCIALALAGJGGICPDGLHIFDDK; "
                      "CNZZDATA524192=cnzz_eid%3D915161487-1522106804-null%26ntime%3D1522193207; cxls=%E6%9E%97; lb%5Fc=mh; "
                      "lb%5Fb=mh; lb%5Fa=hp; tp=tp1; ASPSESSIONIDASQSRBQC=JDMHPALADHOGFHIPCAICKLNM", # 由于字数限制，这里省略掉cookie，见下文的回答
            "Connection": "keep-alive",
            # "Connection": "close",
        }

        self.params = {
            "lb_a": "hp",
            "lb_b": "mh",
            "lb_c": "mh",
            "tp": "tp1",
            # "q": "我"
            "q": None
        }
        self.cookies = {
            "ASPSESSIONIDQQBTQBSA": "AIFKNJKBDMDCNKHIIAEFDLLD",
            "ASPSESSIONIDQQCQSATA": "BKEMOFHCOMBMDNCDLHIINGHD",
            "ASPSESSIONIDQQCSTBSA": "EGIHAKKBKKPDOFOKBGPODFHK",
            "ASPSESSIONIDQQDQTATA": "PPLMDDDBKICEEJANAPIECGHG",
            "ASPSESSIONIDQQDRRATA": "LDKKPNNAKMPDPFEGIIANBLJL",
            "ASPSESSIONIDQSCQSATA": "NPDPCONAILAPOLMFPFLPJKMH",
            "ASPSESSIONIDSQBRSATA": "DOFGMEICOILOJHJENECEOGDA",
            "ASPSESSIONIDSQCRSASB": "PKJIAMNBGNCJMONFLNOEHJPD",
            "ASPSESSIONIDSSDQTDQB": "MDBILFHCCKBIDADCMPHLLBLC",
            "CNZZDATA524192": "cnzz_eid=551846853-1465193430-&ntime=1469453481",
            "Hm_lpvt_57315eba0396d9939adbd0045addeae1": "1469451059",
            "Hm_lvt_57315eba0396d9939adbd0045addeae1": "1467616616,1469451059",
            "cxls": "äºº|ä¼¤|ã¤|å¤|ïª¨|ç´|æ£|æ|ä¸|ä¸¨|ä¸¯|ç¶|ä¸°|ç|ç|çæ´»|ð¢ª|æ¹|æ|åª|æ¤|é|å|é|é¼|å»|ð¯¨|é½",
            "cxls": "ä¸¨|ä¸¯|äºº|ç¶|ä¸°|ä¼¤|ä¸|ç|ç|çæ´»|ð¢ª|æ¹|æ|åª|æ¤|é|å|é|é¼|å»|ð¯¨|é½",
            "lb_a": "hp",
            "lb_b": "mh",
            "lb_c": "mh",
            "tp": "tp1",
        }

    def get_url(self, word):
        self.params = {
            "lb_a": "hp",
            "lb_b": "mh",
            "lb_c": "mh",
            "tp": "tp1",
            # "q": "我"
            "q": word
        }
        requests.adapters.DEFAULT_RETRIES = 50
        s = requests.session()
        s.keep_alive = False
        time.sleep(2)
        response = requests.post("http://www.zdic.net/sousuo/", data=self.params,
                                 headers=self.headers, cookies=self.cookies)

        return response.url


if __name__ == "__main__":
    handian = Handian()
    print(handian.get_url("我"))
    print(handian.get_url("你"))
    print(handian.get_url("烔"))

