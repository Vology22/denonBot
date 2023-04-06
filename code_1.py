import telebot
import os

f = open('base.txt', 'a') # база данных пользовалей, которые использовали бота
glent = True #переключатель. Хуйня, чтобы не повторять приветствие
password = None #введен ли пароль


bot = telebot.TeleBot('6052432461:AAFSNbxkJtb3-jGZc52PCumHjR2cYpOi350'); #токен бота

#region начальная часть бота, работающая без логирования пользователя 
@bot.message_handler(commands=["start", "begin", "начать"])
def begin(message):
  bot.send_message(message.from_user.id, "Для начала тебе стоит ввести свое имя и кодовое слово, друг мой \n /get_nickname")

@bot.message_handler(commands=["help"])
def help(message):
  if not password:
      bot.send_message(message.from_user.id, "Авторизируйся, Путник \n /get_nickname")

  else:
      bot.send_message(message.from_user.id,  name, ', а теперь произнеси ссылку ВК / номер телефона / почту / ФИО / Серия и номер паспорта');
#endregion

#region про авторизацию пользователя
@bot.message_handler(commands=["get_nickname"])
def get_name(message): 
  global password
  if not password:
    global glent
    if glent:
      bot.send_message(message.from_user.id, 'Произнеси своё имя, Путник, а после используй /get_password'); #Приветствие нужно, чтобы тупо было, и было известно, кто пользовался ботом :D
      bot.register_next_step_handler(message, get_namee);
      
  
@bot.message_handler(commands=["get_password"])
def get_namee(message): #Пароль от всяких пидоров, которые захуячат нашего бота
    global password
    if not password:
      global name
      name = message.text;
      f.write("{}\n".format(name))
      glent = None
      f.close()
      bot.send_message(message.from_user.id, 'Произнеси кодовое слово');
      bot.register_next_step_handler(message, get_password);
  
def get_password(message): #пароль
  global password
  if message.text == '12345098765Op' and password != True:
    password = True
    bot.send_message(message.from_user.id, password)
    bot.register_next_step_handler(message, get_deanon);
    bot.send_message(message.from_user.id, "Кинь ссылку ВК \nномер телефона \nпочту \nФИО \nСерия и номер паспорта")

#endregion

def get_deanon(message):#деанон
  global password
  print ("Робит");
  if password:
    bot.register_next_step_handler(message, get_deanon_go);
    bot.polling(none_stop=True, interval=0)
  else:
    bot.send_message(message.from_user.id, "Тебе нужно сначала ввести пароль. /start")

def get_deanon_go(message):#поиск инфы
  file=open('WB.csv','r') #база данных WB
  text=file.read()
  if message in text:
    print ('этот пароль есть в базе')
    bot.send_message(message.from_user.id, "Эта информация есть в базе данных!")
  else:
    print ('пароля нет в базе')
    bot.send_message(message.from_user.id, "Этой информации нет в базе данных!")
    bot.register_next_step_handler(message, get_deanon);
  file.close()

@bot.message_handler()
def AntiChes(message):
  bot.send_message(message.from_user.id, "Нет такого решения задачи. /help")

bot.polling(none_stop=True, interval=0)


