a='gaponov.1997@yandex.ru'
file=open('WB.csv','r')

text=file.read()

if a in text:
    print ('этот пароль есть в базе')
else:
    print ('пароля нет в базе')