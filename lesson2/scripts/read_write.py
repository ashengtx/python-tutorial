
with open("../txt/apple.txt", 'r') as f:
    print("file name: ", f.name)
    print("access mode: ", f.mode)
    print("closed or not:", f.closed)
    chars = []
    for line in f:
        if len(line) > 1:
            chars.append(line.strip()) # str.strip() 去掉首尾空白
        else:
            chars.append(' ')
    print(chars)
    print(''.join(chars)) # 'delimit'.join(alist)
    with open("../txt/output.txt", 'w') as fout:
        #fout.write(''.join(chars)) # 末尾不加换行
        print(''.join(chars), file=fout) # 末尾会加换行

with open("../txt/output.txt", "r+") as fo:
    str = fo.read(10);
    print("Read String is : ", str)

    # Check current position
    position = fo.tell();
    print("Current file position : ", position)

    # Reposition pointer at the beginning once again
    #fo.seek(offset, from); from = 0表示定位到文件开头，1表示当前位置，2表示文件末尾
    position = fo.seek(10, 0);
    #position = fo.seek(0, 1);
    #position = fo.seek(0, 2);
    str = fo.read(10);
    print("Again read String is : ", str)


