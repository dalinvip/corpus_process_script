# @Author : bamtercelboo
# @Datetime : 2018/8/11 14:20
# @File : convert_tag.py
# @Last Modify Time : 2018/8/11 14:20
# @Contact : bamtercelboo@{gmail.com, 163.com}

"""
    FILE :  convert_tag.py
    BIO2BMESO : BIO ---> BMESO
    文件的末尾必须有两个空行
    run: python -u convert_tag.py --input in.txt --output out.txt
"""

import os
import time
from optparse import OptionParser


class TagConvert(object):
    def __init__(self, infile, outfile, tag):
        self.infile = infile
        self.outfile = outfile
        self.tag = tag
        if tag.upper() == "BMESO":
            self.BIO2BMESO(self.infile, self.outfile)
        elif tag.upper() == "BIESO":
            self.BIO2BIESO(self.infile, self.outfile)

    def BIO2BIESO(self, input_file, output_file):
        print("Convert BIO -> BIESO for file:", input_file)
        with open(input_file, encoding="UTF-8") as in_file:
            fins = in_file.readlines()
        if os.path.exists(output_file):
            os.remove(output_file)
        fout = open(output_file, mode="w", encoding="UTF-8")
        words = []
        words_en = []
        labels = []
        for line in fins:
            # print(line)
            if len(line) < 3:
                sent_len = len(words)
                for idx in range(sent_len):
                    print(words)
                    print(labels)
                    if "-" not in labels[idx]:
                        fout.write(words[idx] + "\t" + labels[idx] + "\n")
                    else:
                        label_type = "-".join(labels[idx].split("-")[1:])
                        # print(label_type)
                        if "B-" in labels[idx]:
                            if (idx == sent_len - 1) or ("I-" not in labels[idx + 1]):
                                fout.write(words[idx] + "\tS-" + label_type + "\n")
                            else:
                                fout.write(words[idx] + "\tB-" + label_type + "\n")
                        elif "I-" in labels[idx]:
                            if (idx == sent_len - 1) or ("I-" not in labels[idx + 1]):
                                fout.write(words[idx] + "\tE-" + label_type + "\n")
                            else:
                                fout.write(words[idx] + "\tI-" + label_type + "\n")
                fout.write('\n')
                words = []
                words_en = []
                labels = []
            else:
                pair = line.strip('\n').split()
                # words.append(pair[0])
                words.append("\t".join(pair[0:2]))
                labels.append(pair[-1].upper())
        fout.close()
        print("BIESO file generated:", output_file)

    def BIO2BMESO(self, input_file, output_file):
        print("Convert BIO -> BMESO for file:", input_file)
        with open(input_file, encoding="UTF-8") as in_file:
            fins = in_file.readlines()
        if os.path.exists(output_file):
            os.remove(output_file)
        fout = open(output_file, mode="w", encoding="UTF-8")
        words = []
        words_en = []
        labels = []
        for line in fins:
            # print(line)
            if len(line) < 3:
                sent_len = len(words)
                for idx in range(sent_len):
                    # print(words)
                    # print(labels)
                    if "-" not in labels[idx]:
                        fout.write(words[idx] + "\t" + labels[idx] + "\n")
                    else:
                        label_type = "-".join(labels[idx].split("-")[1:])
                        # print(label_type)
                        if "B-" in labels[idx]:
                            if (idx == sent_len - 1) or ("I-" not in labels[idx + 1]):
                                fout.write(words[idx] + "\tS-" + label_type + "\n")
                            else:
                                fout.write(words[idx] + "\tB-" + label_type + "\n")
                        elif "I-" in labels[idx]:
                            if (idx == sent_len - 1) or ("I-" not in labels[idx + 1]):
                                fout.write(words[idx] + "\tE-" + label_type + "\n")
                            else:
                                fout.write(words[idx] + "\tM-" + label_type + "\n")
                fout.write('\n')
                words = []
                words_en = []
                labels = []
            else:
                pair = line.strip('\n').split()
                # words.append(pair[0])
                words.append("\t".join(pair[0:2]))
                labels.append(pair[-1].upper())
        fout.close()
        print("BMESO file generated:", output_file)


if __name__ == "__main__":
    # print("convert tag......")
    # input = "./Data/srl/srl.sample.conll"
    # output = "./Data/srl/srl.sample.conll.bmeso"
    # TagConvert(infile=input, outfile=output, tag="bmeso")

    parser = OptionParser()
    parser.add_option("--input", dest="input", help="input file")
    parser.add_option("--output", dest="output", default="", help="output file")
    parser.add_option("--tag", dest="converted_tag", default="bmeso", help="output file")

    (options, args) = parser.parse_args()

    input = options.input
    output = options.output
    tag = options.converted_tag

    try:
        start_time = time.time()
        TagConvert(infile=input, outfile=output, tag=tag)
        print("All Finished.")
        end_time = time.time()
        print("Cost Time is {:.4f}.".format(end_time - start_time))
    except Exception as err:
        print("Tag selection from [BMESO, BIESO]")
        print(err)









