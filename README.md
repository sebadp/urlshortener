# URL Shortener API
A URL shortener API built with Django and Django REST Framework (DRF).

## Overview
This API allows users to shorten URLs by submitting the long URL to an endpoint, which returns a shortened URL with a unique short code. When a user enters or sends the short URL, they are redirected to the original long URL. The API also includes an endpoint that returns the top 100 most frequently accessed URLs and crawls the website to retrieve its title.

## Setup
To set up the project, follow these steps:

1. Clone the repository to your local machine.
2. Create a virtual environment: python -m venv env.
3. Activate the virtual environment:
On Unix or Linux: source env/bin/activate
4. Install the project dependencies: pip install -r requirements.txt.
5. Apply migrations: python manage.py migrate.
6. Run the development server: python manage.py runserver.

## Usage
### Shorten URL
To shorten a URL, send a POST request to the shorten/ endpoint with the long URL in the body as a JSON object:

json
{
  "long_url": "https://www.example.com"
}
The endpoint will return a response with the shortened URL:

json
{
  "short_code": "abcdefg",
  "long_url": "https://www.example.com"
}

### Redirect to Long URL
To be redirected to the long URL, enter the shortened URL in a browser or send a GET request to the redirect/<short_code>/ endpoint. For example, if the shortened URL is http://localhost:8000/aBcDeFgH, enter http://localhost:8000/aBcDeFgH in the browser or send a GET request to redirect/aBcDeFgH/.

### Top 100 URLs
To view the top 100 most frequently accessed URLs, send a GET request to the top100/ endpoint. The API will return a list of objects containing the short code, long URL, and title:

json
[
  {
    "short_code": "abcdefg",
    "long_url": "https://www.example.com",
    "title": "Example Domain"
  },
  {
    "short_code": "hijklmn",
    "long_url": "https://www.google.com",
    "title": "Google"
  },
  ...
]
