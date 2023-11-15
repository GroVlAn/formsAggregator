from main import app, appLogger, db


@app.route('/')
def main():
    appLogger.info('/', 'get', 'main')
    form = db.form
    form1 = {
        "name": "name1",
        "type": "type1"
    }
    form.insert_one(form1)
    return 'hello'
