import requests

nomPokemon = input("Dame el nombre de un Pokémon: ")

url = "https://pokeapi.co/api/v2/pokemon/" + nomPokemon

respuesta = requests.get(url)

if respuesta.status_code == 200:
    data = respuesta.json()

    print("")
    print("Tu Pokémon es:", data["name"])
    print("Tiene las siguientes habilidades:")

    for habilidad in data["abilities"]:
        print(" -", habilidad["ability"]["name"])


    for star in data["stats"]:
        print("*", star["stat"]["name"],":", star["base_stat"])

else:
    print("No se encontró ese Pokémon. Verifica el nombre, intenta de nuevo.")




