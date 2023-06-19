FROM python:3-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
#RUN apk add bash curl iptables iperf3
COPY json-to-influx-telegraf.py  .

# docker build -t scottmsilver/purple-air:1.0 .
# docker push scottmsilver/purple-air:1.0 
# docker run scottmsilver/purple-air:1.0 python3 json-to-influx-telegraf.py URL
# sudo usermod -aG docker telegraf
# newgrp docker
# now test with:
# become telegraf
# sudo -u telegraf bash
# telegraf -test