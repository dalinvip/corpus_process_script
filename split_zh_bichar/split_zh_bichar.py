# @Author : bamtercelboo
# @Datetime : 2018/5/7 21:25
# @File : split_zh_bichar.py
# @Last Modify Time : 2018/5/7 21:25
# @Contact : bamtercelboo@{gmail.com, 163.com}

"""
    FILE :  split_zh_bichar.py
    FUNCTION : None
    EXAMPLE:
        Source:
        中国国庆假期
        TO:
        -NULL_中 中国 国庆 庆假 假期 期-NULL-
"""

import sys
import os
from optparse import OptionParser


class Bichar(object):
    def __init__(self, in_file, out_file):
        self.pad = "-NULL-"
        self.infile = in_file
        self.outfile = out_file
        self.line_list = []
        self.out_list = []
        self.count_line = 0
        self.read(self.infile)
        self.split_bichar(self.line_list)
        self.write(self.out_list, self.outfile)

    def read(self, input_file=None):
        print("read file from {}".format(input_file))
        with open(input_file, encoding="UTF-8") as f:
            for line in f:
                if line == "\n":
                    continue
                line = line.strip()
                self.count_line += 1
                self.line_list.append(line)
                # print(line)
        print("Read Finished, all {} lines.".format(self.count_line))

    def write(self, out_list=None, out_file=None):
        print("writing......")
        if os.path.exists(out_file):
            os.remove(out_file)
        file = open(out_file, encoding="UTF-8", mode="w")
        now_line = 0
        count_line = len(out_list)
        for line in out_list:
            now_line += 1
            if now_line % 5000 == 0:
                sys.stdout.write("\rhandling with the {} line, all {} lines.".format(now_line, count_line))
            file.writelines(line + "\n")
        sys.stdout.write("\rhandling with the {} line, all {} lines.".format(now_line, count_line))
        print("\nHandle Finished.")

    def is_chinese(self, uchar):
        """判断一个unicode是否是汉字"""
        if (uchar >= u'\u4e00') and (uchar <= u'\u9fa5'):
            return True
        else:
            return False

    def split_bichar(self, line_list):
        print("split bichar feature......")
        for line in line_list:
            line = list(line)
            if len(line) == 0:
                continue
            line.insert(0, self.pad)
            line.insert(len(line), self.pad)
            temp_list = []
            for i in range(len(line) - 1):
                temp_list.append("".join((line[i:i+2])))
            temp_line = " ".join(temp_list)
            self.out_list.append(temp_line)
        print("split bichar feature finished.")


if __name__ == "__main__":
    print("split chinese bichar feature")
    input = "./Data/giga_small.txt"
    output = "./Data/giga_small_out.txt"
    Bichar(in_file=input, out_file=output)

    # parser = OptionParser()
    # parser.add_option("--input", dest="input", help="input file")
    # parser.add_option("--output", dest="output", help="output file")
    # (options, args) = parser.parse_args()
    # Bichar(in_file=options.input, out_file=options.output)




