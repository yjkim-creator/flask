from wsgiref.simple_server import make_server

def application(environ, start_response):
    response_body="Hello Python Web"
    status = '200 OK'

    response_headers=[('Content-Type', 'text/plain'),
                        ('Content-Length', str(len(response_body)))]
    start_response(status, response_headers)
    return [response_body.encode('utf-8')]

httpd = make_server('localhost', 5000 , application)


print('server start : http://127.0.0.1:5000')
httpd.handle_request()