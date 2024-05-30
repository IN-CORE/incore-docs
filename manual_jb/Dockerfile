# ----------------------------------------------------------------------
# Compiling documentation
# ----------------------------------------------------------------------

FROM python:3.9-slim AS builder

RUN apt-get -y update

WORKDIR /src
COPY requirements.txt /src/
COPY insert_ga_to_header.py /src/
RUN python3 -m pip install -r requirements.txt


COPY content/ /src/content/
RUN jupyter-book build content/

# Run the insert_ga_to_header.py script to insert Google Analytics code
RUN python3 -m pip install beautifulsoup4
RUN python3 /src/docs/source/insert_ga_to_header.py

# ----------------------------------------------------------------------
# Building actual container
# ----------------------------------------------------------------------

FROM nginx

RUN mkdir -p /usr/share/nginx/html/doc/incore
COPY --from=builder /src/content/_build/html/ /usr/share/nginx/html/doc/incore/

COPY config /usr/share/nginx/html/doc/incore/config

