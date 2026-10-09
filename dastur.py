import json

with open('country.json', 'r', encoding='utf-8') as file:
  data = json.load(file)
unique_countries_set = set()
for item in data:
  country_name = item.get('country')
  country_code = item.get('country_code')
  unique_countries_set.add((country_name, country_code))

country_list = list(unique_countries_set)
country_count = len(country_list)

print(f"a) Takrorlanmagan davlatlar soni: {country_count}")
print("Davlatlar ro'yxati (list):")
print(country_list)

sorted_by_area = sorted(data, key=lambda x: x.get('area', 0))

print("\n")
print("b) Davlat maydoni bo'yicha saralangan ma'lumotlar:")
for country in sorted_by_area:
  print(
      f"Davlat: {country.get('country')}, Kodi: {country.get('country_code')},"
      f" Aholi: {country.get('population')}, Til: {country.get('language')},"
      f" Maydoni: {country.get('area')}"
  )
