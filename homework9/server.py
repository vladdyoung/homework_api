import socket


def server_start():
    server = socket.socket()
    server.bind(('localhost', 8883))
    server.listen(4)
    while True:
        client_connect, server_port = server.accept()
        client_data = client_connect.recv(1024).decode('utf-8')
        lines = client_data.split('\r\n')
        lines_list = []
        headers_list = []
        status_row = lines[0]
        method, status_code, protocol = status_row.split(' ')
        for line in lines:
            if 'GET' in line or len(line) == 0:
                continue
            else:
                lines_list.append(line)
        for header in lines_list:
            header = header.split(':')
            headers_list.append(header[0]+':'+':'.join(header[1:]))
        if status_code == '/':
            response_status = '200 OK'
        else:
            response_status = status_code[1:].replace('%20', ' ')
        hdrs = f'{protocol} {response_status}\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
        method_answer = f'Request Method: {method} '
        server_adress_and_port_answer = f'Request Source: {server_port} '
        response_status_answer = f'Response Status: {response_status} '
        headers_list_to_str = ', '.join(headers_list)
        client_connect.send(hdrs.encode('utf-8') + (method_answer + '<br>'
                                                    + server_adress_and_port_answer + '<br>'
                                                    + response_status_answer + '<br>'
                                                    + headers_list_to_str).encode('utf-8'))
        client_connect.close()


if __name__ == '__main__':
    server_start()
