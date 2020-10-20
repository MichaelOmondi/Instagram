# InstagramClone Project-Instagram

An application where users can:
*   Sign up
*   Sign in (authentication)
*   Upload pictures
*   Follow other users and see their pictures
*   Like other users pictures
*   Comment on other users' pictures

## Getting Started

*   Fork the repository
*   git clone the project to your local machine
*   Set up a virtual environment in the project folder
```
python3.8 -m venv --without-pip virtual
```

### Prerequisites

*get pip 

```
curl https://bootstrap.pypa.io/get-pip|python
```

*get all requirements in the requirements.txt file

```
pip install -r requirements.txt
```

### Installing

Ensure that the MODE in the .env is set to development ('dev'), which will automatically set debug to true.

Now run the following command

```
python3.8 manage.py runserver
```

And view the site at the port provided which is most likely 127.0.0.1:8000

## Running the tests

To run the automated tests for this system, run the following command

```
python3.8 manage.py test instagram
```

## Deployment

To deploy on heroku:
*   Have a Procfile in the project root;
*   Update requirements.txt file with all the requirements in the project root;
*   Have Gunicorn to requirements.txt;
*   Have runtime.txt to specify the correct Python version in the project root;
*   Ensure configuration whitenoise to serve static files.
*   Add a heroku remote by logging in
*   Configure all the settings in .env on heroku (set MODE to 'prod' on heroku)
*   git push to heroku
*   git push database and migrate to heroku server

## Built With

* Python Programming Language
* Django Web Framework
* Bootstrap v4 Framework

## Versioning

Find all the versions used in the requirements.txt or run the following command to confirm:

```
pip freeze
```

## Author

* **Michael Omondi** 


## License

This project is licensed under the MIT License - see the LICENSE file for details

## Known Bugs
 * Some functions did not work as expected and due to the submission time, they will be worked upn in the near future.
 
 ##  Contat Info 
 * You can reach me via e-mail on:
   omondimike11@gmail.com

