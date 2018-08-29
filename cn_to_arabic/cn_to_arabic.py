# @Author : bamtercelboo
# @Datetime : 2018/8/29 9:02
# @File : cn_to_arabic.py
# @Last Modify Time : 2018/8/29 9:02
# @Contact : bamtercelboo@{gmail.com, 163.com}

"""
    FILE :  cn_to_arabic.py
    FUNCTION : None
"""


class Chinese_to_arabic(object):
    """
    Chinese_to_arabic
    """
    def __init__(self):
        # constants for chinese_to_arabic
        self.CN_NUM = {
            '〇': 0, '一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9, '零': 0,
            '壹': 1, '贰': 2, '叁': 3, '肆': 4, '伍': 5, '陆': 6, '柒': 7, '捌': 8, '玖': 9, '貮': 2, '两': 2,
        }

        self.CN_UNIT = {
            '十': 10,
            '拾': 10,
            '百': 100,
            '佰': 100,
            '千': 1000,
            '仟': 1000,
            '万': 10000,
            '萬': 10000,
            '亿': 100000000,
            '億': 100000000,
            '兆': 1000000000000,
        }

    def chinese_to_arabic(self, cn: str) -> int:
        """
        :param cn:
        :return:
        """
        unit = 0  # current
        ldig = []  # digest
        for cndig in reversed(cn):
            if cndig in self.CN_UNIT:
                unit = self.CN_UNIT.get(cndig)
                if unit == 10000 or unit == 100000000:
                    ldig.append(unit)
                    unit = 1
            else:
                dig = self.CN_NUM.get(cndig)
                if unit:
                    dig *= unit
                    unit = 0
                ldig.append(dig)
        if unit == 10:
            ldig.append(10)
        val, tmp = 0, 0
        for x in reversed(ldig):
            if x == 10000 or x == 100000000:
                val += tmp * x
                tmp = 0
            else:
                tmp += x
        val += tmp
        return val


if __name__ == "__main__":
    c2a = Chinese_to_arabic()
    s = "一亿三千万"
    s = "一万五千六百三十八"
    val = c2a.chinese_to_arabic(s)
    print(val)
