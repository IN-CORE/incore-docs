FROM nginx

RUN apt-get -qq update && apt-get -qq install git

RUN mkdir /usr/share/nginx/html/doc && \
  mkdir /usr/share/nginx/html/doc/incore
COPY build/html/*.html /usr/share/nginx/html/doc/incore/
COPY build/html/_downloads /usr/share/nginx/html/doc/incore/_downloads
COPY build/html/analyses /usr/share/nginx/html/doc/incore/analyses
COPY build/html/notebooks /usr/share/nginx/html/doc/incore/notebooks
COPY build/html/_images /usr/share/nginx/html/doc/incore/_images
COPY build/html/_sources /usr/share/nginx/html/doc/incore/_sources
COPY build/html/_static /usr/share/nginx/html/doc/incore/_static
COPY incore.conf /etc/nginx/conf.d/default.conf

