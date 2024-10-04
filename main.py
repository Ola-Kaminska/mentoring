
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

my_event = Event(
        name="Team Meeting",
        date_time="2024-10-05 10:00",
        duration=60,
        comments="Discuss project updates.",
        category="Work",
        notifications=True
    )
print(my_event)