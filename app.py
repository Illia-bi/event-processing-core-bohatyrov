def process_event(event: str) -> str:
    return f"event: {event}"


def main():
    event = input("event: ")
    print(process_event(event))


if __name__ == "__main__":
    main()
