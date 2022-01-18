FROM jenkins/jenkins:lts

ENV JENKINS_ADMIN_ID admin
ENV JENKINS_ADMIN_PASSWORD password
ENV JAVA_OPTS -Djenkins.install.runSetupWizard=false
ENV CASC_JENKINS_CONFIG /usr/share/jenkins/ref/jenkins.yaml
ENV ANSIBLE_HOST_KEY_CHECKING False

USER root

COPY plugins.txt /usr/share/jenkins/ref
COPY jenkins.yaml /usr/share/jenkins/ref
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt

ENV pip_packages "ansible cryptography requests docker"

RUN apt-get update && \
    apt-get -y install sudo \
    systemd \
    systemd-sysv \
    nano \
    build-essential \
    libffi-dev \
    libssl-dev \
    openssh-server \
    apt-utils \
    apt-transport-https \
    ca-certificates \
    curl \
    wget \
    gnupg2 \
    gnupg-agent \
    lsb-release \
    software-properties-common \
    python3 \
    python3-dev \
    python3-setuptools \
    python3-wheel \
    python3-apt \
    python3-pip

RUN python3 -m pip install --upgrade pip

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

RUN mkdir -p /data/test
RUN chown -R jenkins:jenkins /data/test
RUN chmod -R 777 /data/test

RUN python3 -m pip install $pip_packages

RUN useradd -rm -d /home/ansible -m -p ansible -s /bin/bash ansible
RUN echo "ansible:Pass@123" | chpasswd
RUN echo "ansible  ALL=(ALL)  NOPASSWD: ALL" >> /etc/sudoers
RUN chmod 755 /home/ansible
RUN usermod -aG sudo ansible

CMD service ssh start && while true; do sleep 3000; done

RUN ssh-keygen -t rsa -f ~/.ssh/id_rsa -q -N ""
RUN mkdir -p /home/ansible/.ssh \
    && cp ~/.ssh/id_rsa.pub /home/ansible/.ssh/authorized_keys \
    && chown -R ansible:ansible /home/ansible/.ssh

# Install Ansible inventory file
RUN mkdir -p /etc/ansible
RUN chown -R ansible:ansible /etc/ansible

USER ansible

# Install Ansible inventory file
RUN echo "[local]\nlocalhost.localdomain ansible_connection=local" > /etc/ansible/hosts

USER jenkins
