from flask import Flask, jsonify
from bot_controller import bot_blueprint

app = Flask(__name__)


@app.route('/')
def home():
    return jsonify({'message': 'Welcome to the Bot Management API'})


app.register_blueprint(bot_blueprint, url_prefix='/bot')


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({'error': 'Resource not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
