# @Author : bamtercelboo
# @Datetime : 2018/3/28 14:07
# @File : merge_file.py
# @Last Modify Time : 2018/3/28 14:07
# @Contact : bamtercelboo@{gmail.com, 163.com}

"""
    FILE :  merge_file.py
    FUNCTION : None
"""

import os
import sys


class Merge_file(object):
    def __init__(self, file1, file2):
        self.dictionary = {}
        self.file_merge = "./merge.txt"
        self.file1 = file1
        self.file2 = file2
        self.read_dictionary(self.file1)
        self.read_dictionary(self.file2)
        self.write_dictionary(self.file_merge, self.dictionary)

    def read_dictionary(self, path=None):
        with open(path, encoding="UTF-8") as f:
            for line in f:
                line = line.strip("\n")
                line = line.split(" ")
                self.dictionary[line[0]] = line[1:]
        f.close()

    def write_dictionary(self, out_file=None, write_dict=None):
        print("save to {}".format(out_file))
        if os.path.exists(out_file):
            os.remove(out_file)
        file = open(out_file, encoding="UTF-8", mode="w")
        for key, value in write_dict.items():
            # print("key {}, value {}".format(key, str(value)))
            v_str = self.dict_value2str(value)
            file.write(key + " " + v_str[1:] + "\n")
        file.close()
        print("Save Finished.")

    def dict_value2str(self, v_list=None):
        if v_list is None:
            return ""
        if isinstance(v_list, list) is False:
            return ""
        v_str = ""
        for v in v_list:
            v_str += (" " + v)
        return v_str


if __name__ == "__main__":
    print("merge file")
    file1 = "./Data/giga_stoke_dict.Found"
    file2 = "./Data/giga_stoke_dict.TempFound"
    Merge_file(file1, file2)