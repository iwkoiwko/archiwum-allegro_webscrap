# from bs4 import BeautifulSoup
# import requests
# import pandas as pd
# import re
# from urllib.parse import urljoin
# import numpy as np


# BASE_URL = "https://archiwum.allegro.pl/kategoria/nieruchomosci?city=Pozna%C5%84"
# MAIN_URLS = [BASE_URL] 



# hrefs_list = []

# for MAIN_URL in MAIN_URLS:
#     response = requests.get(MAIN_URL)
#     main_website = BeautifulSoup(response.text, "html.parser")

#     relevant_elements = main_website.find_all("a", href=re.compile(r"^/&p=\d{1,100}"))
#     hrefs = [link["href"] for link in relevant_elements]
#     hrefs_list.extend(hrefs)


# links_list = [urljoin(BASE_URL, href) for href in hrefs_list]
# links_list = pd.unique(np.array(links_list))


# all_real_estate = []

# for link in links_list:
#     response = requests.get(link)
#     website = BeautifulSoup(response.text, "html.parser")

#     relevant_elements = website.find_all("a", href=re.compile(r"^/&p=\d{1,100}"))
#     hrefs = [link["href"] for link in relevant_elements]
#     all_real_estate.extend(hrefs)

# all_real_estate = [urljoin(BASE_URL, href) for href in all_real_estate]


# df_all_real_estate = []

# for link in all_real_estate:
#     response = requests.get(link)
#     website = BeautifulSoup(response.text, "html.parser")


    

#     print(f"Zbieram dane dla url:{link}")
    

#     for real_estate in all_real_estate:
#         tab_id = real_estate.find("div", class_="opbox-sheet opbox-sheet-82927 _17d9e_Ww88Y msts_n7 card msts_pt mg9e_16 mvrt_16 mj7a_16 mh36_16 mg9e_24_l mvrt_24_l mj7a_24_l mh36_24_l a883q")
#         tab_link = urljoin(link, f"#{tab_id}")
#         response = requests.get(tab_link)
#         website = BeautifulSoup(response.text, "html.parser")
#         table = website.find("div", class_="mpof_ki myre_zn munh_16")


#         df = pd.read_html(str(table))[0]
#         df_all_real_estate.append(df)
# final_df = pd.concat(df_all_real_estate, ignore_index=True)
# final_df.to_excel("re.xlsx", index=False)
# from bs4 import BeautifulSoup
# import requests
# import re
# from urllib.parse import urljoin
# import pandas as pd

# BASE_URL = "https://archiwum.allegro.pl/kategoria/nieruchomosci"
# START_URL = f"{BASE_URL}?city=Pozna%C5%84"

# # Nagłówki dla requestów (symulacja przeglądarki)
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
# }

# # 1. Pobieranie linków paginacji
# hrefs_list = []
# response = requests.get(START_URL, headers=headers)
# main_website = BeautifulSoup(response.text, "html.parser")

# # Szukamy linków do kolejnych stron paginacji
# relevant_elements = main_website.find_all("a", href=re.compile(r"\?city=Pozna%C5%84&p=\d+"))
# hrefs_list = [urljoin(BASE_URL, link["href"]) for link in relevant_elements]

# # Usuwamy duplikaty
# links_list = list(set(hrefs_list))

# print("Znalezione linki paginacji:")
# for link in links_list:
#     print(link)

# # 2. Pobieranie linków do ofert nieruchomości z każdej strony paginacji
# all_real_estate = []
# for link in links_list:
#     response = requests.get(link, headers=headers)
#     website = BeautifulSoup(response.text, "html.parser")

#     # Znajdujemy linki do konkretnych ofert nieruchomości
#     offer_elements = website.find_all("a", href=re.compile(r"&p=\d+"))
#     hrefs = [urljoin(BASE_URL, link["href"]) for link in offer_elements]
#     all_real_estate.extend(hrefs)

# # Usuwamy duplikaty
# all_real_estate = list(set(all_real_estate))

# # 3. Pobieranie szczegółów oferty z każdej strony
# ramka_danych = []
# for offer_url in all_real_estate:
#     response = requests.get(offer_url, headers=headers)
#     website = BeautifulSoup(response.text, "html.parser")
    
#     print(f"Zbieram dane dla: {offer_url}")

#     # Przykładowe divy zawierające dane oferty
#     try:
#         ramka_danych = website.find("div", class_="mpof_ki myre_zn munh_16").get_text(strip=True)
        
     
        
#     except AttributeError as e:
#         print(f"Błąd przy zbieraniu danych z {offer_url}: {e}")

# # Tworzymy DataFrame z zebranych danych
# df_real_estate = pd.DataFrame(ramka_danych)

# # Zapisz do pliku Excel
# df_real_estate.to_excel("real_estate_data.xlsx", index=False)

# print("\nDane zostały zapisane do pliku Excel.")
from bs4 import BeautifulSoup
import requests
import re
from urllib.parse import urljoin
import pandas as pd
import time
import random as ra

BASE_URL = "https://archiwum.allegro.pl/kategoria/nieruchomosci"
START_URL = f"{BASE_URL}?city=Pozna%C5%84"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

hrefs_list = []
response = requests.get(START_URL, headers=headers)
time.sleep(2)
main_website = BeautifulSoup(response.text, "html.parser")



relevant_elements = main_website.find_all("a", href=re.compile(r"\?city=Pozna%C5%84&p=\d+"))
time.sleep(1)
hrefs_list = [urljoin(BASE_URL, link["href"]) for link in relevant_elements]


links_list = list(set(hrefs_list))

print("Znalezione linki :")
for link in links_list:
    print(link)
time.sleep(1)

real_estate_data = []
for link in links_list:
    time.sleep(ra.randint(1, 2))
    response = requests.get(link, headers=headers)
    website = BeautifulSoup(response.text, "html.parser")
    time.sleep(ra.randint(1, 2))
    print(f"Zbieram dane dla: {link}")
    try:

        div_data = website.find_all("div", class_="mpof_ki myre_zn munh_16")
        time.sleep(1)

        if div_data:

            for div in div_data:
                details = div.get_text(strip=True)  # Wyciągamy tylko tekst
                if details:  # Sprawdź, czy tekst w divie jest niepusty
                    real_estate_data.append([details])  # Dodajemy tekst jako listę, aby uniknąć problemu z kolumnami
                    time.sleep(1)
                else:
                    print(f"Div jest pusty dla {link}")
            else:
                print(f"Brak div-a o klasie 'mpof_ki myre_zn munh_16' dla {link}")
        
    except Exception as e:
        print(f"Błąd przy zbieraniu danych z {link}: {e}")


if real_estate_data:

    df_real_estate = pd.DataFrame(real_estate_data, columns=["Details"])
    time.sleep(1)

    df_real_estate.to_excel("real_estate_data.xlsx", index=False)
    print("\nDane zostały zapisane do pliku Excel.")
    df_real_estate.to_csv("real_estate_data.csv")
else:
    print("Nie zebrano żadnych danych.")
