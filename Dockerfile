FROM docker.elastic.co/logstash/logstash:8.14.0

RUN /usr/share/logstash/bin/logstash-plugin install logstash-output-opensearch


RUN /usr/share/logstash/bin/logstash-plugin install logstash-filter-age

RUN /usr/share/logstash/bin/logstash-plugin install logstash-filter-opensearch


USER root
RUN apt-get update \
    && apt-get install -y  vim python3 python3-pip \
    && rm -rf /var/lib/apt/lists/*

RUN pip install requests

USER logstash
