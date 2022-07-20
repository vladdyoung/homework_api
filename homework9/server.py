import socket


# Server
def server_start():
    server = socket.socket()  # сокет
    server.bind(('localhost', 8883))  # тут картеж
    server.listen(4)  # сервер слушает до 4 подключений

    #  цикл на непрерывной прием сообщений от клиента
    while True:
        client_connect, server_port = server.accept()  # открывает соединение, порт
        client_data = client_connect.recv(1024).decode('utf-8')  # получает данные от клиента
        lines = client_data.split('\r\n')  # список из хедеров запроса клиента
        lines_list = []  # наполнение списка списком строк с заголовками
        headers_list = []  #
        status_row = lines[0]  # строка GET/200%20ОК HTTP 1.1/
        # вытаскивает из строки GET/200%20ОК HTTP 1.1/: метод, статус код, протокол
        method, status_code, protocol = status_row.split(' ')

        # получение списка без GET/HTTP 1.1/  и пустых строк
        for line in lines:
            if 'GET' in line or len(line) == 0:
                continue
            else:
                lines_list.append(line)  # получаем список без GET/HTTP 1.1/  и пустых строк

        # формирование списка заголовков для вывода на экран браузера
        for header in lines_list:
            header = header.split(':')
            headers_list.append(header[0]+':'+':'.join(header[1:]))

        # передача статус кода в респонс клиенту
        if status_code == '/':
            response_status = '200 OK'
        else:
            response_status = status_code[1:].replace('%20', ' ')

        # формирование ответа клинту
        # респонс сервера (выставляю сам)
        hdrs = f'{protocol} {response_status}\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
        # строки HTML
        method_answer = f'Request Method: {method} '  # ответ метод запроса от клиента
        server_adress_and_port_answer = f'Request Source: {server_port} '  # ответ адрес и порт клиента
        response_status_answer = f'Response Status: {response_status} '  # ответ статус код
        headers_list_to_str = ', '.join(headers_list)  # список заголовков в виде строки

        # отправка ответа клиенту
        client_connect.send(hdrs.encode('utf-8') + (method_answer + '<br>'
                                                    + server_adress_and_port_answer + '<br>'
                                                    + response_status_answer + '<br>'
                                                    + headers_list_to_str).encode('utf-8'))
        client_connect.close()


if __name__ == '__main__':
    server_start()
