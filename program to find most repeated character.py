#w.a.p.t.p most repeated character in a given string

s='sreerag'
mrc=''
c=0
for i in s:
    if s.count(i)>c:
        c=s.count(i)
        mrc=i
print(f'most repeated character is {mrc,c}')

'''
#method 2

s=input()
Max=0
d={}
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
for i in d:
    if d[i]>Max:
        Max=d[i]
for i in d:
    if d[i]==Max:
        print(i,d[i])
'''
'''
iteration
1.controller will take 's' and will check whether count of 's' is greater than c.
  if it is greater than it will assigned to c.we are taking c=0 for comparing purpose.
  so count of 's' is greater than c so it will assign to c and mrc will assign as
  's'
2.it will take 'r' and wil check whether count of 'r' is greater than c.count of
  'r' is greater than c so it will assign to c and mrc will assign 'r'
3.it will take 'e' and will check whether count of 'e' is greater than c.both 'r'
  and 'e' is repeating 2 times.so condition will false and c will remain as count
  of 'r'
4.it will take 'a' and will check whether count of 'a' is greater than c.count of
  'a' is not greater than c so condition does not satisfies
5.it will take 'g' and will check whether count of 'g' is greater than c.count of
  'g' is not greater than c so condition does not satisfies
6.after iteration controller will come out of the loop and printing mrc

'''




