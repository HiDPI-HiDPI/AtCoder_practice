line = list(map(int, input().split()))
N = line[0]
A = line[1]
B = line[2]
l_Nsum = []
count = 0
result = 0

for i in range(0, N+1):
  l_tmp = list(str(i))
  l_Nsum.append( sum(map(int, l_tmp)) )
 
for i in l_Nsum:
  if A <= i and i <= B:
    result+=count
  count+=1
 
print(result)