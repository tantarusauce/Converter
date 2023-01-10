path = 'test.py'

import os
print(os.getcwd())

class processing():

  def __init__(self, out):
    self.string = out.replace(' ', '') #クラスを呼び出すときにoutに１行ずつ代入され，それがself.strに代入される&' 'を''に置換

  def assignment(self):
    i00dx = self.string.find('+=')
    i01dx = self.string.find('-=')
    i02dx = self.string.find('*=')
    i03dx = self.string.find('/=')
    i04dx = self.string.find('%=')
    i99dx = self.string.find('=')
    if(i00dx != -1):
      outemp = self.string[:i00dx]
      outp = outemp + ' += ' + self.string[i00dx + 1 :]
    elif(i01dx != -1):
      outemp = self.string[:i01dx]
      outp = outemp + ' -= ' + self.string[i01dx + 1 :]
    elif(i02dx != -1):
      outemp = self.string[:i02dx]
      outp = outemp + ' *= ' + self.string[i02dx + 1 :]
    elif(i03dx != -1):
      outemp = self.string[:i03dx]
      outp = outemp + ' /= ' + self.string[i03dx + 1 :]
    elif(i04dx != -1):
      outemp = self.string[:i04dx]
      outp = outemp + ' %= ' + self.string[i04dx + 1 :]
    elif(i99dx != -1):
      outemp = self.string[:i99dx]
      if(outemp not in variable):
        #初めての変数使用
        typ = "long long double "
      outp = typ + outemp + ' = ' + self.string[i99dx + 1 :]
    outpu = outp.replace('\n', '')
    return outpu
  
  def equ(self, str):
    i00dx = self.string.find('+')
    i01dx = self.string.find('-')
    i02dx = self.string.find('*')
    i03dx = self.string.find('/')
    i04dx = self.string.find('%')
    i05dx = self.string.find('**')
    i06dx = self.string.find('//')
    

class other():
  def __init__(self):
    os.chdir('./プログラムコンバータ/programs')#programsフォルダへ移動
  
  def read(self, p):
    leng = 0
    f = open(p, 'r', encoding='UTF-8')#指定されたpythonファイルを開く
    r = f.readlines()
    for i in r:
      leng += 1 #行数計算
    f.close()#pythonファイルを閉じる
    return(r, leng)
  
  def magicalword(self):
    word = ['include <stdio.h>', '']
    mol = 2 #現在の出力行数
    mil = 1 #import行数
    return(word,mol,mil)

l = 0 #生データの全体の行数

ret1 = {}

variable = []#変数
output = []#出力リスト
outemp = []#出力テンポラリ

o = other()
ret1 = o.read(path)
raw = ret1[0]
l = ret1[1]
ret2 = o.magicalword()
output = ret2[0]
ol = ret2[1]
il =ret2[2]

#---main---

for i in range(0, l):
  asginstance = processing(raw[i])
  if ('=' in raw[i]):
    output.append(asginstance.assignment())
    ol += 1



for i in range(0, ol):
  print(output[i])