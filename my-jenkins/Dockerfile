FROM jenkins/jenkins:lts

USER root
RUN apt-get update && \
    apt-get -y install sudo \
    apt-utils \
    apt-transport-https \
    ca-certificates \
    curl \
    wget \
    gnupg2 \
    gnupg-agent \
    lsb-release \
    software-properties-common \
    python3
    python3-pip

RUN curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

RUN apt-get -y update && \
    apt-get install -y docker-ce \
    docker-ce-cli \
    containerd.io

RUN curl -L "https://github.com/docker/compose/releases/download/1.26.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

RUN chmod +x /usr/local/bin/docker-compose
RUN ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose

RUN mkdir -p /data/test && \
    chown -R jenkins:jenkins /data/test && \
    chmod -R 777 /data/test

RUN python3 -m pip install ansible

USER jenkins
