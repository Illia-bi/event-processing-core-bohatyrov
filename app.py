from validator import validate_event


def process_event(event_name: str) -> str:
    return f"Processing event: {event_name}"


def main():
    event = input("Enter event name: ")

    if validate_event(event):
        print(process_event(event))
    else:
        print("MAIN BRANCH ERROR")


if __name__ == "__main__":
    main()
