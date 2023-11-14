from main import app, appLogger


@app.route('/')
def main():
    appLogger.info('/', 'get', 'main')
    return 'hello'
