import requests
nazev_firmy = input ("Zadej název firmy: ")
url = "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat"

headers = {"accept":"application/json", "Content-Type":"application/json"} 
data_pro_ares = {"obchodniJmeno":nazev_firmy}
odpoved = requests.post(url, headers=headers, json=data_pro_ares)  
vysledek = odpoved.json()
seznam_firem = vysledek.get("ekonomickeSubjekty", [])                            
print(f"Nalezeno firem: {len(seznam_firem)}")

for firma in seznam_firem:
    nazev = firma.get("obchodniJmeno") 
    ico = firma.get("ico")       
    print(f"{nazev}, IČO:{ico}")                                                                          