[![GitHub license](https://img.shields.io/badge/implemented%20by-Andy-blue)](https://www.linkedin.com/in/andy-kiaka-76a983110/)

## Approach

1. Virtual environment
   
    Each developer has their preferences in choosing tools to 
    define a virtual environment, for this implementation I 
    opted to use pipenv which uses Pipfile instead of requirements.txt, 
    however a requirements.txt file will be provided to facilitate 
    other developers to use this Implementation.

## Prerequisites

1. Libraries
   
   As described in the Pipfile and requirements.txt files, 
   the libraries needed to run this implementation are:

    * django==4.0.2
    * djangorestframework==3.13.1
    * drf-yasg==1.20.0

## How to use

1. Build the images by running
    ```
    $ docker-compose up -d --build
    ```
2. Make the migrations
   The implementation comes with the app api migration done, the dev just needs to "migrate"
   ```
   $ docker-compose exec hotel_web python manage.py migrate
   ``` 
3. Create a super user
   ```
   $ docker-compose exec hotel_web python manage.py createsuperuser
   ```


### Endpoints

All available endpoints together with auto-generated documentation
can be consulted via the link

*   http://localhost:8000/swagger/


Exemple 1:

* http://localhost:8000/rooms/rooms/

Payload:

As shown in swagger documentation mentioned above, all CRUD operations can be performed.
An exemple of how to create a room (POST)
        
    {
        "number": 105,
        "size": 3.5,
        "nb_bed": 2,
        "type_of_bed": "King size",
        "frigo_bar": false
    }

Exemple 2:

* http://localhost:8000/bookings/bookings/

Payload:

An exemple of how to book a room (POST)

    {        
        "start_date": "2022-02-11",
        "end_date": "2022-02-12",
        "room": 1
    }

## Author ✒️

* **Andy Kiaka** - *Job Completo* - [detona115](https://github.com/detona115)

---
⌨️ com ❤️ por [detona115](https://github.com/detona115) 😊