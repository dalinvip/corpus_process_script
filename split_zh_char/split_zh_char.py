#encoding:utf-8
# @Author : bamtercelboo
# @Datetime : 2018/3/17 8:50
# @File : split_zh_char.py
# @Last Modify Time : 2018/3/17 8:50
# @Contact : bamtercelboo@{gmail.com, 163.com}

"""
    FILE :  split_zh_char.py
    FUNCTION : None
    EXAMPLE:
        Source:
        中国国庆假期香江将涌入人潮
        TO:
        中 国 国 庆 假 期 香 江 将 涌 入 人 潮
"""

import sys
import os
from optparse import OptionParser


def split_zh_char(dict=None, count_line=None, out_file=None):
    print("splitting chinese char")
    split_list = []
    now_line = 0
    for line in dict:
        now_line += 1
        sys.stdout.write("\rhandling with the {} line, all {} lines.".format(now_line, count_line))
        new_line = ""
        for char in line:
            char += " "
            new_line += char
        split_list.append(new_line[:-1])
    print("\nHandle Finished.")
    write(split_list, out_file)
    return split_list


def read(input_file=None):
    print("read file from {}".format(input_file))
    line_list = []
    count_line = 0
    with open(input_file, encoding="UTF-8") as f:
        for line in f:
            if line == "\n":
                continue
            count_line += 1
            line_list.append(line)
    print("Read Finished, all {} lines.".format(count_line))
    return line_list, count_line


def write(dict=None, out_file=None):
    print("writing......")
    if os.path.exists(out_file):
        os.remove(out_file)
    file = open(out_file, encoding="UTF-8", mode="w")
    now_line = 0
    count_line = len(dict)
    for line in dict:
        now_line += 1
        sys.stdout.write("\rhandling with the {} line, all {} lines.".format(now_line, count_line))
        file.writelines(line)
    print("\nHandle Finished.")


if __name__ == "__main__":

    # input_file = "./Data/giga_small.txt"
    # out_file = "./Data/giga_small_out.txt"
    # line_list, count_line = read(input_file=input_file)
    # split_list = split_zh_char(dict=line_list, count_line=count_line, out_file=out_file)

    parser = OptionParser()
    parser.add_option("--input", dest="input", help="input file")
    parser.add_option("--output", dest="output", help="output file")
    (options, args) = parser.parse_args()
    line_list, count_line = read(input_file=options.input)
    split_list = split_zh_char(dict=line_list, count_line=count_line, out_file=options.output)



