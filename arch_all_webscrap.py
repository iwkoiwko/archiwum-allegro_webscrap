
from bs4 import BeautifulSoup
import requests
import re
from urllib.parse import urljoin
import pandas as pd
import time
import random as ra
import selenium as se
BASE_URL = "https://archiwum.allegro.pl/kategoria/nieruchomosci"
START_URL = f"{BASE_URL}?city=Pozna%C5%84"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

hrefs_list = []
response = requests.get(START_URL, headers=headers)
time.sleep(3)
main_website = BeautifulSoup(response.text, "html.parser")


base_pagination_url = f"{BASE_URL}?city=Pozna%C5%84&p="
links_list = [f"{base_pagination_url}{page_num}" for page_num in range(1, 101)]

print("Znalezione linki:")

for link in links_list[:10]:
    print(link)
print(f"...i {len(links_list)-10} więcej stron (do strony 100)")
time.sleep(1)

real_estate_data = []
for link in links_list:
    time.sleep(ra.randint(0, 2))
    response = requests.get(link, headers=headers)
    website = BeautifulSoup(response.text, "html.parser")
    time.sleep(ra.randint(0, 1))
    print(f"Zbieram dane dla: {link}")
    try:

        div_data = website.find_all("div", class_="mpof_ki myre_zn munh_16")
        time.sleep(0.5)

        if div_data:

            for div in div_data:
                details = div.get_text(strip=True) 
                if details:  
                    real_estate_data.append([details])  
                    time.sleep(1)
                else:
                    print(f"Div jest pusty dla {link}")
            else:
                print(f"ładujemy{link}")
        
    except Exception as e:
        print(f"Błąd przy zbieraniu danych z {link}: {e}")


if real_estate_data:

    df_real_estate = pd.DataFrame(real_estate_data, columns=["Details"])
    time.sleep(0.5)

    df_real_estate.to_excel("real_estate_data_testy.xlsx", index=False)
    print("\nDane zostały zapisane do pliku Excel.")
    df_real_estate.to_csv("real_estate_data_testy.csv")
else:
    print("Nie zebrano żadnych danych.")
