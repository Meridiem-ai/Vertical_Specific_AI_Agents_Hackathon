# import requests

# # URL de l'API
# url = "http://localhost:8000/run-agent/"

# # Les données à envoyer dans la requête
# data = {
#     "query": "envoie un email à Corentin Malmart darkk9172@gmail.com pour dire bonjour et ajoute le dans le crm"
# }

# # Envoi de la requête POST
# response = requests.post(url, json=data, stream=True)

# # Affichage des étapes au fur et à mesure
# for chunk in response.iter_content(chunk_size=None):
#     if chunk:
#         print(chunk.decode("utf-8"))
