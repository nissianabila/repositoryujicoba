#membuat website
#belajar_web_1.py
import wsgiref.simple_server

def application(environ, start_response):
    #response
    response = b"hello world"

    #status respon
    staatus = "200 ok"

    #header respon
    headers = [("content-type","text/html")]

    #pengaturan status dan header
    start_response(status, headers)

    return[response]

if __name__ == "__main__":

    w_s = wsgiref.simple_server.make_server(
        host = "locaalhost",
        port = 8021,
        app = application
    )

    w_s.handle_request()