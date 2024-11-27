#w.a.p.t.p the absolute difference between even digit sum and odd digit sum

s='sreerag102324'
es=0
os=0
for i in s:
    if i.isdigit():
        k=int(i)
        if k%2==0:
            es+=k
        else:
            os+=k
if es>os:
    print(f'absolute difference is {es-os}')
else:
    print(f'absolute difference is {os-es}')

'''
iteration
1.it will take 's' and check whether it is a digit or not.'s' is not a digit so
  condition will not satisfy
2.it will take 'r' and check whether it is a digit or not.'r' is not a digit so
  condition will not satisfy
3.it will take 'e' and check whether it is a digit or not.'e' is not a digit so
  condition will not satisfy
4.it will take 'e' and check whether it is a digit or not.'e' is not a digit so
  condition will not satisfy
5.it will take 'r' and check whether it is a digit or not.'r' is not a digit so
  condition will not satisfy
6.it will take 'a' and check whether it is a digit or not.'a' is not a digit so
  condition will not satisfy
7.it will take 'g' and check whether it is a digit or not.'g' is not a digit so
  condition will not satisfy
8.it will take '1' and check whether it is a digit or not.'1' is a digit so condition
  will satisfy and typecasting will done and checks whether it is odd or even.1 is
  odd so in the else part os will add 0 and 1 to 1
9.it will take '0' and check whether it is a digit or not.'0' is a digit so condition
  will satisfy and typecasting will done and checks whether it is odd or even.0 is
  even so in the if part es will add 0 and 0 to 0
10.it will take '2' and check whether it is a digit or not.'2' is a digit so condition
  will satisfy and typecasting will done and checks whether it is odd or even.2 is
  even so in the if part es will add 0 and 2 to 2
11.it will take '3' and check whether it is a digit or not.'3' is a digit so condition
  will satisfy and typecasting will done and checks whether it is odd or even.3 is
  odd so in the else part os will add 1 and 3 to 4
12.it will take '2' and check whether it is a digit or not.'2' is a digit so condition
  will satisfy and typecasting will done and checks whether it is odd or even.2 is
  even so in the if part es will add 2 and 2 to 4
13.it will take '4' and check whether it is a digit or not.'4' is a digit so condition
  will satisfy and typecasting will done and checks whether it is odd or even.4 is
  even so in the if part es will add 4 and 4 to 8
14.after completing the iteration it will enter to the outside of the loop and check the
   condition.if es>os it will print es-os else it will print os-es

'''


