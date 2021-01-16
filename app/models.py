from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db = SQLAlchemy()


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event = db.Column(db.String(80), nullable=False)
    platform = db.Column(db.String(80), nullable=False)
    created = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)

    def __repr__(self):
        return f'Event(id={self.id}, event="{self.event}", platform="{self.platform}", created=datetime({self.created}))'  # NOQA


def configure_db(app):
    db.init_app(app)
    app.db = db
