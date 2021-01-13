from flask import Flask, request


def create_app():
    app = Flask(__name__)

    @app.route('/event', methods=['POST'])
    def event():
        response_template = 'Evento {} na plataforma {} foi cadastrado'
        return response_template.format(
            request.json['event'],
            request.json['platform'],
        ), 201

    return app
