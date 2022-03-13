number=int(input())
list=[]
i=0
while(i<number):
  j=0
  if(i==0 or i==number-1):
    mini=[]
    while(j<number):
      mini.append("w")
      j=j+1
  else:
    mini=["w"]
    while(j<number-2):
      mini.append(" ")
      j=j+1
    mini.append("w")
  list.append(mini)
   i=i+1
i=0
while(i<number):
  j=0
  while(j<number):
    print(list[i][j],end=" ")
    j=j+1
  i=i+1
  print()
