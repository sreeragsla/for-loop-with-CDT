#w.a.p.t.p lengthiest word in a given string

s='sreerag is a python full stack developer'
words=s.split()
lw=''
c=0
for i in words:
    if len(i)>c:
        c=len(i)
        lw=i
print(lw)


'''
#method using max function
s='sreerag is a python full stack developer'
words=s.split()
print(max(words,key=len))

'''
'''
iteration
1.first we are spliting s and store in words
2.controller will take 'sreerag' and check whether len('sreerag') is greater
  than c.for comparison purpose we are taking c=0.len('sreerag') is greater than
  c so condition satisfies and c will assign len('sreerag') and lw will assign
  'sreerag'
3.it will take 'is' and check whether len('is') is greater than c.len('is') is not
  greater than c so condition satisfies.c will remain len('sreerag') and lw will
  remain as 'sreerag'
4.it will take 'a' and check whether len('a') is greater than c.len('a') is not
  greater than c so condition satisfies.c will remain len('sreerag') and lw will
  remain as 'sreerag'
5.it will take 'python' and check whether len('python') is greater than c.len('python') is not
  greater than c so condition satisfies.c will remain len('sreerag') and lw will
  remain as 'sreerag'
6.it will take 'full' and check whether len('full') is greater than c.len('full') is not
  greater than c so condition satisfies.c will remain len('sreerag') and lw will
  remain as 'sreerag'
7.it will take 'stack' and check whether len('stack') is greater than c.len('stack') is not
  greater than c so condition satisfies.c will remain len('sreerag') and lw will
  remain as 'sreerag'
8.it will take 'developer' and check whether len('developer') is greater than c.
  len('developer') is greater than c so condition satisfies and c will take len('developer')
  and lw will take 'developer'
9.after iteration controller will come out of the loop and printing lw

'''




