#w.a.p.t.p how many special characters are present in given string

s='sreerag s@%^'
sc=0
for i in s:
    if not i.isalnum():
        sc+=1
print(f'special character count is {sc}')

'''
iteration
1.it will take 's' and check whether it is not a alphaneumerical.'s' is a alphaneumerical
  so condition does not satisfy.so sc will remain 0
2.it will take 'r' and check whether it is not a alphaneumerical.'r' is a alphaneumerical
  so condition does not satisfy.so sc will remain 0
3.it will take 'e' and check whether it is not a alphaneumerical.'e' is a alphaneumerical
  so condition does not satisfy.so sc will remain 0
4.it will take 'a' and check whether it is not a alphaneumerical.'a' is a alphaneumerical
  so condition does not satisfy.so sc will remain 0
5.it will take 'g' and check whether it is not a alphaneumerical.'g' is a alphaneumerical
  so condition does not satisfy.so sc will remain 0
6.it will take ' ' and check whether it is not a alphaneumerical.' ' is a special
  character.so condition satisfy and increment will happen.sc will goes 0 to 1
7.it will take 's' and check whether it is not a alphaneumerical.'s' is a alphaneumerical
  so condition does not satisfy.so sc will remain 1
8.it will take '@' and check whether it is not a alphaneumerical.'@' is a special
  character.so condition satisfy and increment will happen.sc will goes 1 to 2
9.it will take '%' and check whether it is not a alphaneumerical.'%' is a special
  character.so condition satisfy and increment will happen.sc will goes 2 to 3
10.it will take '^' and check whether it is not a alphaneumerical.'^' is a special
  character.so condition satisfy and increment will happen.sc will goes 3 to 4

'''




  
  
