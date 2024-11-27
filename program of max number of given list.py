#w.a.p.t find the maximum number in a given list

l=[2,28,10,36,4,7]
m=l[0]
for i in l:
    if i>m:
        m=i
print(f'max is {m}')

'''
iteration
1.it will take 2 and check whether it is greater than m.Here we are taking m as zeroth
  index position value for comparison purpose.it is not greater so condition does not satisfy
2.it will take 28 and check whether it is greater than zeroth index m.it is greater than the value.
  so condition satisfies and it will assign i value to m
3.it will take 10 and check whether it is greater than m.10 is not greater than m.so condition does
  not satisfy.m value remains 28
4.it will take 36 and check whether it is greater than m.36 is greater than m.so condition satisfies
  and i value will assign to m
5.it will take 4 and check whether it is greater than m.4 is not greater than m so condition does
  not satisfy and m value will remain on 36
6.it will take 7 and check whether it is greater than m.7 is not greater than m so condition does
  not satisfies and m value will remain on 36
7.after the iteration controller will come out of the loop and printing m

'''
  




        
