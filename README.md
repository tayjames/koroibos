# Koroibos

Koroibos is an API that is designed to expose analytical endpoints displaying data and statistics from the 2016 Summer Olympic Games. This application is the final project of Turing School of Software and Design and intended to simulate a take home challenge from a company as part of the interview process. As such, this project was completed within 48 hours! 

## Endpoints
```
/api/v1/olympians
/api/v1/olympians?age=youngest
/api/v1/olympians?age=oldest
/api/v1/olympian_stats
```

## Example Requests and Responses
```
GET /api/v1/olympians
[
    {
        "name": "Andreea Aanei",
        "team": "Romania",
        "age": "22",
        "sport": "Weightlifting",
        "medal": "NA"
    },
    {
        "name": "Nstor Abad Sanjun",
        "team": "Spain",
        "age": "23",
        "sport": "Gymnastics",
        "medal": "NA"
    },
    {
        "name": "Antonio Abadia Beci",
        "team": "Spain",
        "age": "26",
        "sport": "Athletics",
        "medal": "NA"
    },
    {
        "name": "Giovanni Abagnale",
        "team": "Italy",
        "age": "21",
        "sport": "Rowing",
        "medal": "Bronze"
    },...{}
```

```
GET /api/v1/olympians?age=youngest

[
    {
        "name": "Ana Iulia Dascl",
        "team": "Romania",
        "age": "13",
        "sport": "Swimming",
        "medal": "NA"
    }
]
```

```
GET /api/v1/olympians?age=oldest
[
    {
        "name": "Julie Brougham",
        "team": "New Zealand",
        "age": "62",
        "sport": "Equestrianism",
        "medal": "NA"
    }
]
```

```
GET /api/v1/olympian_stats
[
    {
        "olympian_stats": {
            "total_competing_olympians": 2850,
            "average_weight": {
                "unit": "kg",
                "male_olympians": 79,
                "female_olympians": 62
            },
            "average_age": 26
        }
    }
]
```

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Requirements

* [Python 3.8](https://www.python.org/downloads/)
* [Django 1.11.0](https://docs.djangoproject.com/en/2.2/topics/install/#installing-distribution-package)
* [Postgres](https://www.postgresql.org/download/)

## Clone 
```
$ git clone git@github.com:tayjames/koroibos.git
$ cd koroibos
````

## Setup
```
$ python3.8 -m venv env
$ source env/bin/activate
(env)$ cd olympic_tracker
(env)$ python manage.py makemigrations
(env)$ python manage.py migrate
```

## Testing
Run the test suit with `python manage.py test`

###### Spin up a server with the command `python manage.py runserver` and visit `http://localhost:8000/` to start exploring some endpoints
