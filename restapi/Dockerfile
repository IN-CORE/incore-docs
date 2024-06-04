FROM nginx

RUN apt-get -qq update && apt-get -qq install git

RUN mkdir /usr/share/nginx/html/doc && \
  mkdir /usr/share/nginx/html/doc/api
COPY index.html /usr/share/nginx/html/doc/api/.
COPY config /usr/share/nginx/html/doc/api/config
COPY api.conf /etc/nginx/conf.d/default.conf

