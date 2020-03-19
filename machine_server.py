from http.server import BaseHTTPRequestHandler

class GetHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        cardid = self.path
        if len(cardid) > 0:
          cardid = cardid[1:]
        message = 'OK:'+cardid
        self.send_response(200)
        self.send_header('Content-Type',
                         'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(message.encode('utf-8'))

if __name__ == '__main__':
    from http.server import HTTPServer
    server = HTTPServer(('0.0.0.0', 7777), GetHandler)
    print('Starting server, use <Ctrl-C> to stop')
    server.serve_forever()
