import csv

class Event:
    def __init__(self, name, date_time, duration, comments, category, notifications):
        self.name = name
        self.date_time = date_time
        self.duration = duration
        self.comments = comments
        self.category = category
        self.notifications = notifications

    def __str__(self):
        return (f"Event: {self.name}\n"
                f"Date and Time: {self.date_time}\n"
                f"Duration: {self.duration} minutes\n"
                f"Comments: {self.comments}\n"
                f"Category: {self.category}\n"
                f"Notifications: {'Yes' if self.notifications else 'No'}")

    def to_csv_row(self):
        return [self.name, self.date_time, self.duration, self.comments, self.category, self.notifications]

def save_events_to_csv(events, filename):
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for event in events:
            writer.writerow(event.to_csv_row())

events = [
    Event(
        name="Team Meeting",
        date_time="2024-10-05 10:00",
        duration=60,
        comments="Discuss project updates.",
        category="Work",
        notifications=True
    ),
    Event(
        name="Catch up",
        date_time="2024-10-12 10:00",
        duration=30,
        comments="Discuss objectives.",
        category="Growth",
        notifications=True
    )
]

for event in events:
    print(event)

save_events_to_csv(events, 'events.csv')
