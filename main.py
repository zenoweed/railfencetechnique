plainText = 'HELLO THERE'
n= len(plainText)
i = 0
a = 0
b = 0
e1 = []
e2 = []

def rail(arr):
  while i != len(plainText):
    if i%2 == 0:
      print (e1[a])
      e1[a] = arr[i]
      a+1
    else:
      e2[b] = arr[i]
      b+1
    i + 1

rail(plainText)
      
      