FROM sfdcpcg/ci-tools:latest

USER root

RUN test -d /root/.ssh || mkdir /root/.ssh
COPY ./id_rsa /root/.ssh/id_rsa
COPY ./id_rsa.pub /root/.ssh/id_rsa.pub
COPY ./config /root/.ssh/config
RUN chmod 700 /root/.ssh
RUN chmod 600 /root/.ssh/id_rsa
RUN chown -R root.root /root/.ssh
RUN ssh-keyscan -H github.com > /root/.ssh/known_hosts

RUN mkdir -p /opt/terraform

WORKDIR /opt/terraform
ENTRYPOINT ["/usr/local/bin/terraform"]
