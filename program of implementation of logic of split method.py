#implement the logic of split method

s='how are you sreerag'
delimator='r'
L=[]
summ=''
for i in s:
    if i != delimator:
        summ+=i
    else:
        L.append(summ)
        summ=''
L.append(summ)
print(L)

'''
iteration
1.controller will take 'h' and check whether it is not equal to delimator or not.
  it is not equal so condition satisfies and summ will be added with 'h' and added
  value will be stored in summ
2.
      
''''
