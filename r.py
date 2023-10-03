import random

def Print_array(matrix,rows,columns):
  for i in range(0,rows):
    for j in range(0,columns):
      print(matrix[i][j],end=" ")
    print("\n")
    
    
def Min_hash(input_Dict):
  No_of_random_shuffles = 3
  Keys_list = list(input_Dict.keys())

  col = len(input_Dict[Keys_list[0]])
  row = No_of_random_shuffles
  arr = [[0 for j in range(col)] for i in range(row)]

  no_of_docs=col
  similarity = [[0 for j in range(no_of_docs)] for i in range(no_of_docs)]

  for i in range(0,No_of_random_shuffles):
    Random_order = random.sample(Keys_list,len(Keys_list))
    print(Random_order)
    for j in range(0,col):
      count=1
      for k in Random_order:
        if input_Dict[k][j] == 1:
          break
        count+=1

      arr[i][j] = count

  print("The shuffled matrix is")

  Print_array(arr,row,col)

  for i in range(0,no_of_docs):
    for j in range(0,no_of_docs):
      if i==j:
        similarity[i][j] = 1
      else:
        count=0
        for k in range(0,row):
          if(arr[k][i]==arr[k][j]):
            count+=1

        similarity[i][j] = count/row

  print("The similarity matrix is ")

  Print_array(similarity,no_of_docs,no_of_docs)
  
def documents_to_shringles(Document):
  k=3
  shringle_set=[]

  for i in Document.keys():
    sentence = Document[i]
    list_of_words = sentence.split()

    #print(list_of_words)
    for j in range(0,len(list_of_words)-(k-1)):
      shringle=""
      for l in range(j,j+k):
         shringle += list_of_words[l]
         if not l==(j+k-1):
          shringle +=" "
      #print(shringle)
      if not shringle in shringle_set:
        shringle_set.append(shringle)

  return shringle_set


def shringle_set_to_dictionary(shringle_set,Document):
  input_Dictionary={}
  ch = 'A'
  n = len(Document)
  for i in shringle_set:
    value=[0 for j in range(n)]
    index=0
    for j in Document.keys():
      if i in Document[j]:
        value[index]=1
      else:
        value[index]=0
      index = index+1
    input_Dictionary[ch] = value
    ch = chr(ord(ch) + 1)

  print(input_Dictionary)
  return input_Dictionary


Document = {"document1":"He moved from London Ontario to London England",
               "document2":"He moved from London England to London Ontario",
               "document3":"He moved from England to London Ontario"}

shringle_set = documents_to_shringles(Document)
input_dictionary = shringle_set_to_dictionary(shringle_set,Document)
Min_hash(input_dictionary)

######################

input_Dict = {'A':[1,0,1,0],'B':[1,0,0,1],'C':[0,1,0,1],'D':[0,1,0,1],'E':[0,1,0,1],'F':[1,0,1,0],'G':[1,0,1,0]}

Min_hash(input_Dict)
