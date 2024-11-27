#w.a.p.t.p how many numbers are present in given string

s='sreerag1234'
c=0

for i in s:
    if i.isdigit():
        c+=1
print(f'number of digits present in given string is {c}')



'''
iteration
1.it will take 's' and check whether it is a digit or not.'s' is not a digit so
  c will remain on o
2.it will take 'r' and check whether it is a digit or not.'r' is not a digit so
  c will remain on 0
3.it will take 'e' and check whether it is a digit or not.'e' is not a digit so
  c will remain on 0
4.like that it will take each and every element and checks whether it is a number
5.after taking 'g' it will take '1' and check whether it is a digit or not.'1'
  is a digit so it will satisfy if condition and increment will happen and c goes
  0 to 1
6.it will take '2' and check whether it is a digit.'2' is a digit so increment
  will happen and c goes 1 to 2
7.it will take '3' and check whether it is a digit.'3' is a digit so increment
  will happen and c goes 2 to 3
8.it will take '4' and check whether it is a digit.'4' is a digit so increment
  will happen and c goes 3 to 4

'''  






    







    
    
