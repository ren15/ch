FROM ubuntu:20.04

COPY install_pkgs.sh /build/

RUN \
    apt-get update &&\
    apt-get install -y sudo curl wget &&\
    bash /build/install_pkgs.sh

RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

WORKDIR /app


