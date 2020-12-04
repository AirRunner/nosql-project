from pandas import read_csv

INPUT_FILE = "coronavirus-commercants-parisiens-livraison-a-domicile.csv"
OUTPUT_FILE = "redis_commercants_commands.txt"

ID_KEY = 'commerces:id'
NAME_KEY = 'commerces:name'
ADDRESS_KEY = 'commerces:address'
POSTCODE_KEY = 'commerces:postcode'
TYPE_KEY = 'commerces:type'
SERVICE_KEY = 'commerces:service'
DESCRIPTION_KEY = 'commerces:description'
PHONE_KEY = 'commerces:phone'
LOCATION_KEY = 'commerces:location'
SHOP_KEY = 'commerces:commerce'

commerces = read_csv(INPUT_FILE, sep=';')
commerces = commerces[['Nom du commerce', 'Adresse', 'Code postal', 'Type de commerce', 'Services', 'Description', 'Téléphone', 'geo_point_2d']]
commerces.dropna(inplace=True)

with open(OUTPUT_FILE, 'w') as out:
  for index, row in commerces.iterrows():
    fields = {}
    fields['name'] = str(row['Nom du commerce'])
    fields['address'] = str(row['Adresse'])
    fields['postcode'] = str(row['Code postal'])
    fields['type'] = str(row['Type de commerce'])
    fields['service'] = str(row['Services'])
    fields['description'] = str(row['Description'])
    fields['phone'] = str(row['Téléphone'])
    geopoint = str(row['geo_point_2d']).split(',')
    fields['latitude'] = geopoint[0]
    fields['longitude'] = geopoint[1]
  
    print(f"Processing '{fields['name']}'...")
  
    for field in fields:
      fields[field] = fields[field].replace('\\', '\\\\').replace("'", "\\'").replace('"', '\\"').replace('\n', ' ')
  
    # Indexes
    out.write(f"SADD '{ID_KEY}' {index}\n")
    out.write(f"SADD '{POSTCODE_KEY}:{fields['postcode']}' {index}\n")
    out.write(f"SADD '{TYPE_KEY}:{fields['type']}' {index}\n")
    out.write(f"SADD '{SERVICE_KEY}:{fields['service']}' {index}\n")
  
    # Data
    out.write(f"HSET {SHOP_KEY}:{index} id {index} name \"{fields['name']}\" description \"{fields['description']}\" phone \"{fields['phone']}\"\n")
    out.write(f"GEOADD {LOCATION_KEY} {fields['longitude']} {fields['latitude']} {index}\n")

print("-- Done! --")