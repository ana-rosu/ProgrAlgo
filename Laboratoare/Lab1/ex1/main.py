'''
3 nr nat, afisam in format zz/mm/yyyy
The months having 31 days in a year are January, March, May, July, August, October, and December.
pt 28.2 vr 1.3 doar daca e an nebisect
'''
zz = int(input('Dati ziua: '))
mm = int(input('Dati luna: '))
yyyy = int(input('Dati anul: '))

if mm != 2:
    if (zz + 1 <= 31 and (mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm == 12)) or (
            zz + 1 <= 30 and (mm == 4 or mm == 6 or mm == 9 or mm == 11)):
        zz = zz + 1
    elif mm < 12:
        mm = mm + 1
        zz = 1
    if mm == 12 and zz == 31:
        yyyy = yyyy + 1
        mm = 1
        zz = 1
else:
    # an bisect (februarie are 29 de zile)
    if (yyyy % 4 == 0 and yyyy % 100 != 100) or yyyy % 400 == 0:
        if zz == 29:
            zz = 1
            mm = 3
        else:
            zz = zz + 1
    # an nebisect (februarie are 28 de zile)
    else:
        if not ((yyyy % 4 == 0 and yyyy % 100 != 100) or yyyy % 400 == 0):
            if zz == 28:
                zz = 1
                mm = 3
            else:
                zz = zz + 1

print(zz, mm, yyyy, sep=".")
