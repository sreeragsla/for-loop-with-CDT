#w.a.p.t.p sum of odd digits and even digits present in given string

s='sreerag121314'
es=0
os=0
for i in s:
    if i.isdigit():
        k=int(i)
        if k%2==0:
            es+=k
        else:
            os+=k
print(f'even digit sum is {es}')
print(f'odd digit sum is {os}')

'''
iteration
1.it will take 's' check whether it is digit or not.'s' is not a digit so condition
  will not satisfy
2.it will take 'r' check whether it is digit or not.'r' is not a digit so condition
  will not satisfy
3.it will take 'e' check whether it is digit or not.'e' is not a digit so condition
  will not satisfy
4.it will take 'e' check whether it is digit or not.'e' is not a digit so condition
  will not satisfy
5.it will take 'r' check whether it is digit or not.'r' is not a digit so condition
  will not satisfy
6.it will take 'a' check whether it is digit or not.'a' is not a digit so condition
  will not satisfy
7.it will take 'g' check whether it is digit or not.'g' is not a digit so condition
  will not satisfy
8.it will take '1' check whether it is digit or not.'1' is a digit so condition will
  satisfy and typecasting will be done and check if it is a even or not.1 is odd
  so os will add 0 and 1 to 1
9.it will take '2' check whether it is digit or not.'2' is a digit so condition will
  satisfy and typecasting will be done and check if it is a even or not.2 is even
  so es will add 0 and 2 to 2
10.it will take '1' check whether it is digit or not.'1' is a digit so condition will
  satisfy and typecasting will be done and check if it is a even or not.1 is odd
  so os will add 1 and 1 to 2
11.it will take '3' check whether it is digit or not.'3' is a digit so condition will
  satisfy and typecasting will be done and check if it is a even or not.3 is odd
  so os will add 2 and 3 to 5
12.it will take '1' check whether it is digit or not.'1' is a digit so condition will
  satisfy and typecasting will be done and check if it is a even or not.1 is odd
  so os will add 5 and 1 to 6
13.it will take '4' check whether it is digit or not.'4' is a digit so condition will
  satisfy and typecasting will be done and check if it is a even or not.4 is even
  so es will add 2 and 4 to 6
14.after completing iteration it will come out of the loop and printing os and es

'''



