import itertools
A = int(input())
B = int(input())
C = int(input())
X = int(input())

def make_list(alphabet):
  l_alphabet = []
  for i in range(0,alphabet+1):
    l_alphabet.append(i)
  return l_alphabet

def make_pattern(A_list, B_list, C_list):
  l_pattern = list(itertools.product(A_list, B_list, C_list))
  return l_pattern

def X_count(l_pattern):
  count = 0
  for i in l_pattern:
    X_tmp = i[0]*500 + i[1]*100 + i[2]*50
    if X == X_tmp:
      count+=1
  return count

A_list = make_list(A)
B_list = make_list(B)
C_list = make_list(C)

l_pattern = make_pattern(A_list, B_list, C_list)
result = X_count(l_pattern)
print(result)