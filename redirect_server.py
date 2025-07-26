from http.server import HTTPServer, BaseHTTPRequestHandler

class RedirectHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            # Redirect to /new-page.html
            self.send_response(302)
            self.send_header('Location', '/new-page.html')
            self.end_headers()

        elif self.path == "/new-page.html":
            # Successful response page
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"<h1>You have been redirected (Real 302)!</h1>")

        elif self.path == "/cause-error":
            # Simulated server-side error
            try:
                # Trigger intentional error (division by zero)
                1 / 0
            except Exception as e:
                self.send_response(500)
                self.send_header("Content-Type", "text/html")
                self.end_headers()
                error_html = f"""
                <html>
                <head><title>500 Internal Server Error</title></head>
                <body>
                    <h1>500 Internal Server Error</h1>
                    <p>{str(e)}</p>
                </body>
                </html>
                """.encode()
                self.wfile.write(error_html)

        else:
            # 404 Not Found
            self.send_error(404, "Not Found")

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, RedirectHandler)
    print("🚀 Serving on http://localhost:8000")
    httpd.serve_forever()
