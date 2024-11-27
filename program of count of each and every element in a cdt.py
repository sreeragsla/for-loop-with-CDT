#w.a.p.t print how many time each and every element is present in given cdt

cdt='sreerag'
d={}
for i in cdt:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)

'''
#method 2
cdt='sreerag'
d={}.fromkeys(cdt,0)
for i in cdt:
    d[i]+=1
print(d)
'''
'''
#method 3
cdt='sreerag'
d={}
for i in cdt:
    d[i]=cdt.count(i)
print(d)
'''
'''
iteration
1.it will take 's' and check whether 's' is in d or not.'s' is not in d so in the if
  part d['s']=1 will take added to the dictionary
2.it will take 'r' and check whether 'r' is in d or not.'r' is not in d so in the if
  part d['r']=1 will take added to the dictionary
3.it will take 'e' and check whether 'e' is in d or not.'e' is not in d so in the if
  part d['e']=1 will take added to the dictionary
4.it will take 'e' and check whether 'e' is in d or not.'e' is in d so in the else
  part d['e']=1+1 will take and updated to the dictionary
5.it will take 'r' and check whether 'r' is in d or not.'r' is in d so in the else
  part d['r']=1+1 will take and updated to the dictionary
6.it will take 'a' and check whether 'a' is in d or not.'a' is not in d so in the if
  part d['a']=1 will take added to the dictionary
7.it will take 'g' and check whether 'g' is in d or not.'g' is not in d so in the if
  part d['g']=1 will take added to the dictionary
8.after iteration it will come out of the loop and printing d
'''



