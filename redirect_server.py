from http.server import HTTPServer, BaseHTTPRequestHanler

class RedirectHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(302)
            self.send_header('Location', '/new-page.html')
            self.end_headers()
        elif self.path == "/new-page.html":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"<h1>You have been redirected (Real 302)!</h1>")
        else:
            self.send_error(404, "Not Found")

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, RedirectHandler)
    print("Serving on http://localhost:8000")
    httpd.serve_forever()
