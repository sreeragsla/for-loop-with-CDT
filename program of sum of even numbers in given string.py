#w.a.p.t.p the sum of even digits present in a given string

s='sreerag245'
es=0
for i in s:
    if i.isdigit():
        k=int(i)
        if k%2==0:
            es+=k
print(f'even digit sum of given string is {es}')

'''
iteration
1.controller will take 's' and check whether it is a digit or not.'s' is not a digit
  so condition does not satisfies
2.it will take 'r' and check whether it is a digit or not.'r' is not a digit so
  condition does not satisfies
3.it will take 'e' and check whether it is a digit or not.'e' is not a digit so
  condition does not satisfies
4.it will take 'e' and check whether it is a digit or not.'e' is not a digit so
  condition does not satisfies
5.it will take 'r' and check whether it is a digit or not.'r' is not a digit so
  condition does not satisfies
6.it will take 'a' and check whether it is a digit or not.'a' is not a digit so
  condition does not satisfies
7.it will take 'g' and check whether it is a digit or not.'g' is not a digit so
  condition does not satisfies
8.it will take '2' and check whether it is a digit or not.'2' is a digit so condition
  satisfies and typecasting will happen and it is stored in k.Then it will check whether
  it is even or odd.If it even es will be added with k value and stored in es.'2' is even
  so it will added with es and stored in es
9.it will take '4' and check whether it is a digit or not.'4' is a digit so condition
  satisfies and typecasting will happen and stored the value in k.Then it will check
  whether it is even or odd.'4' is even so it will add with es and stored the added
  value in es
10.it will take '5' and check whether it is a digit or not.'5' is a digit so condition
  satisfies and typecasting will happen and stored the value in k.Then it will check
  whether it is even or odd.'5' is odd so condition does not satisfies and es value
  will remain same
11.after iteration controller will come out of the loop and printing es

'''



