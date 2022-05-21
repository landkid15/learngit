hello
the net is good.
I am not playing fgo.
I would run tomorrow.
classmates=['Apple','apple','Cook']
classmates.append('Dave')
classmates.insert(1,'Bruce')
classmates.pop(2)
classmates[2]='Carter'
classmates.append(561)
print(classmates)
people=['president li',classmates,'saniters']
print(people)
print(people[1][2])
t=(1,2)
print(t)
t=('a','b',['A','B'])
t[2][0]='X'
t[2][1]='Y'
print(t)
L=[
    ['Apple','Google','Microsoft'],
    ['Java','Python','Ruby','PHP'],
    ['Adam','Bart','Lisa']
]
print(L[2][2])
for name in classmates:
    print(name)
for tag in L:
    print(tag)
sum=0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum=sum+x
print(sum)
sum=0
print(list(range(11)))
for y in range(101):
    sum=sum+y
print(sum)
sum=0
n=99
while n>0:
    sum=sum+n
    n=n-2
print(sum)
for tag in L:
    print('I could deal with',tag)
for tag in L[1]:
    print('I could deal with',tag)
n=1
while n <=100:
    n=n+1
    if n >33:
        break 
    if n%2==0:
        continue
    print(n)
print('end')
n=0
while n<10:
    n=n+1
    if n%2==0:
        continue
    print(n)
