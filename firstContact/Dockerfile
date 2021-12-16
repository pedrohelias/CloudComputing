FROM ubuntu:20.04
RUN apt-get -y update
RUN apt-get -y install python
RUN apt-get -y install net-tools
RUN apt-get -y install iputils-ping
RUN apt-get -y install python3-pip
RUN apt-get -y install nano
RUN pip install requests
RUN cd home && mkdir cloud #criando a pasta cloud apos entrar em home
WORKDIR /cloud
ADD /codigo_teste_2.py ./
CMD ["python3", "./codigo_teste_2.py"]
#RUN python3 codigo_teste.py
#WORKDIR /
