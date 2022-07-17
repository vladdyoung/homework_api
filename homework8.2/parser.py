import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from csv import DictWriter
import datetime

try:
    browser = webdriver.Chrome()
    browser.get('https://www.tutorialspoint.com/unix_terminal_online.php')
    browser.implicitly_wait(3)
    terminal = browser.find_element(By.CSS_SELECTOR, '#terminal textarea.ace_text-input')
    time.sleep(1)
    terminal.send_keys('python')
    terminal.send_keys(Keys.ENTER)
    time.sleep(1)
    terminal.send_keys('import subprocess')
    terminal.send_keys(Keys.ENTER)
    time.sleep(1)
    terminal.send_keys('subprocess.call(["ps", "aux"])')
    terminal.send_keys(Keys.ENTER)
    time.sleep(2)
    terminal.send_keys(Keys.PAGE_UP)
    terminal.send_keys(Keys.PAGE_UP)
    terminal.send_keys(Keys.PAGE_UP)
    time.sleep(5)

    #  получаем верхнюю часть текста из терминала
    response1 = browser.find_element(By.CSS_SELECTOR, '#terminal .ace_content').text
    terminal.send_keys(Keys.PAGE_DOWN)
    terminal.send_keys(Keys.PAGE_DOWN)
    terminal.send_keys(Keys.PAGE_DOWN)
    time.sleep(5)

    #  получаем нижнюю часть текста из терминала
    response2 = browser.find_element(By.CSS_SELECTOR, '#terminal .ace_content').text

    #  получаем общий текст терминала
    response = '{0}\n{1}'.format(response1, response2)

    #  превращем тест из терминала в список
    response_in_list = response.split('\n')

    #  убираем лишнее из списка
    response_in_list = response_in_list[9:]
    response_in_list = response_in_list[::-1]
    response_in_list = response_in_list[2::]
    response_in_list = response_in_list[::-1]

    spisok_slovarey = []

    USER = []
    MEM = []
    CPU = []
    count_mem = 0.0
    max_mem = str()
    count_cpu = 0.0
    max_cpu = str()

    #  приводим к виду CSV, удаляем пробелы
    for element_of_response_in_list in response_in_list:
        element_of_response_in_list = element_of_response_in_list.replace('    ', ' ')
        element_of_response_in_list = element_of_response_in_list.replace('   ', ' ')
        element_of_response_in_list = element_of_response_in_list.replace('  ', ' ')
        #  разделяем запятой
        spisok = element_of_response_in_list.split(' ')
        #  создаем словарь из списка
        slovar = {'USER': spisok[0], 'PID': spisok[1], '%CPU': float(spisok[2]), '%MEM': float(spisok[3]), 'VSZ': spisok[4],
                  'RSS': spisok[5], 'TTY': spisok[6], 'STAT': spisok[7], 'START': spisok[8],
                  'TIME': spisok[9], 'COMMAND': spisok[10]}

        spisok_slovarey.append(slovar)

        # Пользователи системы
        if slovar.get('USER') not in USER:
            USER.append(slovar.get('USER'))
        # Память
        MEM.append(slovar.get('%MEM'))
        # Команда макс использующая память
        if slovar.get('%MEM') > count_mem:
            count_mem = slovar.get('%MEM')
            max_mem = slovar.get('COMMAND')
        # CPU
        CPU.append(slovar.get('%CPU'))
        if slovar.get('%CPU') > count_cpu:
            count_cpu = slovar.get('%CPU')
            max_cpu = slovar.get('COMMAND')

    #  запись в файл.csv
    with open("otus.csv", "w") as file:
        fieldnames = ['USER', 'PID', '%CPU', '%MEM', 'VSZ', 'RSS', 'TTY', 'STAT', 'START', 'TIME', 'COMMAND']
        writer = DictWriter(file, fieldnames=fieldnames, lineterminator='\n')  # lineterminator убирает пустые строки
        writer.writeheader()
        for element in spisok_slovarey:
            writer.writerow(element)

finally:
    browser.close()

print('Отчет о состоянии системы:\n'
      'Пользователи системы:', *USER)
print(f'Процессов запущено: {len(spisok_slovarey)}\n'
      f'Пользовательских процессов: {len(spisok_slovarey)}\n'
      f'Всего памяти используется: {sum(MEM)}\n'
      f'Всего CPU используется: {round(sum(CPU), 2)}\n'
      f'Больше всего памяти использует: {max_mem}\n'
      f'Больше всего CPU использует: {max_cpu}\n')

answer = 'Отчет о состоянии системы:\n', f'Пользователи системы: ', *USER, '\n', \
      f'Процессов запущено:' \
      f' {len(spisok_slovarey)}\n',\
      f'Пользовательских процессов: {len(spisok_slovarey)}\n',\
      f'Всего памяти используется: {sum(MEM)} mb\n',\
      f'Всего CPU используется: {sum(CPU)}\n',\
      f'Больше всего памяти использует: {max_mem}\n',\
      f'Больше всего CPU использует: {max_cpu}\n'

current_data = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

with open(f'{current_data}-scan.txt', 'w') as file:
    for item in answer:
        file.write("%s" % item)

