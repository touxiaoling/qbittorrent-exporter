from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='qbittorrent-exporter',
    packages=['qbittorrent_exporter'],
    version='0.6.1',
    long_description=long_description,
    long_description_content_type="text/markdown",
    description='Prometheus exporter for qbittorrent',
    author='To Min',
    author_email='me@leishi.io',
    url='https://github.com/touxiaoling/qbittorrent-exporter',
    download_url='https://github.com/leishi1313/downloader-exporter/archive/0.5.1.tar.gz',
    keywords=['prometheus', 'qbittorrent'],
    classifiers=[],
    python_requires='>=3.11',
    install_requires=[
        'loguru==0.7.0',
        'qbittorrent-api==2023.4.47',
        'prometheus_client==0.16.0',
        'fastapi[all]==0.95.1'
    ],
    entry_points={
        'console_scripts': [
            'qbittorrent-exporter=qbittorrent_exporter.exporter:main',
        ]
    }
)
