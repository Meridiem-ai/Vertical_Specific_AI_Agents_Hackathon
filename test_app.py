# from main import main_


# query = "quelle est la longueur de 'déclinaison'"
# print(main_(query))
import requests

def call_api(query):
    url = "http://127.0.0.1:8000/run-agent/"
    payload = {"query": query}

    response = requests.post(url, json=payload)

    print(response.json())

query = "quelle est la longueur de 'déclinaison'"

call_api(query)