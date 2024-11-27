#w.a.p.t.p how many vowels are present in given string

s='sreerag1013'
vowels='aeiouAEIOU'
c=0
for i in s:
    if i in vowels:
        c+=1
print(f'number of vowels present in given string is {c}')

'''
iteration
1.controller will take 's' and check whether it is present in vowels.'s' is not present
  in vowels so condition not satisfies and c will remain on 0
2.it will take 'r' and check whether it is present in vowels.'r' is not present
  in vowels so condition does not satisfies and c will remain on 0
3.it will take 'e' and check whether it is present in vowels.'e' is present in
  vowels so condition satisfies and increment will happen.c will goes 0 to 1
4.it will take 'e' and check whether it is present in vowels.'e' is present in
  vowels so condition satisfies and increment will happen.c will goes 1 to 2
5.it will take 'r' and check whether it is present in vowels.'r' is not present
  in vowels so condition does not satisfies and c will remain on 2
6.it will take 'a' and check whether it is present in vowels.'a' is present in
  vowels so condition satisfies and increment will happen.c will goes 2 to 3
7.it will take 'g' and check whether it is present in vowels.'g' is not present
  in vowels so condition does not satisfies and c will remain on 3
8.it will take '1' and check whether it is present in vowels.'1' is not present
  in vowels so condition does not satisfies and c will remain on 3
9.it will take '0' and check whether it is present in vowels.'0' is not present
  in vowels so condition does not satisfies and c will remain on 3
10.it will take '1' and check whether it is present in vowels.'1' is not present
  in vowels so condition does not satisfies and c will remain on 3
11.it will take '3' and check whether it is present in vowels.'3' is not present
  in vowels so condition does not satisfies and c will remain on 3
12.after iteration controller will come out of the loop and printing c

'''


