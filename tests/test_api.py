from pytest import mark
from flask import url_for

RESPONSE_DATA_TEMPLATE = 'Evento {} na plataforma {} foi cadastrado'


def test_event_post_should_response_201(client):
    response = client.post(
        url_for('event'), json={'event': 'cha', 'platform': 'twitch'}
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

    response = client.post(url_for('event'), json=event_json)

    expected = RESPONSE_DATA_TEMPLATE.format(
        event_json['event'], event_json['platform']
    )

    assert expected == response.data.decode()
