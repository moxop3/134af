import vk_api
from vk_api.longpoll import  VkLongPoll,VkEventType
import random
import datetime
import time
import requests
from bs4 import BeautifulSoup

token = "fd104c1936388b967932a3ef1cc18fd96d6c4bc77644a8124049394b7390c0ef00315b6cc8dc2d0ad80b6"
vk_session = vk_api.VkApi(token=token) # Токен вк
vk = vk_session.get_api()
longpoll= VkLongPoll(vk_session)
convert = "Для того, чтобы перевести фаренгейты в градусы\nИспользуйте команду конверт x\nx-кол-во градусов по фаренгейту"
privetstvue = ["Привет","Здравствуй","Приветствую","Хай","Хеллоу","Йо","Бонжур","Салам","Вотс ап","Hi","Szia","Ola","Hola","Salve","Hallo","Hæ"]

def message(text,noLinks=0):
	if event.from_user:
		randomidd = random.randint(0,100000)
		vk.messages.send(
			user_id=event.user_id,
			random_id=event.message_id,
			message=str(text),
			dont_parse_links = noLinks,
			peer_id=event.peer_id
	)
	elif event.from_chat:
		vk.messages.send(
			random_id=event.message_id,
			chat_id=event.chat_id,
			message=str(text),
			peer_id=event.peer_id
	)




while True:
	for event in longpoll.listen():
		if event.type == VkEventType.MESSAGE_NEW:
			text = event.text.lower()
			user_id=int(event.user_id)
			if text == "привет":
				us=str(vk.users.get(user_id=user_id)[0]['first_name'])
				time.sleep(2)
				message(random.choice(privetstvue)+", " +us + '.')
			elif text == "расписание":
				date = datetime.datetime.today().isoweekday()
				if date == 1: 
					vk.messages.send(user_id=event.user_id,random_id=event.random_id,peer_id=event.peer_id,message="Расписание на понедельник:",attachment="photo388910540_457264536")
				elif date == 2:
					vk.messages.send(user_id=event.user_id,random_id=event.random_id,peer_id=event.peer_id,message="Расписание на вторник:",attachment="photo388910540_457264535")
				elif date == 3:
					vk.messages.send(user_id=event.user_id,random_id=event.random_id,peer_id=event.peer_id,message="Расписание на среду:",attachment="photo388910540_457264534")
				elif date == 4:
					vk.messages.send(user_id=event.user_id,random_id=event.random_id,peer_id=event.peer_id,message="Расписание на четверг:",attachment="photo388910540_457264533")
				elif date == 5:
					vk.messages.send(user_id=event.user_id,random_id=event.random_id,peer_id=event.peer_id,message="Расписание на пятницу:",attachment="photo388910540_457264532")
				elif date == 6:
					message("Сегодня мы не учимся =)")
				elif date == 7:
					message("Совсем что-ли?\nЩас бы в воскресенье учится..")
			elif  text == "пока":
				us=str(vk.users.get(user_id=user_id)[0]['first_name'])
				message('Пока, '+us + '.')
				time.sleep(2)
			elif text == "рандом":
				rand = random.randint(0,100)
				time.sleep(2)
				message("Ваше рандомное число - "+str(rand))
			elif text == "погода":
				url = "https://yandex.ru/pogoda/nizhnevartovsk"
				source = requests.get(url)
				main_text = source.text
				soup = BeautifulSoup(main_text)
				div = soup.find('div',{'class':'fact__hour-temp'})
				celsius = div.text
				voshod = soup.find('div',{'class':'sun-card__sunrise-sunset-info sun-card__sunrise-sunset-info_value_rise-time'})
				voshod = voshod.text
				voshod = voshod[6:]
				zakat = soup.find('div',{'class':'sun-card__sunrise-sunset-info sun-card__sunrise-sunset-info_value_set-time'})
				zakat = zakat.text
				zakat = zakat[5:]
				dlunadnya = soup.find('div',{'class':'sun-card__day-duration-value'})
				dlunadnya = dlunadnya.text
				yavlenue = soup.find('div', {'class': 'link__condition day-anchor i-bem'})
				yavlenue = yavlenue.text
				vlaznost = soup.find('div', {'class': 'term term_orient_v fact__humidity'})
				vlaznost = vlaznost.text
				veter = soup.find('div', {'class': 'term term_orient_v fact__wind-speed'})
				veter = veter.text
				komfort = soup.find('div', {'class': 'term term_orient_h fact__feels-like'})
				komfort = komfort.text
				komfort = komfort[13:]
				time.sleep(2)
				message("🌍В Нижневартовске сейчас "+celsius+"🌍\n❄Комфорт "+komfort+"❄\n💧Влажность воздуха "+vlaznost+"💧\n☁Сейчас на улице "+yavlenue+"☁\n🌪Скорость ветра "+veter+"🌪\n🌕Длина дня "+dlunadnya+"🌕\n🌖Восход в "+voshod+"🌖\n🌒Ззакат "+zakat+"🌒")
			elif text == "цитата":
				print(requests.post("https://randstuff.ru/saying/generate/",headers = {'Accept-Language':'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 'Connection':'keep-alive', 'Host':'randstuff.ru', 'origin':'https://randstuff.ru','Referer':'https://randstuff.ru/saying/'}))
				url = "https://randstuff.ru/saying/"
				source = requests.get(url)
				main_text = source.text
				soup = BeautifulSoup(main_text)
				cutata = soup.find('table', {'class': 'text'})
				cutata = cutata.text
				time.sleep(2)
				message("⚠"+cutata+"⚠")
			elif text == "факт":
				print(requests.post("https://randstuff.ru/fact/",
									headers={'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
											 'Connection': 'keep-alive', 'Host': 'randstuff.ru',
											 'origin': 'https://randstuff.ru',
											 'Referer': 'https://randstuff.ru/fact/'}))
				url = "https://randstuff.ru/fact/"
				source = requests.get(url)
				main_text = source.text
				soup = BeautifulSoup(main_text)
				fakt = soup.find('table', {'class': 'text'})
				fakt = fakt.text
				time.sleep(2)
				message("⚠" + fakt + "⚠")
			elif text == "курс":
				url = "https://cbr.ru/"
				source = requests.get(url)
				main_text = source.text
				soup = BeautifulSoup(main_text)
				usd = soup.findAll('div', {'class': 'col-md-2 col-xs-9 _right mono-num'})
				euro = soup.findAll('div', {'class': 'col-md-2 col-xs-9 _right mono-num'})
				data = soup.findAll('div', {'class': 'col-md-2 col-xs-7 _right'})
				data = data[1].text
				usd = usd[1].text
				euro = euro[3].text
				message("💵Курс доллара - "+usd+"💶Курс евро - "+euro+"📅"+data[5:])


