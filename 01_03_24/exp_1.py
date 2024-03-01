# Exemplo 1 - Bubble sort

vetor = [3,8,7,2,6,1]
n=len(vetor)
print(vetor)
for i in range(n):
  print(i,'<-')
  for j in range(0,n-i-1):
    print(j,'*')
    if vetor[j]>vetor[j+1]:
      aux=vetor[j]
      vetor[j]=vetor[j+1]
      vetor[j+1]=aux
print(vetor)