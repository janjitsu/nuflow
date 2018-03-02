import pygsheets

client = pygsheets.authorize(service_file='client_secret.json')

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
nubank = client.open("Nubank")
sheet = nubank.sheet1

# Extract and print all of the values
sheet.insert_rows(2,1,['25/02/2018','top sabor','restaurante','jan,karina'])
list_of_hashes = sheet.get_all_records()
print(list_of_hashes)
#print(nubank.worksheets())
#print(sheet.row_values(1))
#print(sheet.row_count())
