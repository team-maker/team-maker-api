## 1 -  Requirements

 -  Python: run `brew install python3`

## 2 - Setup

 - run `pip3 install virtualenv`

 - create your virtual env and activate it `virtualenv venv && source venv/bin/activate`

 - install dependencies `pip3 install -r requirements.txt`

 - Add dummy data to the db `python3 manage.py seed core --number=15`

## 3 - Run

- Run the server `python3 manage.py runserver`

$$ 4 - Shell

- Run python shell `python3 manage.py shell_plus`