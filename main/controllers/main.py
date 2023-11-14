from main import app, appLogger


@app.route('/')
def main():
    request = [1, 2, 3]
    appLogger.info('/', 'get', 'main', request)
    return 'hello'
