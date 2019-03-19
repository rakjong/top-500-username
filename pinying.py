# -*- coding: utf-8 -*-

from pypinyin import pinyin, lazy_pinyin

def rename():
    f1 = open('C:\\Users\\Yisihe\\Desktop\\hanzi.txt','r+')
    for line in f1:
        pin1 = lazy_pinyin(f1)
        pin2 = []
        for i in range(len(pin1)):
            pin2.append(str(pin1[i]))
            pinyin = ''.join(pin2)
            #print(pinyin)
            f = open('result.txt','w+')
            f.write(pinyin+'\n')
            f.close
    f1.close()

rename()
