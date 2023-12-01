a,v,s=open(0).readlines(),{"X":1,"Y":2,"Z":3,"A":1,"B":2,"C":3},0
for l in a:
 i,j=v[l.strip()[0]],v[l.strip()[2]]
 if i==j:
  j=j+3
 elif (j==1 and i==3)or(j==3 and i==2)or(j==2 and i==1):
  j=j+6
 s=s+j
print(s)