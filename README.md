# Nightcrawler

[![Build Status](https://travis-ci.org/qiubix/Nightcrawler.svg?branch=master)](https://travis-ci.org/qiubix/Nightcrawler)
[![Coverage Status](https://coveralls.io/repos/github/qiubix/Nightcrawler/badge.svg?branch=master)](https://coveralls.io/github/qiubix/Nightcrawler?branch=master)

Web application running on Django for displaying map of procurers and contractors of public tenders.

## Dependencies

- Django
- GoogleMaps
- beautifulsoup4
- pyhamcrest

## Installation
- Install all dependecies. Application runs with python3 (tested with 3.4)
- copy data to `/data` directory
- run database migrations: `python manage.py migrate`

## Running tests
`python manage.py test tenders`

## Running application
Run: `python manage.py runserver localhost:8080`

Then open browser and go to `localhost:8080/tenders`.

To import data, go to `localhost:8080/tenders/import`.

