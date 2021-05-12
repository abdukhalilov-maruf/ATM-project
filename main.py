import pymongo
import random

client = pymongo.MongoClient()
my_firstDb = client['FirstDb']
db_collection = my_firstDb['users']

text_red = '\033[91m'
text_green = '\x1b[6;30;42m'
text_white = '\x1b[0m'
text_yellow = '\033[93m'
text_bold = '\033[1m'


def user_reg():
    user = {
        '_id': random.randrange(8600000000000000, 8600999999999999),
        'name': input('Имя владельца карты: '),
        'balance': float(input('Внесите депозить: ')),
        'password': int(input('Введите 4 значный пароль:')),
    }
    try:
        db_collection.insert_one(user)
    except:
        print(text_red + 'Такой id уже существует!!!\n Повторите заного!' + text_white)


def updateDb():
    query = {'_id': _id}
    update = {'$set': {'balance': balance}}
    db_collection.update_one(query, update)


while True:
    func = int(input('1-Создать карту\n2-Операции с картой\nВаш выбор: '))
    if func == 1:
        user_reg()
    elif func == 2:
        _id = int(input('Введите id: '))
        card_pin = int(input('Введите ПИН: '))
        for x in db_collection.find():
            if x['_id'] == _id and x['password'] == card_pin:
                name = x['name']
                balance = float(x['balance'])

                process = True
                while process:
                    print('1-Посмотреть баланс\n2-Внести наличные\n3-Снять наличные\n4-Отправить '
                          'деньги\n5-Завершить')
                    choise = int(input('Ваш выбор: '))

                    if choise == 1:
                        print(f'{text_green}{text_bold} У вас на счету {balance}$! {text_white}')

                    elif choise == 2:
                        insert_sum = float(input('Вставте деньги: '))
                        balance += insert_sum
                        updateDb()
                        print(f'{text_green}{text_bold} Выполнено! {text_white}')

                    elif choise == 3:
                        take_sum = float(input('Какую сумму хотите снять?: '))
                        balance -= take_sum
                        updateDb()
                        print(f'{text_green}{text_bold} Заберите деньги!!! {text_white}')
                    elif choise == 4:
                        send_sum = float(input('Сколько хотите отправить? '))
                        user_id = int(input('Введите id пользователя: '))
                        balance -= send_sum

                        for i in db_collection.find():
                            if i['_id'] == user_id:
                                user_balance = i['balance']
                                user_balance += send_sum

                                key = {'_id': user_id}
                                update_user = {'$set': {'balance': user_balance}}
                                db_collection.update_one(key, update_user)
                                updateDb()
                                print(f'{text_green}{text_bold} Выполнено! {text_white}')
                                break
                        else:
                            print(f'{text_red} Несуществующий id! Попробуйте заного!{text_white}')

                    elif choise == 5:
                        print(f'{text_green}До свидание!{text_white}')
                        break
