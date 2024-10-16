import csv

def save_events_to_csv(events, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for event in events:
            writer.writerow([event['name'], event['date_time'], event['duration'],
                             event['comments'], event['category'], event['notifications']])

def load_events_from_csv(filename):
    events = []
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                event = {
                    "name": row[0],
                    "date_time": row[1],
                    "duration": int(row[2]),
                    "comments": row[3],
                    "category": row[4],
                    "notifications": row[5] == 'True'
                }
                events.append(event)
    except FileNotFoundError:
        print("File does not exist. Starting with an empty list of events.")
    return events

# CRUD functions
def create_event(events):
    name = input("Enter the name of the event: ")
    date_time = input("Enter the date and time of the event (YYYY-MM-DD HH:MM): ")
    duration = int(input("Enter the duration of the event (minutes): "))
    comments = input("Enter comments (optional): ")
    category = input("Enter category: ")
    notifications = input("Do you want to enable notifications? (yes/no): ").lower() == 'yes'

    event = {
        "name": name,
        "date_time": date_time,
        "duration": duration,
        "comments": comments,
        "category": category,
        "notifications": notifications
    }
    events.append(event)
    print("Event added.")

def read_events(events):
    if not events:
        print("No events to display.")
        return
    for event in events:
        print(f"Event: {event['name']}\n"
              f"Date and Time: {event['date_time']}\n"
              f"Duration: {event['duration']} minutes\n"
              f"Comments: {event['comments']}\n"
              f"Category: {event['category']}\n"
              f"Notifications: {'Yes' if event['notifications'] else 'No'}\n")

def update_event(events):
    name = input("Enter the name of the event to update: ")
    for event in events:
        if event['name'] == name:
            event['date_time'] = input("Enter new date and time (YYYY-MM-DD HH:MM): ")
            event['duration'] = int(input("Enter new duration (minutes): "))
            event['comments'] = input("Enter new comments (optional): ")
            event['category'] = input("Enter new category: ")
            event['notifications'] = input("Do you want to enable notifications? (yes/no): ").lower() == 'yes'
            print("Event updated.")
            return
    print("Event not found.")

def delete_event(events):
    name = input("Enter the name of the event to delete: ")
    for event in events:
        if event['name'] == name:
            events.remove(event)
            print("Event deleted.")
            return
    print("Event not found.")

def main():
    filename = 'events.csv'
    events = load_events_from_csv(filename)

    while True:
        print("\n1. Add event")
        print("2. Display events")
        print("3. Update event")
        print("4. Delete event")
        print("5. Save and exit")
        choice = input("Choose an option: ")

        if choice == '1':
            create_event(events)
        elif choice == '2':
            read_events(events)
        elif choice == '3':
            update_event(events)
        elif choice == '4':
            delete_event(events)
        elif choice == '5':
            save_events_to_csv(events, filename)
            print("Data saved. Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
