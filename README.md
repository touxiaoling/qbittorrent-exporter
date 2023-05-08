# qbittorrent-exporter

A prometheus exporter for qBitorrent. Get metrics from servers and offers them in a prometheus format.


## How to use it

You can run it in a docker container:

```
docker run -d -e QBITTORRENT_BASE_URL=http://localhost:8080 -e QBITTORRENT_USERNAME=admin -e QBITTORRENT_PASSWORD=adminadmin -p 9000:9000 tousang/qbittorrent-exporter
```
Add this to your prometheus.yml
```
  - job_name: "downloader_exporter"
    static_configs:
        - targets: ['exporter-host-name:port']
```
