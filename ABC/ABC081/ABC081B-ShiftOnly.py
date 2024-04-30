num = int(input())
line = input().split()
count = 0
num_list = [int(i) for i in line]
tmp_list = []
def even_check(check_list):
  for i in check_list:
    if (i % 2) == 1:
      return False
  return True
 
 
while True:
  bool_result = even_check(num_list)
  if bool_result:
    tmp_list = list(map(lambda x: x//2 ,num_list))
    count+=1
    num_list = tmp_list
  else:
    break
 
print(count)