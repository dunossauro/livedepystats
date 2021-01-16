from pytest import mark
from flask import url_for
from app.models import Event


def test_event_post_should_response_201(client):
    response = client.post(
        url_for('api.event'), json={'event': 'cha', 'platform': 'twitch'}
    )

    assert response.status_code == 201


@mark.parametrize(
    'event,platform', [
        ('cha', 'youtube'),
        ('zoom', 'youtube'),
        ('cigarrinho', 'twitch'),
        ('gritinho', 'twitch')
    ]
)
def test_event_post_should_return_event_name(event, platform, client):
    event_json = {'event': event, 'platform': platform}

    response = client.post(url_for('api.event'), json=event_json).json
    assert response['event'] == event_json['event']


@mark.parametrize(
    'event,platform', [
        ('cha', 'youtube'),
        ('zoom', 'youtube'),
        ('cigarrinho', 'twitch'),
        ('gritinho', 'twitch')
    ]
)
def test_event_post_should_return_event_platform(event, platform, client):
    event_json = {'event': event, 'platform': platform}

    response = client.post(url_for('api.event'), json=event_json).json
    assert response['platform'] == event_json['platform']


def test_event_should_register_database_event_row(client, app):
    client.post(
        url_for('api.event'),
        json={'event': 'cha', 'platform': 'twitch'}
    )

    assert Event.query.filter_by(event='cha', platform='twitch').first()
