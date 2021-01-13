# livedepystats

Aplicação para coletar métricas sobre as lives de python.

A aplicação é divida entre back e mobile. O backend será feito em flask e aplicativo mobile em Kivy.


## TODO (v1.0) - WEB
- [x] Rota para receber eventos
- [ ] Modelo do banco de dados
- [ ] Serializer
- [ ] WSGI
- [ ] Gitlab-CI
- [ ] Deploy no Heroku

## TODO (v1.0) - Mobile
- [ ] View principal dos eventos (sem MD)
- [ ] Requests para registar eventos ([UrlRequest](https://kivy.org/doc/stable/api-kivy.network.urlrequest.html))
- [ ] Notificação de aviso do envio do evento ([Plyer](https://github.com/kivy/plyer))
