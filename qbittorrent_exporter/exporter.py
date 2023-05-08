import os 

from fastapi import FastAPI
import uvicorn

from prometheus_client import  make_asgi_app
from prometheus_client.core import REGISTRY

from .qbittorrent_exporter import QbittorrentMetricsCollector

app = FastAPI()


def main():
    base_url=os.getenv("QBITTORRENT_BASE_URL")
    user_name=os.getenv("QBITTORRENT_USERNAME")
    user_password=os.getenv("QBITTORRENT_PASSWORD")

    REGISTRY.register(QbittorrentMetricsCollector(host=base_url,username=user_name,password=user_password))
    metrics_app = make_asgi_app()
    app.mount("/metrics", metrics_app)

    uvicorn.run(app, host="0.0.0.0", port=9000)

if __name__ == "__main__":
    main()
    