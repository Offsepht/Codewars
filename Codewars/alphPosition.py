def alphabet_position(text):
    dict = {'a':'1','b':'2','c':'3','d':'4','e':'5','f':'6','g':'7',
            'h':'8','i':'9','j':'10','k':'11','l':'12','m':'13','n':'14',
            'o':'15','p':'16','q':'17','r':'18','s':'19','t':'20','u':'21','v':'22',
            'w':'23','x':'24','y':'25','z':'26'}
    new_text = text.lower()
    new_string = []
    for i in new_text:
        if i in dict:
            new_strin = new_string.append(dict[i])
    return ' '.join(new_string)


print(alphabet_position("The sunset sets at twelve o' clock."))
#"20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"