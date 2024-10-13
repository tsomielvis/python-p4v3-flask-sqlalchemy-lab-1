from app import app, db
from models import Earthquake
import random
from datetime import datetime, timedelta

def seed_data():
    print("Starting seeding process...")
    
    with app.app_context():
        # Create tables if they don't exist
        db.create_all()
        
        # Clear existing data
        Earthquake.query.delete()
        db.session.commit()
        
        # Generate random earthquake data
        places = ["California", "Japan", "Chile", "Indonesia", "Nepal", "Mexico", "Italy", "New Zealand", "Turkey", "Iran"]
        start_date = datetime(2000, 1, 1)
        end_date = datetime.now()

        for _ in range(100):  # Create 100 random earthquakes
            magnitude = round(random.uniform(4.0, 9.0), 1)
            place = random.choice(places)
            date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
            year = date.year

            earthquake = Earthquake(magnitude=magnitude, place=place, year=year)
            db.session.add(earthquake)

        db.session.commit()
        print("Successfully added 100 new earthquake records.")

    print("Seeding process completed.")

if __name__ == '__main__':
    seed_data()

