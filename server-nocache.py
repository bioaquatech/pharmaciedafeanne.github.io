from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

class NoCacheHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

os.chdir('.')
server = HTTPServer(('127.0.0.1', 3000), NoCacheHandler)
print('✅ Serveur lancé sur http://127.0.0.1:3000 (SANS CACHE)')
server.serve_forever()
