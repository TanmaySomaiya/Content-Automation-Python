import csv

# Read the country codes from a CSV file
country_codes = {}
with open('country code.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        country_codes[row['country']] = row['code']

# Sentences to be replaced
sentences = [
    'Please find top 10 topics, phrases related to {country} Virtual phone number and country code {code}',
    'Please find top 20 keywords related to {country} Virtual number phone',
    'Please create a 2000 word article for {country} phone number provided by TELOZ and Country code {code} based on information provided, also please provide meta content, title'
]

# Replace placeholders in each sentence with the country and code for each country in the table
for country, code in country_codes.items():
    print("\n")
    print("\n")
    print(country)
    for sentence in sentences:
        replaced_sentence = sentence.format(country=country, code=code)
        print(replaced_sentence)

        
