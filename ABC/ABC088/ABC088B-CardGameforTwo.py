N = list(map(int, input().split()))[0]
l_AB = list(map(int, input().split()))
l_AB.sort(reverse=True)
num_A = 0
num_B = 0

for i in range(N):
  if i % 2 == 0:
    num_A += l_AB[i]
  else:
    num_B += l_AB[i]

print(num_A - num_B)