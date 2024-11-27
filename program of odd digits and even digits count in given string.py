#w.a.p.t.p count how many even digits and odd digits are present in given string

s='sreerag1213'
ec=0
oc=0
for i in s:
    if i.isdigit():
        k=int(i)
        if k%2==0:
            ec+=1
        else:
            oc+=1
print(f'even digit count is {ec}')
print(f'odd digit count is {oc}')

'''
iteration
1.controller will take 's' and check it is a digit or not.'s' is not a digit so
  condition does not satisfies and ec,oc will remain on 0
2.it will take 'r' and check whether it is a digit or not.'r' is not a digit so
  condition does not satisfies and ec,oc will remain on 0
3.it will take 'e' and check whether it is a digit or not.'e' is not a digit so
  condition does not satisfies and ec,oc will remain on 0
4.it will take 'e' and check whether it is a digit or not.'e' is not a digit so
  condition does not satisfies and ec,oc will remain on 0
5.it will take 'r' and check whether it is a digit or not.'r' is not a digit so
  condition does not satisfies and ec,oc will remain on 0
6.it will take 'a' and check whether it is a digit or not.'a' is not a digit so
  condition does not satisfies and ec,oc will remain on 0
7.it will take 'g' and check whether it is a digit or not.'g' is not a digit so
  condition does not satisfies and ec,oc will remain on 0
8.it will take '1' and check whether it is a digit or not.'1' is a digit so condition
  satisfies and typecasting will happen and i value will assign to k.Then it will
  check whether k is even or not.if k is even increment will happen and ec will
  goes 0 to 1,else increment will happen and oc will goes 0 to 1.1 is odd in the
  else part increment will happen and oc will goes 0 to 1
9.it will take '2' and check whether it is a digit or not.'2' is a digit so condition
  satisfies and typecasting will happen and i value will stored in k.Then it will
  check whether it is even or odd.'2' is even in the if part increment will happen
  and ec will goes 0 to 1
10.it will take '1' and check whether it is a digit or not.'1' is a digit so condition
   satisfies and typecasting will happen and i value is stored in k.Then it will check
   whether it is even or odd.'1' is odd in the else part increment will happen and oc
   will goes 1 to 2
11.it will take '3' and check whether it is a digit or not.'3' is a digit so condition
   satisfies and typecasting will happen and i value is stored in k.Then it will check
   whether it is even or odd.'3' is odd in the else part increment will happen and oc
   will goes 2 to 3
12.after iteration controller will come out of the loop and printing oc,ec

'''


