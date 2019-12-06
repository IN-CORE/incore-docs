FROM nginx

RUN apt-get -qq update && apt-get -qq install git

RUN mkdir /usr/share/nginx/html/doc && \
  mkdir /usr/share/nginx/html/doc/incore
COPY *.html /usr/share/nginx/html/doc/incore/ 
COPY _images /usr/share/nginx/html/doc/incore/_images
COPY _sources /usr/share/nginx/html/doc/incore/_sources
COPY _static /usr/share/nginx/html/doc/incore/_static
COPY .doctrees /usr/share/nginx/html/doc/incore/.doctrees
COPY incore.conf /etc/nginx/conf.d/default.conf

