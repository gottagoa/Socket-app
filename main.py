import socket

def generate_response(request):
    pass



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
# обхение между клиентом и сервером долгосрочные отношения, поэтому необходимо постоянно обьновлять связи
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
        client_socket.sendall('hello world'.encode())
        # сокеты не принимают строки-только байты
        client_socket.close()
        # в браузере нельзя увидеть ответ, пока не закрыт соелинение



if __name__=='__main__':
    run()