FROM ubuntu

RUN apt -y update \
	&& apt -y dist-upgrade \
	&& apt -y autoremove \
	&& apt-get -y install python3 \
	&& apt-get -y install python3-django \
	&& apt-get -y install python3-bs4 \
	&& apt-get -y install python3-selenium \
	&& apt-get -y install python3-pip \
	&& pip3 install requests \
	&& apt-get install -y wget \
	&& apt-get install -y curl
	#&& apt -y install chromium-browser 
RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/
   
WORKDIR /var/www/html

#COPY requirements.txt ./
#RUN pip install -r requirements.txt
COPY . .

CMD ["python3", "manage.py", "runserver", "0.0.0.0:80"]