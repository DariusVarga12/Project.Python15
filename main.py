import csv

with open('cars.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    for row in reader:
        print(row)  # adăugați această linie pentru a verifica conținutul rândului
        car = {'id': next(id_generator), 'brand': row['brand'], 'model': row['model'], 'hp': int(row['hp']), 'price': int(row['price'])}
