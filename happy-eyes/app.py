from plyer import notification
from playsound import playsound
import time


def send_notification():
	notification.notify(title='Time for some eye rest.', message='Look elsewhere for 20 seconds', app_name='Twenty', app_icon='eye.ico', timeout=20, ticker='', toast=False)


def soundplay():
	playsound('alert.mp3')


while True:
	soundplay()
	send_notification()
	time.sleep(20)
	soundplay()
	time.sleep(1200)
