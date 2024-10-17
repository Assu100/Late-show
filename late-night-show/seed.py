import csv
from app import db
from models import Episode, Guest

# seeding the db
def seed_data():
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            episode = Episode(date=row[0], number=row[1])
            db.session.add(episode)
    db.session.commit()

if __name__ == "__main__":
    seed_data()
