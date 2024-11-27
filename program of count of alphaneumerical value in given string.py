#w.a.p.t.p how many alphaneumerical values present in given string

s='sreerag 1013'
anc=0
for i in s:
    if i.isalnum():
        anc+=1
print(f'number of alphaneumerical value is {anc}')

'''
iteration
1.it will take 's' and check whether it is a alphabet or number.'s' is a alphabet
  so condition will satisfy and increment will happen and anc will goes 0 to 1
2.it will take 'r' and check whether it is a alphabet or number.'r' is a alphabet
  so condition will satisfy and increment will happen and anc will goes 1 to 2
3.it will take 'e' and check whether it is a alphabet or number.'e' is a alphabet
  so condition will satisfy and increment will happen and anc will goes 2 to 3
4.it will take 'e' and check whether it is a alphabet or number.'e' is a alphabet
  so condition will satisfy and increment will happen and anc will goes 3 to 4
5.it will take 'r' and check whether it is a alphabet or number.'r' is a alphabet
  so condition will satisfy and increment will happen and anc will goes 4 to 5
6.it will take 'a' and check whether it is a alphabet or number.'a' is a alphabet
  so condition will satisfy and increment will happen and anc will goes 5 to 6
7.it will take 'g' and check whether it is a alphabet or number.'g' is a alphabet
  so condition will satisfy and increment will happen and anc will goes 6 to 7
8.it will take ' ' and check whether it is a alphabet or not.' ' is not a alphabet
  or number so condition will not satisfy and anc will stay on 7
9.it will take '1' and check whether it is a alphabet or not.'1' is a number so
  condition will satisfy and increment will happen and anc goes 7 to 8
10.it will take '0' and check whether it is a alphabet or not.'0' is a number so
  condition will satisfy and increment will happen and anc goes 8 to 9
11.it will take '1' and check whether it is a alphabet or not.'1' is a number so
  condition will satisfy and increment will happen and anc goes 9 to 10
12.it will take '3' and check whether it is a alphabet or not.'3' is a number so
  condition will satisfy and increment will happen and anc goes 10 to 11
13.after completing iteration it will come out of the loop and printing anc

'''


