def fakt(n):
    '''
        returns the factorial from n
        Syntax: fraktal(n)
    '''
    erg = 1
    while n > 0:
        erg *= n
        n -= 1
    return erg

a = 5

lst =[]

for i in range(1, a+1):
    lst.append(fakt(i))

#print(lst)
print(fakt(a))


