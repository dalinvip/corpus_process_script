# @Author : bamtercelboo
# @Datetime : 2018/5/10 16:20
# @File : wiki_process.py
# @Last Modify Time : 2018/5/10 16:20
# @Contact : bamtercelboo@{gmail.com, 163.com}

"""
    FILE :  wiki_process.py
    FUNCTION : None
    REFERENCE: https://github.com/AimeeLee77/wiki_zh_word2vec/blob/master/1_process.py
"""

import logging
import os.path
import sys

from gensim.corpora import WikiCorpus

if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))

    if len(sys.argv) < 3:
        print(globals()['__doc__'] % locals())
        sys.exit(1)

    inp, outp = sys.argv[1:3]
    space = " "
    i = 0

    output = open(outp, 'w')
    wiki = WikiCorpus(inp, lemmatize=False, dictionary=[])
    for text in wiki.get_texts():
        output.write(space.join(text) + "\n")
        i = i + 1
        if (i % 10000 == 0):
            logger.info("Saved " + str(i) + " articles.")

    output.close()
    logger.info("Finished Saved " + str(i) + " articles.")




