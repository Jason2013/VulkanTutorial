# coding=utf-8

import glob

a = glob.glob("*.cpp")

print(a)

for i in range(len(a)-1):
    print(i, a[i], a[i+1])
    with open("diff_{}_{}.bat".format(a[i], a[i+1]), "w") as f:
        f.write("\"C:\\Program Files\\KDiff3\\kdiff3.exe\" --cs \"ShowWhiteSpaceCharacters=0\" {} {}\n".format(a[i], a[i+1]))
