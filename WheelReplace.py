#python program to show wheels replaced to run maximum distannce

def LastRotate(W,total,n):
  k=0
  for i in range(0,n):
   W[i]=W[i]-S
  W=RotateByN(W,2,total)
  for j in range(0,n):
    W[j]=W[j]-S
  while(k<total):
    if(W[k]==0):
      capacity=0
    else:
      capacity=1
    k=k+1
  if(capacity==0):
    print("All tyres has been fully utilized")
  else:
    print("Not all tyres has been fully utilized")
  MD=S*total
  print("The maximum distance Vehicle can travel with replacing all spare tyres",MD)

def TyreExchange(W,total,n,m,S):
  j=0
  k=total-1
  least=(k-m)
  print(W)
  for i in range(0,n):
    W[i]=W[i]-S
  print("Tyre capacity after optimal dstance",W)
  while(j<m):
    while(k>=least):
      temp=W[j]
      W[j]=W[k]
      W[k]=temp
      k=k-1
      j=j+1
  print("Tyre capacity after first tyre replace",W)
  Rotate(W,S,n,total)

def Rotate(W,S,n,total):  
  count=2
  while(count<5):
    for i in range(0,n):
      W[i]=W[i]-S
    W=RotateByN(W,1,total)
    print("Tyre capacity after next optimal dstance and replacement",W)
    count=count+1
  LastRotate(W,total,n)

def RotateByN(W,r,total):
  L=[]
  index=total-1
  indexer=index-r
  while(indexer<index):
    indexer=indexer+1
    L.append(W[indexer])
  for item in range(0,total-r):
    L.append(W[item])
  W=L
  return W
    

if __name__=='__main__':
  W=[]
  n=int(input("Enter number of wheels in Vehicle :"))
  m=int(input("Enter number of spare tyres available :"))
  D=int(input("Enter maximum distance a Vehicle can travel :"))
  total=n+m
  S=int(D/n)
  for i in range(0,total):
    W.append(D)
  TyreExchange(W,total,n,m,S)
  