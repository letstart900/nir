Mat = [[1,0,0,1],
       [0,0,1,0],
       [0,1,0,1],
       [1,0,1,1],
       [0,0,1,0]]


def hash1(val):
  return (val+1)%5

def hash2(val):
  return (3*val + 1)%5


def minHashing(mat):
  ans = [[float('inf') for i in range(len(mat[0]))] for j in range(2)]
  # print(ans)
  for i in range(len(mat)):
    h1 = hash1(i)
    h2 = hash2(i)
    for j in range(len(mat[0])):
      if(mat[i][j]==1):
        ans[0][j] = min(ans[0][j],h1)
        ans[1][j] = min(ans[1][j],h2)
  return ans

print("ans1 :")
ans1 = minHashing(Mat)
print(ans1)

#######################################

import string

arr = ["He moved from London, Ontario, to London, England.","He moved from London, England, to London, Ontario","He moved from England to London, Ontario"]
def removePunctuation(arr):
  for i in range(len(arr)):
    arr[i] = arr[i].translate(str.maketrans('', '', string.punctuation))
removePunctuation(arr)
print(arr)

shringle_size = 4
shringle_set = set()
for i in range(len(arr)):
  words = arr[i].split()
  for j in range(len(words)-shringle_size + 1):
    shringle_set.add(" ".join(words[j:j+shringle_size]))
print(shringle_set)


mat = []
for shringle in shringle_set:
  row = []
  for doc in arr:
    if shringle in doc:
      row.append(1)
    else:
      row.append(0)
  mat.append(row)
print(mat)

print("ans2: ")
ans2 = minHashing(mat)
print(ans2)
