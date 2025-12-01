import requests
from bs4 import BeautifulSoup as bs
from db import create_database, insert_into_db

URL_TEMPLATE = "https://www.work.ua/ru/jobs-odesa/?page=2"



def parse_and_store_jobs(url):
    """Parses job listings from the given URL and stores them in the database.

    Args:
        url (str): The URL of the job listings page.

    Returns:
        None
    """

    result_dict = {'href': [], 'title': [], 'text': []}
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for non-200 status codes

        soup = bs(response.text, "html.parser")

        # Improved selectors based on potential HTML structure variations
        vacancies_names = soup.find_all('h2', class_='my-0')
        vacancies_info = soup.find_all('p', class_="overflow")

        for name in vacancies_names:
            if name.a:  # Check if 'a' tag exists
                result_dict['href'].append(url + name.a['href'])
                try:
                    result_dict['title'].append(name.a['title'])
                except (AttributeError, TypeError):
                    result_dict['title'].append("No title found")

        for info in vacancies_info:
            result_dict['text'].append(info.text.strip())  # Remove leading/trailing whitespace

        create_database()  # Assuming this creates the database if it doesn't exist
        insert_into_db(result_dict)  # Assuming this inserts data into your database

        print("Successfully parsed and stored jobs from", url)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching jobs from {url}: {e}")


parse_and_store_jobs(URL_TEMPLATE)

