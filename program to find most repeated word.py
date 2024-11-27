#w.a.p.t.p most repeated word ina given string

s='sreerag loves python sreerag'
ws=s.split()
mrw=''
c=0
for i in ws:
    if ws.count(i)>c:
        c=ws.count(i)
        mrw=i
print(f'most repeated word is {mrw}')

'''
iteration
1.first we are doing spliting method with s and stored it in ws
2.controller will take 'sreerag' and check whether count of 'sreerag' is greater
  than c.for comparison purpose we are taking c=0.count of 'sreerag' is greater
  than c so count of 'sreerag' will be assign to c and mrw will assign 'sreerag'.
  'sreerag' is 2 times repeated.so c will become 2 and mrw will becom 'sreerag'
3.it will take 'loves' and check whether count of 'loves' is greater than c.condition
  will not satisfy so c will remain on 2 and mrw will remain as 'sreerag'
4.it will take 'python' and check whether count of 'python' is greater than c.condition
  will not satisfy so c will remain on 2 and mrw will remain as 'sreerag'
5.after iteration controller will come out of the loop and printing mrw
    
'''




