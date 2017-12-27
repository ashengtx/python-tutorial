import re


if __name__ == '__main__':

    # case 1

    s = 'hi, how old are you?'

    res = re.findall('hi', s)
    print("case 1", res)

    # case 2
    s = 'hi him history high'

    res = re.findall('hi', s)
    print("case 2", res)

    # case 3
    s = 'hi him history high'

    res = re.findall('\bhi\b', s)
    print("case 3", res)

    # case 4
    s = 'hi him history high'

    res = re.findall(r'\bhi\b', s)
    print("case 4", res)

    # 字符串前面加个r表示这里面的字符是非转义字符，可以从下面的例子感受一下
    print("without r prefix:", 'abd\tbad')
    print("with r prefix:", r'abd\tbad')

    # case 5 

    s = 'tel: 010-88881234, 0591-22223456'
    res = re.findall(r'0\d\d-\d\d\d\d\d\d\d\d', s)
    print("case 5-1", res)
    res = re.findall(r'0\d{2}-\d{8}', s)
    print("case 5-2", res)

    # case 6 字符转义

    s = 'c:\windows'
    res = re.findall(r'\w:\\w+', s)
    print("case 6-1", res)
    res = re.findall(r'\w:\\\w+', s)
    print("case 6-2", res)

    # case 7

    s = '像(010)88886666，或022-22334455，或02912345678等。'
    res = re.findall(r'0\d{2}-\d{8}', s)
    print("case 7-1", res)
    res = re.findall(r'\(?0\d{2}[)-]?\d{8}', s)
    print("case 7-2", res)

