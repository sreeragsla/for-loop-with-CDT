L=[11,22,33,44,55]
for L[-1] in L:
    print(L[-1])
print(L)

'''
iteration
1.controller will take 11 and it will assign to L[-1] and 11 will be printed
2.it will take 22 and it will assign to L[-1].early L[-1] was 11 and it will replaced
  with 22 and it is printed
3.it will take 33 and it will assign to L[-1].early L[-1] was 22 and it will replaced
  with 33 and it is printed
4.it will take 44 and it will assign to L[-1].early L[-1] was 33 and it will replaced
  with 44 and it is printed
5.last element is also 44 and controller will take 44 and will assign to L[-1].44
  will again replaced with 44 and it is printed
6.after iteration controller will come out of the loop and printing L.L is [11,22,33,44,44]

'''




    
