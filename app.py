# coding=utf-8
import json
import sys
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

from ant import calc_available_field


class HandleRequests(BaseHTTPRequestHandler):
    """ Обработчик запросов web-сервера """

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        with open('templates/index.html') as f:
            file = f.read()

        self.wfile.write(file)

    def do_POST(self):
        # Получаем данные из запроса
        content_len = int(self.headers.getheader('content-length', 0))
        content = self.rfile.read(content_len)
        body = json.loads(content)

        # рассчитываем карту
        data = calc_available_field(
            x=int(body['x']),
            y=int(body['y']),
            max_sum=int(body['max_sum']),
        )

        # отправляем ответ
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        self.wfile.write(json.dumps(data, encoding='utf-8'))


if __name__ == '__main__':
    HOST_NAME = '0.0.0.0'
    PORT = 8080
    server = HTTPServer((HOST_NAME, PORT), HandleRequests)
    print "Server started http://{HOST_NAME}:{PORT}".format(HOST_NAME=HOST_NAME, PORT=PORT)

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
        sys.exit(0)
