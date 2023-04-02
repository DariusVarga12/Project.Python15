import csv
import json
import os

categories_hp = {
    'slow_cars': range(0, 120),
    'fast_cars': range(120, 180),
    'sport_cars': range(180, 1000),
}

categories_price = {
    'cheap': range(0, 1000),
    'medium': range(1000, 5000),
    'expensive': range(5000, 1000000),
}


def load_cars_from_csv(filename):
    cars = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cars.append({
                'id': int(row['id']),
                'brand': row['brand'],
                'model': row['model'],
                'hp': int(row['hp']),
                'price': int(row['price'])
            })
    return cars


def save_cars_to_csv(filename, cars):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['id', 'brand', 'model', 'hp', 'price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for car in cars:
            writer.writerow(car)


def save_cars_to_json(filename, cars):
    with open(filename, 'w') as jsonfile:
        json.dump(cars, jsonfile, indent=4)


def generate_car_id(cars):
    ids = set([car['id'] for car in cars])
    while True:
        new_id = random.randint(1, 1000000)
        if new_id not in ids:
            return new_id


def categorize_cars(cars):
    categorized_cars = {}
    for category in categories_hp:
        categorized_cars[category] = []
    for category in categories_price:
        categorized_cars[category] = []
    for car in cars:
        for category, range_hp in categories_hp.items():
            if car['hp'] in range_hp:
                categorized_cars[category].append(car)
                break
        for category, range_price in categories_price.items():
            if car['price'] in range_price:
                categorized_cars[category].append(car)
                break
    return categorized_cars


def categorize_cars_by_brand(cars):
    categorized_cars = {}
    for car in cars:
        brand = car['brand']
        if brand not in categorized_cars:
            categorized_cars[brand] = []
        categorized_cars[brand].append(car)
    return categorized_cars


if __name__ == '__main__':
    cars = load_cars_from_csv('cars.csv')
    categorized_cars = categorize_cars(cars)
    print('Cars categorized by horsepower:')
    for category, cars in categorized_cars.items():
        if category in categories_hp:
            print(category)
            for car in cars:
                print(f"{car['brand']} {car['model']}: {car['hp']} hp")
    print('\nCars categorized by price:')
    for category, cars in categorized_cars.items():
        if category in categories_price:
            print(category)
            for car in cars:
                print(f"{car['brand']} {car['model']}: {car['price']} $")


    if not os.path.exists('output_data'):
        os.makedirs('output_data')

    categorized_cars = categorize_cars(cars)
    for category, cars in categorized_cars.items():
        filename = f'output_data/{category}.json'
        save_cars_to_json(filename, cars)

    categorized_cars = categorize_cars_by_brand(cars)
    for brand, cars in categorized_cars.items():
        filename = f'output_data/{brand.lower()}.json'
        save_cars_to_json(filename, cars)



