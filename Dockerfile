from postgres:13

ENV POSTGRES_USER database
ENV POSTGRES_PASSWORD batatinha
ENV POSTGRES_DB livedepystats

USER postgres

RUN initdb