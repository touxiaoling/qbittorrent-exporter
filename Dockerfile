FROM python:3.11-slim

# Install package
WORKDIR /code
COPY . .
RUN pip3 install .


ENV QBITTORRENT_BASE_URL==http://local.host:8080
ENV QBITTORRENT_USERNAME=admin
ENV QBITTORRENT_PASSWORD=adminadmin

ENTRYPOINT qbittorrent-exporter
