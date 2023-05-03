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

# Write the output to a text file
with open('output.txt', 'w') as outfile:
    for country, code in country_codes.items():
        outfile.write("\n")
        outfile.write("\n")
        outfile.write(country)
        for sentence in sentences:
            replaced_sentence = sentence.format(country=country, code=code)
            outfile.write('\n' + replaced_sentence)
