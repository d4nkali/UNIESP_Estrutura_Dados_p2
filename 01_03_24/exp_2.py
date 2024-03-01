# Exemplo 2 - Selection sort

vetor = [3,8,7,2,6,1]
n=len(vetor)
print(vetor)
for i in range(n):
  id_min=i
  print(i,'<-')
  for j in range(i+1,n):
    print(j,'*')
    if vetor[id_min]>vetor[j]:
      id_min=j
  aux=vetor[i]
  vetor[i]=vetor[id_min]
  vetor[id_min]=aux

print(vetor)