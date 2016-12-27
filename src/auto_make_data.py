#-*- encoding: utf-8 -*-

import sys
import subprocess
import re

def makefilelist():
    #今いる、ディレクトリ内のファイル名を取り出す
    ret = subprocess.getoutput('ls')
    #改行文字で分けてリストを作る
    filelist = ret.split('\n')
    #リストの中から、拡張子が.woutのみを取り出し、リストに格納
    namelist = []
    for filename in filelist:
        if mymatch('\.wout$', filename):
            namelist.append(filename)
    #リストを返す
    print(len(namelist))
    return namelist


def mymacth(pattern, text):
    repat = re.compile(pattern)
    result = repat.search(text)
    if result:
        return True
    else:
        return False


def list2file(namelist):
    fname = input('Type file name >>> ')
    fout = open('fname', 'wt')
    for name in namelist:
        print(name, file=fout)

    fout.close()


def result():
    #ファイルからファイル名を取り出し、リストに格納、クローズ
    fname = input('Type file name >>> ')
    fout1 = open('fname', 'rt')
    namelist = []
    for line in fout:
        namelist.append(line)

    fout1.close()
    #以降をすべてのファイル名に対して、繰り返す
    for name in namelist:
        #bptest.parを読み込む
        fout2 = open('bptest.par', 'rw')
        #Weight for init の行を書き換え
        text = ''
        for line in fout2:
            if mymatch(r'Weight for Init:', line)
                text += 'Weight for Init: ' + name + '\n'
            else:
                text += line
        
        fout2.write(text)
        #テストデータに対する実行
        result1 = 
        result1 = subprocess.getoutput('./a.out')
        #結果をファイルに(result_test.txt or result_test.csv)
        #Datafile for Test　の行を書き換え
        #学習データに対する実行
        #結果をファイルに(result_learn.txt or result_learn.csv)
        #Datafile for Testの行を再書き換え
        #クローズ
        fout2.close()


#本体
filelist = makefilelist()
list2file(filelist)




