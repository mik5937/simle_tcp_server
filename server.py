import logging
import re
import socket

# создаемTCP/IP сокет
sock = socket.socket()

# Привязываем сокет к порту
server_address = ('localhost', 15000)
print('Сервер запущен на {} порт {}'.format(*server_address))
sock.bind(server_address)

# Слушаем входящие подключения
sock.listen(1)

string = ''

logging.basicConfig(filename="data.log", level=logging.INFO)
while True:
    print('Ждем подключение клиента...')
    connection, client_address = sock.accept()
    try:
        print('Связь установлена с:', client_address)
        while data := connection.recv(4096).decode("utf-8"):
            records = f'{string}{data}'.split('\n')
            for record in records:
                if len(record) == 23:
                    bbbb, nn, hh, mm, ss_zsh, gg = re.split(' |:', record)
                    if gg == '00':
                        print(f'cпортсмен, нагрудный номер {bbbb} прошёл отсечку {nn} в «{hh}:{mm}:{ss_zsh[:4]}»')
                    logging.info(record)
                else:
                    string = record

    except ValueError:
        connection.close()
        logging.info('ValueError. Connection close.')