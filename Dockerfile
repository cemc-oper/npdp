FROM node:latest as npdp_web_builder

COPY npdp-web /srv/npdp-web

RUN cd /srv/npdp-web \
    && yarn install \
    && npm run build

FROM python:3.6

LABEL maintainer="perillaroc@gmail.com"

COPY npdp-server /srv/npdp-server
COPY --from=npdp_web_builder /srv/dist /srv/dist

RUN cd /srv/npdp-server \
    && pip install .

EXPOSE 80

WORKDIR /srv/npdp-server

ENTRYPOINT ["python3", "./run_server.py"]

CMD ["--config-file=/etc/npdp/config.yml", "--static-folder=/srv/dist/static", "--template-folder=/srv/dist/template"]