
# Программа разработана самостоятельно
#
#               Игра "быки"-"коровы"
# Игрок задумывает четырех символьное число из неповторющихся цифр
# Компьютер "задумывает" аналогичное число
# Игрок вводит четырех символьное число из неповторющихся цифр
# Компьютер отвечает чарез двоеточие двумя цифрами.Первая число
# угаданных символов в числк,вторая цифра- сколько из них стоят
# на том же месте ,что и введеным числе
# Компьютер выводит свое  аналогичное число на которое вы должны
# ответить      Удачи  !!!
def random_number_41():
    """генерация четырех символьной строки из неповторяюшихся цифр"""
    import random
    while True :
        number_4 = random.randint(0, 9999)
        if (len(set(str(number_4))))==4 :
              return str(number_4)
              break


def random_number_4():
    """генерация четырех символьной строки из неповторяюшихся цифр"""
    import random
    all_number="0123456789"
    start_num =random.randint(1,8)#случайное число для начапа перебора
    str_num=all_number[start_num:]+all_number[:start_num]
    ansver = ''
    len_str=3 #формируем 3 символьное слово чтобы избежать повтора чисел
    prior = ('43215') #приоритеты выбора чисел согласно статуса цифра
    for index in prior:
        for number_num in str_num:
            if staus_str[int(number_num)] == str(index):
                ansver += all_number[int(number_num)]
            if len(ansver)!=0 and index=='4':
                len_str=4  #для статуса 4 символ не дополняем
            if len(ansver) == len_str:
                   if len(ansver) ==4:
                       return ansver
                   else:
                       # lдля статуса отличного от 4 формирует число из трех символов
                       # дополням  случайным символом и проверяем число на уникальноать
                       while True:
                           ansver+=str(random.randint(0,9))
                           if len(set(ansver ))==4:
                               return ansver
                               break
                           ansver=ansver[:3]
def compare_number(num_secret,num_send):
    """сравнивает введеное число с задуманым
       первый символ-общее сисло,второй символ  втом же места"""
    result=0
    for index in range(0,4):
        if(num_secret[index]==num_send[index]):
            result +=1
    num_overall=set(num_secret) & set( num_send)
    all_num= len(num_overall)
    return str(all_num)+":"+str(result)

def get_number():
    """ ввод цифровых символов"""
    try:
        num_send = int(input("Введите число компу"))
        return num_send
    except ValueError:
        print("Вы ввели не число.")
def number2(ansver):
    all_numb={'0','1','2','3','4','5','6','7','8','9'}
    rez6= all_numb - set(ansver)
    num7=rez6.pop()
    num8=rez6.pop()
    return str(rez6)+num7+num8
def set_status():
    """изменяем статус цифры в соответствии ответа на число"""
    for index in range(0,4):
        staus_str[int(ansver[index])]=num_res[0]


#сохранить задуманное секретное число
staus_str=['5','5','5','5','5','5','5','5','5','5']
history='' #история ударов [[удар],[ответ]]
num_secret = random_number_41()#секретное слово
ansver=random_number_41()#слово удара по компу
num_res=""#анализ удара компа
inter=1 #номер интерации
#print(num_secret)
while True:
    num_send = get_number()
    if len(str(num_send)) != 4:
        print('    не четыре символа')
        continue
    num_send = str(num_send)
    if len(num_send) != 4:
        print('     не разные символы ')
        continue
    rez_comp=str(compare_number(num_secret, num_send))
    print('    ' + rez_comp+ '      ' + ansver)
    if (rez_comp=='4:4'):
         print('Я выиграл у компа')
         break
    num_send=''
    while True:
        num_res = input("Введите анализ удара компа")
        if len(str(num_res)) != 3:
            print('    не три символа')
            continue
        if str(num_res[0])> '4':
            print('    первый символ не больше 4')
            continue
        if str(num_res[2]) > '4':
            print('    второй символ не больше 4')
            continue
        if str(num_res[2]) > str(num_res[0]):
            print('    второй символ не больше первого')
            continue
        if str(num_res[1]) !=':':
            print('   между первым и вторым символами не стоит : ')
            continue
        break

    set_status()
    if (num_res == '4:4'):
        print('Вы выиграли.Поздравляю!!!')
        break
    if inter == 1:
        if (num_res == '4:2'):
            ansver = ansver[1] + ansver[0] + ansver[3] + ansver[2]  # следующее число удара
        if (num_res == '4:0'):
            ansver = ansver[::-1]  # следующее число удара
        if (num_res[0] == 1):
            ansver = number2(ansver)  # следующее число удара
    if inter == 2:
        if (num_res == '4:2'):
            ansver = ansver[0] + ansver[1] + ansver[3] + ansver[2]  # следующее число удара
        if (num_res == '4:0'):
            ansver = ansver[::-1]  # следующее число удара
        if (num_res[0] == 1):
            ansver = number2(ansver) # следующее число удара

    if inter == 3:
        if (num_res == '4:2'):
                ansver = ansver[0] + ansver[2] + ansver[1] + ansver[3]  # следующее число удара
        if (num_res == '4:0'):
                ansver = ansver[::-1]  # следующее число удара
    if inter==1:
        history += ansver + num_res
    count=0
    ansver =random_number_4()
    while (count < len(history)):
        send_hictory=history[count:4]
        rez=compare_number(ansver,send_hictory)
        if(rez==history[count+4:count+8]):
             count+=7
        else:

             break
    inter+=1