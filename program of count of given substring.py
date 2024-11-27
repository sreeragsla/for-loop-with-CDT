#w.a.p.t.p how many time given substring is present in given string

ms='sreerag'
ss='r'
c=0
for i in ms:
    if i in ss:
        c+=1
print(f'number of time given substring present is {c}')

'''
iteration
1.it will take 's' and check whether it is present in ss.'s' is not present in ss
  condition will not satisfies and c will remain 0
2.it will take 'r' and check whether it is present in ss.'r' is present in ss condition
  satisfies and increment will happen and c goes 0 to 1
3.it will take 'e' and check whether it is present in ss.'e' is not present in ss
  condition will not satisfies and c will remain 1
4.it will take 'e' and check whether it is present in ss.'e' is not present in ss
  condition will not satisfies and c will remain 1
5.it will take 'r' and check whether it is present in ss.'r' is present in ss condition
  satisfies and increment will happen and c goes 1 to 2
6.it will take 'a' and check whether it is present in ss.'a' is not present in ss
  condition will not satisfies and c will remain 2
7.it will take 'g' and check whether it is present in ss.'g' is not present in ss
  condition will not satisfies and c will remain 2
8.after iteration it will come out of the loop and printing c

'''







