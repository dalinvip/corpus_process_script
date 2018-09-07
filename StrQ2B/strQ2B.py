# @Author : bamtercelboo
# @Datetime : 2018/9/7 16:14
# @File : strQ2B.py
# @Last Modify Time : 2018/9/7 16:14
# @Contact : bamtercelboo@{gmail.com, 163.com}

"""
    FILE :  strQ2B.py
    FUNCTION : None
"""
import os
import sys
from optparse import OptionParser
from idna import unichr


class StrQ2B(object):
    """
        全角转换半角
    """
    def __init__(self, in_path, out_path):
        self.in_path = in_path
        self.out_path = out_path
        self.half_corpus = self.process(path=self.in_path)
        self.write2file(corpus=self.half_corpus, path=self.out_path)

    def process(self, path):
        """
        :param path:
        :return:
        """
        print("Processing......")
        half_corpus = []
        with open(path, encoding="UTF-8") as f:
            for line in f.readlines():
                line = line.strip()
                line = self.strQ2B(line)
                half_corpus.append(line)
        return half_corpus

    @staticmethod
    def strQ2B(ustring):
        """全角转半角"""
        rstring = ""
        for uchar in ustring:
            inside_code = ord(uchar)
            if inside_code == 12288:  # 全角空格直接转换
                inside_code = 32
            elif (inside_code >= 65281) and (inside_code <= 65374):  # 全角字符（除空格）根据关系转化
                inside_code -= 65248

            rstring += unichr(inside_code)
        return rstring

    @staticmethod
    def write2file(corpus, path):
        """
        :param corpus:
        :param path:
        :return:
        """
        print("Writing to File......")
        if os.path.exists(path):
            os.remove(path)
        file = open(path, encoding="UTF-8", mode="w")
        for line in corpus:
            file.write(line + "\n")
        file.close()
        print("Finished.")


if __name__ == "__main__":
    # StrQ2B(in_path=in_path, out_path=out_path)
    parser = OptionParser()
    parser.add_option("--input", dest="input", help="input file")
    parser.add_option("--output", dest="output", help="output file")
    (options, args) = parser.parse_args()

    input_file = options.input
    output_file = options.output
    try:
        StrQ2B(in_path=input_file, out_path=output_file)
    except Exception as err:
        print(err)
    print("All Finished.")
