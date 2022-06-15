"""# How Crazy RNG It Was Calculator"""

import math as m

print("m回中n回x%を引き当てた時の確率を計算します。")
print()

def test():
  print("Success")
def a():
  print("ばーか")
def gnn():
  print("ぐぬぬ")
def tryfloat(x):
  try:
    float(x)
  except ValueError:
    return False
  else:
    return True



tries = input("m:試行回数を入力してください : ")
if tries.isdecimal() == True:
  tries = int(tries)
  if tries > 0:
    wins = input("n:当たりの回数を入力してください : ")
    if wins.isdecimal() == True:
      wins = int(wins)
      if wins >= 0:
        if wins <= tries:
          odds = input("x:当たりの確率を入力してください[%] : ")
          if tryfloat(odds) == True:
            odds = float(odds)
            if odds > 0:
              odds = odds / 100
              answer = m.factorial(tries) / m.factorial(tries - wins) / m.factorial(wins) * (odds ** wins) * ((1 - odds) ** (tries - wins))
              print(str(round(answer * 100 , 3)) + "%です")
            else:
              a()
          else:
            a()
        else:
          gnn()
      else:
        a()
    else:
      a()
  else:
    a()
else:
  a()