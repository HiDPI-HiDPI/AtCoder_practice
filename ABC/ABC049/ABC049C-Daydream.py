# ネットを参考にした記憶あり
S = list(map(str, input().split()))[0]
l_T = ["dream", "dreamer", "erase", "eraser"]
T = ""

while True:
  for i in l_T:
    if S.endswith(i):
      S = S[:-len(i)]
      break
  else:
    print("NO")
    break
  if not S:
    print("YES")
    break
