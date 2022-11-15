# Platzigram

Create a minimal project (inspired by instagram) in Django.

![](https://i.imgur.com/4VotR0d.png)

## Dependencies
Python 3
Django

## Usage
```shell
python3 -m venv .env
.env\Scripts\activate
pip install -r requirements.txt
pip freeze
```

```python
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## SuperUser
```shell
python manage.py createsuperuser
```