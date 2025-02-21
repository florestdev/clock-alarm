from os import environ, chdir
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import time
from pygame import mixer
import pathlib, sys
from colorama import Fore

chdir(pathlib.Path(sys.argv[0]).parent.resolve())
mixer.init()
running = True

def set_alarm(time_to_ring):
    """Устанавливает будильник на указанное время"""
    # Преобразуем строку в формат времени
    alarm_time = time.strptime(time_to_ring, "%H:%M:%S")
    hour = alarm_time.tm_hour
    minutes = alarm_time.tm_min
    seconds = alarm_time.tm_sec
    data = {'hour':hour, 'minutes':minutes, 'seconds':seconds}
    print(f'{Fore.GREEN}Будильник установлен на {Fore.MAGENTA}{time_to_ring}')
    while running:
        # Получаем текущее время
        current_time = time.localtime()
        hour_ = current_time.tm_hour
        minutes_ = current_time.tm_min
        seconds_ = current_time.tm_sec
        
        # Проверяем, наступило ли время будильника
        if {'hour':hour_, 'minutes':minutes_, 'seconds':seconds_} == data:
            mixer.Sound('alarm.mp3').play()
        else:
            pass

# Пример использования
set_alarm(input(f'Введите время запуска будильника в формате ЧЧ:ММ:СС : '))