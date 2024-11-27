'''
d1={'a':20,'b':30,'c':400,'e':500}
d2={'a':40,'b':20,'c':500,'d':25}
d={'a':40,'b':30,'c':500,'d':25,'e':500}

'''
d1={'a':20,'b':30,'c':400,'e':500}
d2={'a':40,'b':20,'c':500,'d':25}
d={}
for i in d2:
    if i not in d1:
        d[i]=d2[i]
    elif d2[i]>d1[i]:
        d[i]=d2[i]
    else:
        d[i]=d1[i]
for i in d1:
    if i not in d:
        d[i]=d1[i]
print(d)

'''
iteration
1.controller will take 'a' and check whether 'a' is present in d1.'a' is present
  so condition false.Then in the elif part it will check d2['a'] is greater than
  d1['a'] or not.d2['a'] is greater so condition satisfies and d['a'] will assign
  with d2['a']
2.it will take 'b' and check whether 'b' is present in d1.'b' is present so condition
  false.Then in the elif part it will check d2['b'] is greater than d1['b'] or not.
  d2['b'] is not greater so in the else part d['b'] will assign d1['b']
3.it will take 'c' and check whether 'c' is present in d1.'c' is present so condition
  false.Then in the elif part it will check d2['c'] is greater than d1['c'] or not.
  d2['b'] is greater so condition satisfies and d['c'] will asign with d2['c']
4.it will take 'd' and check whether 'd' is present in d1.'d' is not present in d1
  so condition satisfies and d['d'] will assign with d2['d']
5.after iteration controller will come out of the loop
6.controller will enter the next loop and take 'a' and check whether 'a' is present
  in d or not.'a' is present so condition does not satisfies
7.it will take 'b' and check whether 'b' is present in d or not.'b' is present so
  condition does not satisfies
8.it will take 'c' and check whether 'c' is present in d or not.'c' is present so
  condition does not satisfies
9.it will take 'e' and check whether 'e' is present in d or not.'e' is not present
  so condition satisfies and d['e'] will assign with d1['e']
10.after iteration controller will come out of the loop and printing d

'''


  

    
    

