list1=['pune','satara','banglore']



a=input('enter city  to be deleted')
if a in list1:
    list1.remove(a)
    print(list1)
else:
    print('not in the list')
    print(f'not present {a}')

