#w.a.p.t.p the sum of digits present in given string

s='sreerag1013'
summ=0
for i in s:
    if i.isdigit():
        k=int(i)
        summ+=k
print(f'sum of digits present in given string is {summ}')

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
8.it will take '1' and check whether it is a digit or not.'1' is digit so condition
  satisfies and typecasting will happen and stored the value in k.Then k value
  will added with summ and stored in summ
9.it will take '0' and check whether it is a digit or not.'0' is digit so condition
  satisfies and typecasting will happen and stored the value in k.Then k value
  will added with summ and stored in summ
10.it will take '1' and check whether it is a digit or not.'1' is digit so condition
  satisfies and typecasting will happen and stored the value in k.Then k value
  will added with summ and stored in summ
11.it will take '3' and check whether it is a digit or not.'3' is digit so condition
  satisfies and typecasting will happen and stored the value in k.Then k value
  will added with summ and stored in summ
12.after iteration controller will come out of the loop and printing summ

'''





