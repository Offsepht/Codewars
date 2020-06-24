def xo(s):
    
    o = s.lower().count('o')
    x = s.lower().count('x')

    if o == x : print True
    elif o != x : print False
    else:
        print True

xo('fr232')
not xo('xxxohhho')