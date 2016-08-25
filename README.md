Installing
----------------------

### Dependencies
+ Python 3.5
+ pip

### Installing dependencies
    sudo add-apt-repository ppa:fkrull/deadsnakes
    sudo apt-get update
    sudo apt-get install python3.5 python3.5-dev
    sudo apt-get install python3-pip

### Setting up a virtualenv
    Virtualenv is not required (but it's better to use it)
    sudo pip3 install virtualenv
    mkdir ~/.virtualenvs/
    virtualenv ~/.virtualenvs/light.refugee.info -p <path>/python3.5

### Configuring App
    source ~/.virtualenvs/light.refugee.info/bin/activate      # if you installed
    pip install -r requirements.txt
    cp root/localsettings.example.py root/localsettings.py

### Setting up your django environment
    ./manage.py runserver

### Code style
    source ~/.virtualenvs/light.refugee.info/bin/activate      # if you installed
    pip install flake8
    git diff origin/master | flake8 --diff
