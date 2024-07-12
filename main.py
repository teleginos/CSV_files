import csv


def write_holiday_cities(first_letter):
    visited = set()
    want = set()

    with open('travel-notes.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for name, visited_cities, want_to_visit in reader:
            if name.startswith(first_letter):
                for city in visited_cities.split(';'):
                    visited.add(city)

                for city in want_to_visit.split(';'):
                    want.add(city)

    been_to_cities = want - visited

    with open('holiday.csv', 'w', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([f"Посетили: {', '.join(sorted(visited))}"])
        csv_writer.writerow([f"Хотят посетить: {', '.join(sorted(want))}"])
        csv_writer.writerow([f"Никогда не были: {', '.join(sorted(been_to_cities))}"])
        csv_writer.writerow([f"Следующим городом будет: {sorted(want)[0]}"])


if __name__ == '__main__':
    write_holiday_cities('R')

    with open('holiday.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            print(*row)
