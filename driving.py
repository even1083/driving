coutry = input('請輸入國家:')
age = input('請輸入年齡:')
age = int(age)
if coutry == 台灣:
    if age >= 18:
        print('你可以考駕照')
    else:
        print('你還不能考駕照')
elif coutry == 美國:
    if age >= 16:
        print('你可以考駕照')
    else:
        print('你還不能考駕照')
else
    print('只能輸入台灣/美國')