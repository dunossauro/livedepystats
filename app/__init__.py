from flask import Flask, request
from .models import configure_db, Event


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    configure_db(app)

    @app.route('/event', methods=['POST'])
    def event():
        response_template = 'Evento {} na plataforma {} foi cadastrado'

        event = Event(
            event=request.json['event'],
            platform=request.json['platform'],
        )

        app.db.session.add(event)
        app.db.session.commit()

        return response_template.format(
            event.event,
            event.platform,
        ), 201

    return app
