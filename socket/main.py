import socket
from views import index, blog

URLS={
    '/':index,
    '/blog':blog
}

def parse_request(request):
    parsed=request.split(' ')
    method=parsed[0]
    url=parsed[1]
    return (method, url)


def generate_headers(method, url):
    if not method=='GET':
        return ('HTTP/1.1 405 Method not allowed\n\n', 405)
    if not url in URLS:
        return ('HTTP/1.1 404 Not found\n\n', 404)
    
    return ('HTTP/1.1 200 OK\n\n', 200)
    

def generate_content(code, url):
    if code==404:
        return '<h1>404</h1>Not found<p></p>'
    if code==405:
        return '<h1>404</h1>Method is not allowed<p></p>'
    return URLS[url]()


def generate_response(request):
    # необходимо распарсить request, который был получен в функции run()
    method, url=parse_request(request)
    # ответ клиенту-заголовок и тело текста
    headers, code= generate_headers(method, url)
    body=generate_content(code, url)
    # генерация тела ответа
    # функция generate_headers будет заниматься генерацией статуса кода
    return (headers+'hello world').encode()


def run():
# создает объект, принимающий запрос
    server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # перед вызовом bind необходимо использовать setsockpot, чтобы порт постоянно 
    # не был занят и не тратил 1,5 минуты на восстановление
    # он принимает три аргумента- socket.SOL_SOCKET(говорит что слушает именно наш сокет), socket.SO_REUSEADDR-можем его переисопльзовать адрес и 1-True
# связать этот объект (server_socket) с конкретным адресом и портом
    server_socket.bind(('localhost', 8000))
    # пинимает кортеж-адрес и порт
    # необходимо теперь ему дать указание прослушивать этот порт и ждать пакеты данных
    server_socket.listen()
# общение между клиентом и сервером долгосрочные отношения, поэтому необходимо постоянно обьновлять связи
    # поэтому используется бесконечный цикл
    while True:
        # например, сервер получил ответ и мы хотим его посмотреть
        client_socket, addr=server_socket.accept()
        # возвращает кортеж
        # client_socket-клиент, который отправляет запрос по адресу addr. система сама задаст его адрес
        request=client_socket.recv(1024)
        # 1024-еоличество байтов
        print(request.decode('utf-8'))

        response=generate_response(request.decode('utf-8'))
# после получения запроса необходимо ответить клиенту
        client_socket.sendall(response)
        # сокеты не принимают строки-только байты
        client_socket.close()
        # в браузере нельзя увидеть ответ, пока не закрыт соелинение


if __name__=='__main__':
    run()