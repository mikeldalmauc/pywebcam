# Use a base image with Python and OpenCV
FROM python:3

# Terminal environment for colored output
ENV TERM=xterm-256color
RUN echo "PS1='\e[92m\u\e[0m@\e[94m\h\e[0m:\e[35m\w\e[0m# '" >> /root/.bashrc

# Install dependencies
RUN apt-get update
RUN apt-get install -y openssh-server sudo

# SSH  conf------
RUN mkdir /var/run/sshd
RUN echo 'root:redhat' | chpasswd
EXPOSE 22

# Limit the number of simultaneous connections
RUN sed -i 's/^#MaxSessions.*/MaxSessions 1/' /etc/ssh/sshd_config
RUN sed -i 's/^#MaxStartups.*/MaxStartups 1/' /etc/ssh/sshd_config

RUN echo player           -       maxlogins 1 >> /etc/security/limits.conf

# Set app user copy code as appuser so it belogs to app user and change to workdir 
RUN useradd -rm -d /home/player -s /bin/bash -u 1010 player
RUN echo "PS1='\e[92m\u\e[0m@\e[94m\h\e[0m:\e[35m\w\e[0m# '" >> /home/player/.bashrc
RUN echo 'player:player' | chpasswd

COPY src/game.py /home/player/ 
COPY src/compile.py /home/player/ 
RUN python /home/player/compile.py

RUN rm /home/player/compile.py
RUN rm /home/player/game.py
RUN cp -R /home/player/__pycache__/* /home/player/
RUN rm -r /home/player/__pycache__

WORKDIR /home/player

RUN echo 'python game.cpython-312.pyc' >> /home/player/.bashrc

USER root

CMD ["/usr/sbin/sshd", "-D"]