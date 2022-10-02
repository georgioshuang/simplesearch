
    sudo apt -y update
    sudo apt -y dist-upgrade
    sudo apt -y autoremove
    sudo apt-get -y install python3
    sudo apt-get -y install python3-django
    sudo apt-get -y install python3-bs4
    sudo apt-get -y install python3-selenium
    sudo apt-get -y install chromium-browser
    sudo cp chromedriver /usr/bin
    sudo nohup python3 ~/python_search_engine/manage.py runserver 0:80
