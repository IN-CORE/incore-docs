# ----------------------------------------------------------------------
# Compiling documentation
# ----------------------------------------------------------------------

FROM python:3.9-slim AS builder

RUN apt-get -y update

WORKDIR /src
COPY requirements.txt /src/
RUN python3 -m pip install -r requirements.txt

COPY content/ /src/content/
RUN jupyter-book build content/

# ----------------------------------------------------------------------
# Building actual container
# ----------------------------------------------------------------------

FROM nginx

RUN mkdir -p /usr/share/nginx/html/doc/incore
COPY --from=builder /src/content/_build/html/ /usr/share/nginx/html/doc/incore/

