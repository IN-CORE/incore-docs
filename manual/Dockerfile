# ----------------------------------------------------------------------
# Compiling documentation
# ----------------------------------------------------------------------

FROM python:3.7-slim AS builder

RUN apt-get -y update && apt-get -y install pandoc

WORKDIR /src
COPY requirements.txt /src/
RUN python3 -m pip install -r requirements.txt

COPY source/ /src/source/
RUN sphinx-build -M html "source" "build"

# ----------------------------------------------------------------------
# Building actual container
# ----------------------------------------------------------------------

FROM nginx

RUN mkdir -p /usr/share/nginx/html/doc/incore
COPY --from=builder /src/build/html/ /usr/share/nginx/html/doc/incore/

