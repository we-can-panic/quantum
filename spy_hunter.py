from blueqat import Circuit as C

def spy_hunter(spy):
  # C[4] = [a_val, a_had, b_had, res]
    # a_val, a_had, b_hadは0か1の定数。resのみを送受信する
    # a_hadとb_hadは「暗号のキー」。合致しているときにだけ解読可能
    #  -> a_hadとb_hadが合致していたら、a_valとresが合致(不一致の時は情報が解読できない)
  Alice = C(4).h[:2].m[:2].cx[0,3].ch[1,3]

  if spy:
    connection = Alice.m[3].h[3] # 観測したのち、偽装のためhをかける
    Bob = connection.h[2].m[2].ch[2,3]
  else:
    connection = Alice
    Bob = connection.h[2].m[2].ch[2,3]

  # 途中でresを観測してしまうと、a_hadとb_hadが合致していても、a_valとresが合致しなくなる
  # -> spyの有無が50%の確率で判明(10qbitで1023/1024の確率で判明)
  result = Bob.m[:].run(100)
  return result
  return sorted(list(result.keys()))

if __name__ == '__main__':
  print("T: ", spy_hunter(spy=True))
  print("F: ", spy_hunter(spy=False))
  # Fのときは、'0001', '0111', '1000', '1110'
  # (a_hadとb_hadが一致していて、a_valとresが一致しないパターン)が観測されない
  # Tのとき、上記が25%の確率で観測される
  # (a_had=b_had、かつ、a_valと(ランダムな)resが一致しない確率)
  # 「スパイが暗号を解読でき、バレない確率」=「Bobが暗号を解読できる確率/4」
