from src import app

if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run(host='0.0.0.0')