import telebot
from telebot import types
from random import randint
bot = telebot.TeleBot('5743889615:AAF3gd1Va3RYywwD6-8O8GJVobsS71tIt1Y')
# stikers = '⬜️⬜️⬜️\n⬜️⬜️⬜️\n⬜️⬜️⬜️️'
matrix = [['','',''],['','',''],['','','']]
turn = 'x'
users = {}
d = {}


# заполнение словаря users из файлa
try:
    with open(r"C:\Users\volvas\Downloads\users.txt", mode="r", encoding="UTF-8") as file:
        s = file.readlines()
        # s = ["{12341412: {'chat_id': 12423432, 'status': 'ищет игру'}}",
        #      "{12341412123: {'chat_id': 12423432, 'status': 'ищет игру'}}"]


        for i in range(len(s)):
            s[i] = s[i].replace("'", "")[:-2].split(': {')
            # print(s[i])
            users[int(s[i][0])] = {}
            for item in s[i][1].split(', '):

                item = item.split(': ')
                try:
                    users[int(s[i][0])][item[0]] = int(item[1])
                except :
                    users[int(s[i][0])][item[0]] = item[1]
        print(users)


except FileNotFoundError:
    print("Не удалось открыть файл, проверьте путь к файлу!")

games = {}



koloda = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] * 4

import random
random.shuffle(koloda)

count = 0
botcount = 0

# добавление пользователя в словаль users
def add_user(message):
    global users
    users[message.from_user.id] = {'chat_id': message.chat.id,'status': 'не ищет игру', 'current_game': '', 'count': 0, 'botcount': 0}
    print(users)


# заполнение поля в конце игры
# def winner_field(matrix):
#     for row in matrix:
#         for i in range(len(row)):
#             if row[i] == 0:
#                 row[i] = '⭕️'
#             elif row[i] == 1:
#                 row[i] = '❌'
#             else:
#                 row[i] = '⬜️'
#     return '\n'.join([''.join(row) for row in matrix])
def winner_field(matrix):
    for row in matrix:
        for i in range(len(row)):
            if row[i] == 0:
                row[i] = '⭕'
            elif row[i] == 1:
                row[i] = '❌'
            elif row[i] == '':
                row[i] = '⬜'
    return '\n'.join([''.join(row) for row in matrix])
# определение победителя
def win(matrix, call):
    for g in games:
        if call.message.chat.id in g:
            game = g
            break
    if matrix[1][0] == matrix[1][1] and matrix[1][1] == matrix[1][2] and matrix[1][2] == 1:
        bot.edit_message_text(chat_id=game[0], message_id=games[game]['user1'], text=f"Победили крестики\n{winner_field(matrix)}")
        bot.edit_message_text(chat_id=game[1], message_id=games[game]['user2'], text=f"Победили крестики\n{winner_field(matrix)}")
    elif matrix[0][0] == matrix[0][1] and matrix[0][1] == matrix[0][2] and matrix[0][2] == 1:
        bot.edit_message_text(chat_id=game[0], message_id=games[game]['user1'], text=f"Победили крестики\n{winner_field(matrix)}")
        bot.edit_message_text(chat_id=game[1], message_id=games[game]['user2'], text=f"Победили крестики\n{winner_field(matrix)}")
    elif matrix[2][0] == matrix[2][1] and matrix[2][1] == matrix[2][2] and matrix[2][2] == 1:
        bot.edit_message_text(chat_id=game[0], message_id=games[game]['user1'], text=f"Победили крестики\n{winner_field(matrix)}")
        bot.edit_message_text(chat_id=game[1], message_id=games[game]['user2'], text=f"Победили крестики\n{winner_field(matrix)}")
    elif matrix[1][0] == matrix[1][1] and matrix[1][1] == matrix[1][2] and matrix[1][2] == 0:
        bot.edit_message_text(chat_id=game[0], message_id=games[game]['user1'], text=f"Победили нолики\n{winner_field(matrix)}")
        bot.edit_message_text(chat_id=game[1], message_id=games[game]['user2'], text=f"Победили нолики\n{winner_field(matrix)}")
    elif matrix[0][0] == matrix[0][1] and matrix[0][1] == matrix[0][2] and matrix[0][2] == 0:
        bot.edit_message_text(chat_id=game[0], message_id=games[game]['user1'], text=f"Победили нолики\n{winner_field(matrix)}")
        bot.edit_message_text(chat_id=game[1], message_id=games[game]['user2'], text=f"Победили нолики\n{winner_field(matrix)}")
    elif matrix[2][0] == matrix[2][1] and matrix[2][1] == matrix[2][2] and matrix[2][2] == 0:
        bot.edit_message_text(chat_id=game[0], message_id=games[game]['user1'], text=f"Победили нолики\n{winner_field(matrix)}")
        bot.edit_message_text(chat_id=game[1], message_id=games[game]['user2'], text=f"Победили нолики\n{winner_field(matrix)}")
    elif matrix[0][0] == matrix[1][0] and matrix[1][0] == matrix[2][0] and matrix[2][0] == 1:
        bot.edit_message_text(chat_id=game[0], message_id=games[game]['user1'], text=f"Победили крестики\n{winner_field(matrix)}")
        bot.edit_message_text(chat_id=game[1], message_id=games[game]['user2'], text=f"Победили крестики\n{winner_field(matrix)}")
    elif matrix[0][1] == matrix[1][1] and matrix[1][1] == matrix[2][1] and matrix[2][1] == 1:
        bot.edit_message_text(chat_id=game[0], message_id=games[game]['user1'], text=f"Победили крестики\n{winner_field(matrix)}")
        bot.edit_message_text(chat_id=game[1], message_id=games[game]['user2'], text=f"Победили крестики\n{winner_field(matrix)}")
    elif matrix[0][2] == matrix[1][2] and matrix[1][2] == matrix[2][2] and matrix[2][2] == 1:
        bot.edit_message_text(chat_id=game[0], message_id=games[game]['user1'], text=f"Победили крестики\n{winner_field(matrix)}")
        bot.edit_message_text(chat_id=game[1], message_id=games[game]['user2'], text=f"Победили крестики\n{winner_field(matrix)}")
    elif matrix[0][2] == matrix[1][2] and matrix[1][2] == matrix[2][2] and matrix[2][2] == 0:
        bot.edit_message_text(chat_id=game[0], message_id=games[game]['user1'], text=f"Победили нолики\n{winner_field(matrix)}")
        bot.edit_message_text(chat_id=game[1], message_id=games[game]['user2'], text=f"Победили нолики\n{winner_field(matrix)}")
    elif matrix[0][0] == matrix[1][0] and matrix[1][0] == matrix[2][0] and matrix[2][0] == 0:
        bot.edit_message_text(chat_id=game[0], message_id=games[game]['user1'], text=f"Победили нолики\n{winner_field(matrix)}")
        bot.edit_message_text(chat_id=game[1], message_id=games[game]['user2'], text=f"Победили нолики\n{winner_field(matrix)}")
    elif matrix[0][1] == matrix[1][1] and matrix[1][1] == matrix[2][1] and matrix[2][1] == 0:
        bot.edit_message_text(chat_id=game[0], message_id=games[game]['user1'], text=f"Победили нолики\n{winner_field(matrix)}")
        bot.edit_message_text(chat_id=game[1], message_id=games[game]['user2'], text=f"Победили нолики\n{winner_field(matrix)}")
    elif matrix[0][0] == matrix[1][1] and matrix[1][1] == matrix[2][2] and matrix[2][2] == 1:
        bot.edit_message_text(chat_id=game[0], message_id=games[game]['user1'], text=f"Победили крестики\n{winner_field(matrix)}")
        bot.edit_message_text(chat_id=game[1], message_id=games[game]['user2'], text=f"Победили крестики\n{winner_field(matrix)}")
    elif matrix[0][0] == matrix[1][1] and matrix[1][1] == matrix[2][2] and matrix[2][2] == 0:
        bot.edit_message_text(chat_id=game[0], message_id=games[game]['user1'], text=f"Победили нолики\n{winner_field(matrix)}")
        bot.edit_message_text(chat_id=game[1], message_id=games[game]['user2'], text=f"Победили нолики\n{winner_field(matrix)}")
    elif matrix[0][2] == matrix[1][1] and matrix[1][1] == matrix[2][0] and matrix[2][0] == 1:
        bot.edit_message_text(chat_id=game[0], message_id=games[game]['user1'], text=f"Победили крестики\n{winner_field(matrix)}")
        bot.edit_message_text(chat_id=game[1], message_id=games[game]['user2'], text=f"Победили крестики\n{winner_field(matrix)}")
    elif matrix[0][2] == matrix[1][1] and matrix[1][1] == matrix[2][0] and matrix[2][0] == 0:
        bot.edit_message_text(chat_id=game[0], message_id=games[game]['user1'], text=f"Победили нолики\n{winner_field(matrix)}")
        bot.edit_message_text(chat_id=game[1], message_id=games[game]['user2'], text=f"Победили нолики\n{winner_field(matrix)}")
    else:
        flag = False
        for row in matrix:
            for i in row:
                if i == '':
                    flag = True
                    break
            if flag:
                break
        else:
            print("Ничья")
            bot.edit_message_text(chat_id=game[0], message_id=games[game]['user1'], text=f'Ничья\n{winner_field(matrix)}')
            bot.edit_message_text(chat_id=game[1], message_id=games[game]['user2'], text=f"Ничья\n{winner_field(matrix)}")

# создание 9 кнопок
def generate_markup(b1, b2, b3, b4, b5, b6, b7, b8, b9):
    markup = types.InlineKeyboardMarkup()
    one = types.InlineKeyboardButton(b1, callback_data='btn1')
    two = types.InlineKeyboardButton(b2, callback_data='btn2')
    three = types.InlineKeyboardButton(b3, callback_data='btn3')
    four = types.InlineKeyboardButton(b4, callback_data='btn4')
    five = types.InlineKeyboardButton(b5, callback_data='btn5')
    six = types.InlineKeyboardButton(b6, callback_data='btn6')
    seven = types.InlineKeyboardButton(b7, callback_data='btn7')
    eight = types.InlineKeyboardButton(b8, callback_data='btn8')
    nine = types.InlineKeyboardButton(b9, callback_data='btn9')
    markup.add(one, two, three, four, five, six, seven, eight, nine)
    return markup
# запуск бота
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton("Орел или решка")
    markuptwo = types.KeyboardButton('Крестики нолики')
    blackjack = types.KeyboardButton('Blackjack')
    markup.add(button, markuptwo, blackjack)
    bot.send_message(message.chat.id, "Выбери игру", reply_markup=markup)
    add_user(message)
# запись пользователей из словаря users в файл
    try:
        with open(r"C:\Users\volvas\Downloads\users.txt", mode="w", encoding="UTF-8") as file:
            [print(f'{k}: {v}', file=file) for k,v in users.items()]
            # print(users,file=file)

    except FileNotFoundError:
        print("Не удалось открыть файл, проверьте путь к файлу!")

# отслеживание ходов игроков
@bot.callback_query_handler(func = lambda call: True)
def answer(call):
    global games, users
    print(call)
    for game in games:
        if call.from_user.id in game:
            print(games[game])
            if call.data == 'btn1':
                keyboard = call.message.reply_markup
                if games[game]['turn'] == 'x':
                    new_button = types.InlineKeyboardButton('❌', callback_data='btn3')
                    games[game]['turn'] = '0'
                    games[game]['matrix'][0][0] = 1
                elif games[game]['turn'] == '0':
                    new_button = types.InlineKeyboardButton('⭕️', callback_data='btn3')
                    games[game]['turn'] = 'x'
                    games[game]['matrix'][0][0] = 0
                keyboard.keyboard[0][0] = new_button
                bot.edit_message_reply_markup(chat_id=game[1], message_id=games[game]['user2'], reply_markup=keyboard)
                bot.edit_message_reply_markup(chat_id=game[0], message_id=games[game]['user1'], reply_markup=keyboard)
                print(call.message.chat.id, call.message.message_id)
            elif call.data == 'btn2':
                keyboard = call.message.reply_markup
                if games[game]['turn'] == 'x':
                    new_button = types.InlineKeyboardButton('❌', callback_data='btn3')
                    games[game]['turn'] = '0'
                    games[game]['matrix'][0][1] = 1
                elif games[game]['turn'] == '0':
                    new_button = types.InlineKeyboardButton('⭕️', callback_data='btn3')
                    games[game]['turn'] = 'x'
                    games[game]['matrix'][0][1] = 0
                keyboard.keyboard[0][1] = new_button
                bot.edit_message_reply_markup(chat_id=game[1], message_id=games[game]['user2'], reply_markup=keyboard)
                bot.edit_message_reply_markup(chat_id=game[0], message_id=games[game]['user1'], reply_markup=keyboard)
            elif call.data == 'btn3':
                keyboard = call.message.reply_markup
                if games[game]['turn'] == 'x':
                    new_button = types.InlineKeyboardButton('❌', callback_data='btn3')
                    games[game]['turn'] = '0'
                    games[game]['matrix'][0][2] = 1
                elif games[game]['turn'] == '0':
                    new_button = types.InlineKeyboardButton('⭕️', callback_data='btn3')
                    games[game]['turn'] = 'x'
                    games[game]['matrix'][0][2] = 0
                keyboard.keyboard[0][2] = new_button
                bot.edit_message_reply_markup(chat_id=game[1], message_id=games[game]['user2'], reply_markup=keyboard)
                bot.edit_message_reply_markup(chat_id=game[0], message_id=games[game]['user1'], reply_markup=keyboard)
            elif call.data == 'btn4':
                keyboard = call.message.reply_markup
                if games[game]['turn'] == 'x':
                    new_button = types.InlineKeyboardButton('❌', callback_data='btn3')
                    games[game]['turn'] = '0'
                    games[game]['matrix'][1][0] = 1
                elif games[game]['turn'] == '0':
                    new_button = types.InlineKeyboardButton('⭕️', callback_data='btn3')
                    games[game]['turn'] = 'x'
                    games[game]['matrix'][1][0] = 0
                keyboard.keyboard[1][0] = new_button
                bot.edit_message_reply_markup(chat_id=game[1], message_id=games[game]['user2'], reply_markup=keyboard)
                bot.edit_message_reply_markup(chat_id=game[0], message_id=games[game]['user1'], reply_markup=keyboard)
            elif call.data == 'btn5':
                keyboard = call.message.reply_markup
                if games[game]['turn'] == 'x':
                    new_button = types.InlineKeyboardButton('❌', callback_data='btn3')
                    games[game]['turn'] = '0'
                    games[game]['matrix'][1][1] = 1
                elif games[game]['turn'] == '0':
                    new_button = types.InlineKeyboardButton('⭕️', callback_data='btn3')
                    games[game]['turn'] = 'x'
                    games[game]['matrix'][1][1] = 0
                keyboard.keyboard[1][1] = new_button
                bot.edit_message_reply_markup(chat_id=game[1], message_id=games[game]['user2'], reply_markup=keyboard)
                bot.edit_message_reply_markup(chat_id=game[0], message_id=games[game]['user1'], reply_markup=keyboard)
            elif call.data == 'btn6':
                keyboard = call.message.reply_markup
                if games[game]['turn'] == 'x':
                    new_button = types.InlineKeyboardButton('❌', callback_data='btn3')
                    games[game]['turn'] = '0'
                    games[game]['matrix'][1][2] = 1
                elif games[game]['turn'] == '0':
                    new_button = types.InlineKeyboardButton('⭕️', callback_data='btn3')
                    games[game]['turn'] = 'x'
                    games[game]['matrix'][1][2] = 0
                keyboard.keyboard[1][2] = new_button
                bot.edit_message_reply_markup(chat_id=game[1], message_id=games[game]['user2'], reply_markup=keyboard)
                bot.edit_message_reply_markup(chat_id=game[0], message_id=games[game]['user1'], reply_markup=keyboard)
            elif call.data == 'btn7':
                keyboard = call.message.reply_markup
                if games[game]['turn'] == 'x':
                    new_button = types.InlineKeyboardButton('❌', callback_data='btn3')
                    games[game]['turn'] = '0'
                    games[game]['matrix'][2][0] = 1
                elif games[game]['turn'] == '0':
                    new_button = types.InlineKeyboardButton('⭕️', callback_data='btn3')
                    games[game]['turn'] = 'x'
                    games[game]['matrix'][2][0] = 0
                keyboard.keyboard[2][0] = new_button
                bot.edit_message_reply_markup(chat_id=game[1], message_id=games[game]['user2'], reply_markup=keyboard)
                bot.edit_message_reply_markup(chat_id=game[0], message_id=games[game]['user1'], reply_markup=keyboard)
            elif call.data == 'btn8':
                keyboard = call.message.reply_markup
                if games[game]['turn'] == 'x':
                    new_button = types.InlineKeyboardButton('❌', callback_data='btn3')
                    games[game]['turn'] = '0'
                    games[game]['matrix'][2][1] = 1
                elif games[game]['turn'] == '0':
                    new_button = types.InlineKeyboardButton('⭕️', callback_data='btn3')
                    games[game]['turn'] = 'x'
                    games[game]['matrix'][2][1] = 0
                keyboard.keyboard[2][1] = new_button
                bot.edit_message_reply_markup(chat_id=game[1], message_id=games[game]['user2'], reply_markup=keyboard)
                bot.edit_message_reply_markup(chat_id=game[0], message_id=games[game]['user1'], reply_markup=keyboard)
            elif call.data == 'btn9':
                keyboard = call.message.reply_markup
                if games[game]['turn'] == 'x':
                    new_button = types.InlineKeyboardButton('❌', callback_data='btn3')
                    games[game]['turn'] = '0'
                    games[game]['matrix'][2][2] = 1
                elif games[game]['turn'] == '0':
                    new_button = types.InlineKeyboardButton('⭕️', callback_data='btn3')
                    games[game]['turn'] = 'x'
                    games[game]['matrix'][2][2] = 0
                keyboard.keyboard[2][2] = new_button
                bot.edit_message_reply_markup(chat_id=game[1], message_id=games[game]['user2'], reply_markup=keyboard)
                bot.edit_message_reply_markup(chat_id=game[0], message_id=games[game]['user1'], reply_markup=keyboard)
            win(games[game]['matrix'], call)
            users[game[1]]['status'] = 'не ищет игру'
            users[game[0]]['status'] = 'не ищет игру'

        # bot.send_message(chat_id=call.message.chat.id, text=call.message.reply_markup)

        # bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Пыщь!")


@bot.message_handler(commands=['friends'])
def friends(message):
    bot.send_message(message.chat.id, 'Привет, если мы знакомы напиши код, "Напиши и узнаешь какой код"')






# игра орел и решка
@bot.message_handler(content_types=["text"])
def reply(message):
    # bot.send_message(message.chat.id, message.text)
    global count, botcount, koloda
    if message.text == "Орел или решка":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        orel = types.KeyboardButton("Орел")
        reshka = types.KeyboardButton('Решка')
        markup.add(orel, reshka)
        bot.send_message(message.chat.id,"Выберите сторону",reply_markup=markup)
    elif message.text.lower() == "орел":
        if randint(0,9) %2:
            bot.send_message(message.chat.id,'Увы,ты проиграл, выпала решка')
        else:
            bot.send_message(message.chat.id, 'Поздравляю ты выйграл')
    elif message.text.lower() == "решка":
        if randint(0,9)%2:
            bot.send_message(message.chat.id, 'Увы, ты проиграл, выпал орел')
        else:
            bot.send_message(message.chat.id, "Поздравляю ты выйграл")
    elif message.text.lower() == "крестики нолики":
        bot.send_message(message.chat.id, 'Идет подбор противника')
        users[message.from_user.id]['status'] = 'ищет игру'
        for id in users:
            if users[id]['status'] == 'ищет игру' and id != message.from_user.id:
                users[message.from_user.id]['status'] = 'в игре'
                users[id]['status'] = 'в игре'
                peremena1 = bot.send_message(message.chat.id, 'Ходи', reply_markup=generate_markup('⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️','⬜️'))
                peremena2 = bot.send_message(id, 'Ходи',reply_markup=generate_markup('⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️'))
                games[(message.from_user.id, id)] = {'user1': peremena1.id, 'user2': peremena2.id,
                                                     'firt_turn': message.from_user.id,
                                                     'matrix': [['', '', ''], ['', '', ''], ['', '', '']],
                                                     'turn': 'x'}
                print(users, games)


    elif message.text.lower() == 'blackjack':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        users[message.from_user.id]['current_game'] = 'blackjack'
        no = types.KeyboardButton('Нет не знаю')
        yes = types.KeyboardButton('Знаю')
        markup.add(no, yes)
        bot.send_message(message.chat.id, 'Знаешь правилы игры?', reply_markup=markup)
    elif message.text.lower() == 'нет не знаю':
        bot.send_message(message.chat.id, 'Смотри тебе выпадает число "карта" и ты должен собрать 21 очко, если больше, то ты автоматически проиграл, если не собрал, то подсчитавается количество очков у игрокa и у кого больше тот и выйгравает (Игра идет с ботом)')
    elif message.text.lower() == 'знаю':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        go = types.KeyboardButton('Погнали')
        markup.add(go)
        bot.send_message(message.chat.id, "Хорошо, тебе предстоит сыграть с ботом, надеюсь ты победишь, погнали?", reply_markup=markup)
    elif message.text.lower() == 'погнали':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        da = types.KeyboardButton('Да')
        ne = types.KeyboardButton('Хватит')
        # repeat = types.KeyboardButton('Ну давай')
        markup.add(da, ne)
        bot.send_message(message.chat.id, 'Будете брать карту?', reply_markup=markup)
    elif message.text.lower() == 'да':
        # markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        current = koloda.pop()
        botcurrent = koloda.pop()
        print(f'Боту попалась карта достоинства {botcurrent}')
        users[message.chat.id]['count'] += current
        users[message.chat.id]["botcount"] += botcurrent
        bot.send_message(message.chat.id, f'Вам попалась карта достоинства {current}\nТвое количество очков:  {users[message.chat.id]["count"]}')
        if users[message.chat.id]['count'] == 21:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, f'Поздравляю, у бота было {users[message.chat.id]["botcount"]} ')
            repeat = types.KeyboardButton('Ну давай')
            markup.add(repeat)
            bot.send_message(message.chat.id, 'хочешь еще раз?', reply_markup=markup)
            users[message.chat.id]['count'] = 0
            users[message.chat.id]["botcount"] = 0
            koloda = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
            random.shuffle(koloda)
        elif users[message.chat.id]["botcount"] == 21:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, f'Поздравляю, у бота было {users[message.chat.id]["botcount"]} ')
            repeat = types.KeyboardButton('Ну давай')
            markup.add(repeat)
            bot.send_message(message.chat.id, 'хочешь еще раз?', reply_markup=markup)
            users[message.chat.id]['count'] = 0
            users[message.chat.id]["botcount"] = 0
            koloda = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
            random.shuffle(koloda)
        elif users[message.chat.id]['count'] > 21:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, f'К сожелению вы проиграли у вас {users[message.chat.id]["count"]} очков')
            repeat = types.KeyboardButton('Ну давай')
            markup.add(repeat)
            bot.send_message(message.chat.id, 'хочешь еще раз?', reply_markup=markup)
            users[message.chat.id]['count'] = 0
            users[message.chat.id]["botcount"] = 0
            koloda = [1,2,3,4,5,6,7,8,9,10,11]
            random.shuffle(koloda)
        elif users[message.chat.id]["botcount"] > 21:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, f'Поздравляю вы выйграли, у бота {users[message.chat.id]["botcount"]} Очков')
            repeat = types.KeyboardButton('Ну давай')
            markup.add(repeat)
            bot.send_message(message.chat.id, 'хочешь еще раз?', reply_markup=markup)
            users[message.chat.id]['count'] = 0
            users[message.chat.id]["botcount"] = 0
            koloda = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
            random.shuffle(koloda)
    elif message.text.lower() == 'хватит':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        if users[message.chat.id]['count'] < users[message.chat.id]["botcount"]:
            bot.send_message(message.chat.id, f'К сожелению вы проиграли у бота {users[message.chat.id]["botcount"]} очков')
            koloda = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
            random.shuffle(koloda)
        elif users[message.chat.id]['count'] > users[message.chat.id]["botcount"]:
            bot.send_message(message.chat.id, f'Поздравляю вы выйграли, у бота {users[message.chat.id]["botcount"]} Очков')
        repeat = types.KeyboardButton('Ну давай')
        markup.add(repeat)
        bot.send_message(message.chat.id, 'хочешь еще раз?', reply_markup=markup)
        koloda = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        random.shuffle(koloda)
    elif message.text.lower() == 'ну давай':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        da = types.KeyboardButton('Да')
        ne = types.KeyboardButton('Хватит')
        markup.add(da, ne)
        users[message.chat.id]['count'] = 0
        users[message.chat.id]["botcount"] = 0
        koloda = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        random.shuffle(koloda)
        current = koloda.pop()
        botcurrent = koloda.pop()
        print(f'Боту попалась карта достоинства {botcurrent}')
        users[message.chat.id]['count'] += current
        users[message.chat.id]["botcount"] += botcurrent
        bot.send_message(message.chat.id, f'Вам попалась карта достоинства {current}\nТвое количество очков:  {users[message.chat.id]["count"]}', reply_markup=markup)

    elif message.text.lower() == 'хватит':
        if users[message.chat.id]['count'] < users[message.chat.id]["botcount"]:
            bot.send_message(message.chat.id, f'К сожелению вы проиграли у бота {users[message.chat.id]["botcount"]} очков')
            users[message.chat.id]['count'] = 0
            users[message.chat.id]["botcount"] = 0
            koloda = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
            random.shuffle(koloda)
        elif users[message.chat.id]['count'] > users[message.chat.id]["botcount"]:
            bot.send_message(message.chat.id, f'Поздравляю вы выйграли, у бота {users[message.chat.id]["botcount"]} Очков')
            users[message.chat.id]['count'] = 0
            users[message.chat.id]["botcount"] = 0
            koloda = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
            random.shuffle(koloda)
        if users[message.chat.id]['count'] == 21:
            bot.send_message(message.chat.id, f'Поздравляю, у бота было {users[message.chat.id]["botcount"]} ')
            users[message.chat.id]['count'] = 0
            users[message.chat.id]["botcount"] = 0
            koloda = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
            random.shuffle(koloda)
        elif users[message.chat.id]["botcount"] == 21:
            bot.send_message(message.chat.id, 'К сожелению бот вас выйграл, у него 21 очко')
            users[message.chat.id]['count'] = 0
            users[message.chat.id]["botcount"] = 0
            koloda = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
            random.shuffle(koloda)
        elif users[message.chat.id]['count'] > 21:
            bot.send_message(message.chat.id, f'К сожелению вы проиграли у вас {users[message.chat.id]["count"]} очков')
            users[message.chat.id]['count'] = 0
            users[message.chat.id]["botcount"] = 0
            koloda = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
            random.shuffle(koloda)
        elif users[message.chat.id]["botcount"] > 21:
            bot.send_message(message.chat.id, f'Поздравляю вы выйграли, у бота {users[message.chat.id]["botcount"]} Очков')
            users[message.chat.id]['count'] = 0
            users[message.chat.id]["botcount"] = 0
            koloda = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
            random.shuffle(koloda)
    #                   s = randint(0.100)
    #                   s < 70:


# bot.send_message(message.chat.id, "Привет")
#
# @bot.callback_query_handler(func=lambda c: c.data == 'btn2')
# def btn2(message):
#     print(message)
# @bot.message_handler(content_types=['text'])
# def echo(message):
#     bot.send_message(message.chat.id, message.text)
# generate_markup('❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌'))
# keyboard = call.message.reply_markup
        # new_button = types.InlineKeyboardButton('❌', callback_data='btn3')
        # keyboard.keyboard[0][1] = new_button
        # bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=keyboard)
    # markup = types.InlineKeyboardMarkup()
    # a = types.InlineKeyboardButton("Привет друг",callback_data='btn2')
    # markup.add(a)
    # bot.send_message(message.chat.id, 'Напиши код', reply_markup=markup)
bot.polling(none_stop=True)