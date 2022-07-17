import socket


def server_start():
    server = socket.socket()
    server.bind(('localhost', 8883))  # тут картеж
    server.listen(4)
    while True:
        client_connect, server_port = server.accept()
        client_data = client_connect.recv(1024).decode('utf-8')  # получаю данные от клиента
        lines = client_data.split('\r\n')
        lines_list = []  # наполнение списка списком строк с заголовками
        headers_dict = {}
        status_row = lines[0]
        method, status_code, protocol = status_row.split(' ')

        for line in lines:
            if 'GET' in line or len(line) == 0:
                continue
            else:
                lines_list.append(line)  # получаем список без GET/HTTP 1.1/  и пустых строк
        for header in lines_list:
            header = header.split(':')
            headers_dict[header[0]] = ':'.join(header[1:])

        if status_code == '/':
            response_status = '200 OK'
        else:
            response_status = status_code[1:].replace('%20', ' ')

        HDRS = f'{protocol} {response_status}\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'  # респонс сервера (выставляю сам)
        method_answer = f'Request Method: {method} '
        server_adress_and_port_answer = f'Request Source: {server_port} '
        response_status_answer = f'Response Status: {response_status} '
        # server_answer = '\n'.join(list(headers_dict))  # ответ сервера
        # headers_dict = headers_dict.items()  # заголовки запроса от клиента
        server_answer_headers = headers_dict  # ответ сервера

        client_connect.send(HDRS.encode('utf-8') + (method_answer
                                                    + server_adress_and_port_answer
                                                    + response_status_answer
                                                    + server_answer_headers).encode('utf-8'))
        client_connect.close()


if __name__ == '__main__':
    server_start()
