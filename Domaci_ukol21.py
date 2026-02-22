import requests
ico = input("Zadejte IČO subjektu: ")
url = f"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{ico}"
odpoved = requests.get(url)
data = odpoved.json()

obchodni_jmeno = data.get("obchodniJmeno")
adresa = data.get("sidlo", {}).get("textovaAdresa")

print(f"Název: {obchodni_jmeno}")
print(f"Adresa: {adresa}")
