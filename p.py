A=[[0,1,0],
   [1,0,1],
   [0,1,0]]
N = len(A)
alpha = 0.5


def calculateP(A):
  # step 1: If a row has no 1, then add 1/N to all entry in row
  for i in range(len(A)):
    if 1 not in A[i]:
      A[i] = [1/N]*len(A[i])

  # step 2: Divide each 1 in a row by no. of ones in row
  for i in range(len(A)):
    cnt = 0
    for j in range(len(A[i])):
      if A[i][j]==1:
        cnt+=1
    if cnt>0:
      A[i] = [ele/cnt for ele in A[i]]

  # step 3: Multiply each entry by (1-aplha)
  one_minus_alpha = 1-alpha
  for i in range(len(A)):
    A[i] = [ele*one_minus_alpha for ele in A[i]]

  # step 4: Add alpha/N to each entry
  alpha_by_N = alpha/N
  for i in range(len(A)):
    A[i] = [ele+alpha_by_N for ele in A[i]]

  return A


def matrixMultiply(x,P):
  res = []
  for j in range(len(P[0])):
    sums = 0
    for i in range(len(P)):
      sums+=(P[i][j]*x[i])
    res.append(sums)
  return res


def findDiff(x1,x2):
  val = 0
  for ele1,ele2 in zip(x1,x2):
    val+=abs(ele1-ele2)
  return val


P = calculateP(A.copy())
x = [1,0,0]
while(True):
  newX = [round(ele,2) for ele in matrixMultiply(x.copy(),P)]
  if(findDiff(x,newX)<0.01):
    break
  x = newX.copy()
print(x)
