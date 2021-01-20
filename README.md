# livedepystats

[![codecov](https://codecov.io/gh/dunossauro/livedepystats/branch/main/graph/badge.svg?token=T1KSFHD6EN)](https://codecov.io/gh/dunossauro/livedepystats)

Aplicação para coletar métricas sobre as lives de python.

A aplicação é divida entre back e mobile. O backend será feito em flask e aplicativo mobile em Kivy.


## TODO (v1.0) - WEB
- [x] Rota para receber eventos
- [x] Modelo do banco de dados
- [x] Serializer
- [x] Migration
- [x] WSGI (Gunicorn)
  - [x] supervisor
  - [x] Procfile
- [-] Logs
  - [x] Gunicorn level
  - [ ] Custom handlers
- [x] Coverage
- [x] github Actions?
- [ ] Postgres
- [ ] Deploy no Heroku

### Rodar projeto web

Projeto em desenvolvimento
```bash
flask run
```

WSGI
```bash
gunicorn "app:create_app()" --log-level debug --capture-output
```

Rodar testes
```bash
pytest
```

Rodar cobertura
```
pytest --cov app
```

## TODO (v1.0) - Mobile
- [ ] View principal dos eventos (sem MD)
- [ ] Requests para registar eventos ([UrlRequest](https://kivy.org/doc/stable/api-kivy.network.urlrequest.html))
- [ ] Notificação de aviso do envio do evento ([Plyer](https://github.com/kivy/plyer))
