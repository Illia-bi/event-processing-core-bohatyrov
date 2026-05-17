from validator import validate_event


def process_event(event_name):
    return f"Processing event: {event_name}"


event = input("Enter event name: ")

if validate_event(event):
    print(process_event(event))
else:
    print("Invalid event")
