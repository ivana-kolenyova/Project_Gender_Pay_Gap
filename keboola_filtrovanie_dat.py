import pandas as pd
import os

# Cesta k IN a OUT zlozkam
in_path = "/data/in/tables/"
out_path = "/data/out/tables/"

# Nacitanie dat
try:
    df = pd.read_csv(os.path.join(in_path, "dataset-items.csv"), low_memory=False, encoding="utf-8")
    print(df.head())
except Exception as e:
    print(f"Error: {e}")

# Premenovanie stlpcov
column_mapping = {
    "createdAt": "datum_vytvoreni",
    "data_address": "adresa",
    "data_balcony": "ma_balkon",
    "data_balconyArea": "velilkost_balkonu",
    "data_arrangement": "dipozice",
    "data_city": "mesto",
    "data_countryCode": "kod_krajiny",
    "data_district": "oblast",
    "data_floor": "patro",
    "data_garage": "ma_garaz",
    "data_garden": "ma_zahradu",
    "data_gardenArea": "rozloha_zahrady",
    "data_gpsCoord_lat": "zemepisna_sirka",
    "data_gpsCoord_lon": "zemepisna_delka",
    "data_gpsCoordType": "gps_typ",
    "data_livingArea": "uzitna_plocha",
    "data_neighborhood": "lokalita",
    "data_offerType": "typ_nabidky",
    "data_ownership": "vlastnictvi",
    "data_parking": "ma_parkovani",
    "data_price": "cena",
    "data_priceCurrency": "mena",
    "data_priceType": "forma_platby",
    "data_propertyState": "stav_nemovitosti",
    "data_title": "nazev_inzeratu",
    "data_type": "typ_nemovitosti",
    "modifiedAt": "datum_upravy"
}

df.rename(columns=column_mapping, inplace=True)

# Filtrovanie dat podla stlpca "oblast"
df_filtered = df[df["oblast"].isin(["Brno-město", "Brno-venkov"])]

# Uloženie vyslednej tabulky
df_filtered.to_csv(os.path.join(out_path, "nemovitosti_priprava.csv"), index=False, encoding="utf-8")
