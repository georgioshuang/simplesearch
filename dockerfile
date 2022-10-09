#FROM ubuntu:22.04
FROM alpine

RUN apt -y update \
	&& apt -y upgrade \
	&& apt-get -y install python3 \
	&& apt-get -y install python3-django \
	&& apt-get -y install python3-bs4 \
	&& apt-get -y install python3-selenium \
	&& apt-get -y install python3-pip \
	&& pip3 install requests \
	&& apt-get install -y wget \
	&& apt-get install -y curl \
	&& apt-get install -y fonts-liberation libasound2 libatk-bridge2.0-0 libatk1.0-0 libatspi2.0-0 libcairo2 libcups2 libdrm2 libgbm1 libgtk-3-0 libgtk-4-1 libnspr4 libnss3 libpango-1.0-0 libwayland-client0 libxcomposite1 libxdamage1 libxfixes3 libxkbcommon0 libxrandr2 xdg-utils
	

RUN wget -P ~/downloads/  https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
	&& dpkg -i ~/downloads/google-chrome-stable_current_amd64.deb \
	&& wget -P ~/downloads/ https://chromedriver.storage.googleapis.com/106.0.5249.61/chromedriver_linux64.zip \
	&& cd ~/downloads \
	&& apt-get install unzip \
	&& unzip chromedriver_linux64.zip
RUN chmod +x ~/downloads/chromedriver \
	&& mv ~/downloads/chromedriver /usr/local/share/chromedriver \
	&& ln -fs /usr/local/share/chromedriver /usr/bin/chromedriver

WORKDIR /var/www/html

COPY . .

CMD ["python3", "manage.py", "runserver", "0.0.0.0:80"]