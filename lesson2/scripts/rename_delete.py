import os

filename = "../txt/testrename.txt"

if not os.path.exists(filename):
    open(filename, 'w')

# 下面这两行一行一行来执行

#os.rename(filename, "../txt/testrename1.txt")
#os.remove("../txt/testrename1.txt")
