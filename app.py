from wsgiref.simple_server import make_server
from calculatorservice import main

if __name__ == '__main__':
    app = main()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()
