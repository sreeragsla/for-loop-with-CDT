#w.a.p.t find the sum of digits present in a list

l=[22,33,2,3]
summ=0
for i in l:
    if type(i)==int:
        summ+=i
print(f'sum of digits is {summ}')

'''
l=[22,33,2,3]
summ=0
for i in l:
    if isinstance(i,int):
        summ+=i
print(f'sum of digits is {summ}')
'''
'''
iteration
1.controller will take 22 and check whether type of 22 is integer or not.Type of 22
  is integer so condition satisfies and we are adding i value with summ.it will
  add 0 and 22 and the added value will be stored in summ
2.it will take 33 and check whether type of 33 is interger or not.Type of 33 is
  integer so condition satisfies and i value will be added with summ and stored
3.it will take 2 and check whether type of 2 is interger or not.Type of 2 is
  integer so condition satisfies and i value will be added with summ and stored
4.it will take 3 and check whether type of 3 is interger or not.Type of 3 is
  integer so condition satisfies and i value will be added with summ and stored
5.after iteration controller will come out of the loop and printing summ

'''



  

