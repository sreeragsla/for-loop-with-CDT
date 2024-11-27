#w.a.p.t.p how many consonents are present in given string

s='sreerag1013'
vowels='aeiouAEIOU'
cc=0
for i in s:
    if i.isalpha():
        if i not in vowels:
            cc+=1
print(f'number of consonents present in given string is {cc}')

'''
iteration
1.it will take 's' and check whether it is a alphabet or not.'s' is a alphabet so
  condition satisfies and it will check whether 's' is in vowels or not.'s' is not
  in vowels so condition satisfies and increment will happen and cc goes 0 to 1
2.it will take 'r' and check whether it is a alphabet or not.'r' is a alphabet so
  condition satisfies and it will check whether 'r' is in vowels or not.'r' is not
  in vowels so condition satisfies and increment will happen and cc goes 1 to 2
3.it will take 'e' and check whether it is a alphabet or not.'e' is a alphabet so
  condition will satisfies and it will check whether 'e' is in vowels or not.'e'
  is in the vowels so condition will not satisfies and cc will remain 2
4.it will take 'e' and check whether it is a alphabet or not.'e' is a alphabet so
  condition will satisfies and it will check whether 'e' is in vowels or not.'e'
  is in the vowels so condition will not satisfies and cc will remain 2
5.it will take 'r' and check whether it is a alphabet or not.'r' is a alphabet so
  condition satisfies and it will check whether 'r' is in vowels or not.'r' is not
  in vowels so condition satisfies and increment will happen and cc goes 2 to 3
6.it will take 'a' and check whether it is a alphabet or not.'a' is a alphabet so
  condition will satisfies and it will check whether 'a' is in vowels or not.'a'
  is in the vowels so condition will not satisfies and cc will remain 3
7.it will take 'g' and check whether it is a alphabet or not.'g' is a alphabet so
  condition satisfies and it will check whether 'r' is in vowels or not.'g' is not
  in vowels so condition satisfies and increment will happen and cc goes 3 to 4
8.it will take '1' and check whether it is a alphabet or not.'1' is not a alphabet
  so condition not satisfies and cc will remain 4
9.it will take '0' and check whether it is a alphabet or not.'0' is not a alphabet
  so condition not satisfies and cc will remain 4
10.it will take '1' and check whether it is a alphabet or not.'1' is not a alphabet
  so condition not satisfies and cc will remain 4
11.it will take '3' and check whether it is a alphabet or not.'3' is not a alphabet
  so condition not satisfies and cc will remain 4
12.after iteration it will come out the loop and printing cc

'''

