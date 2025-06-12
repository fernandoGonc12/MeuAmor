from collections import defaultdict

# TextParser.py

def parse_whatsapp_chat(file_path, search_strings):
    """
    Parses a WhatsApp chat file and counts occurrences of specific strings for each person.

    :param file_path: Path to the WhatsApp chat text file.
    :param search_strings: List of strings to search for in the messages.
    :return: Dictionary with counts of occurrences for each person.
    """

    occurrences = defaultdict(lambda: defaultdict(int))

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                # Check if the line contains a message (format: "date, time - sender: message")
                if " - " in line and ": " in line:
                    try:
                        # Extract sender and message
                        sender, message = line.split(" - ", 1)[1].split(": ", 1)
                        # Count occurrences of each search string in the message
                        for string in search_strings:
                            if string in message:
                                occurrences[sender][string] += 1
                    except ValueError:
                        # Skip lines that don't match the expected format
                        continue
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

    return occurrences

def find_first_occurrences(file_path, search_strings):
    """
    Finds the first occurrence of each search string in the WhatsApp chat file.

    :param file_path: Path to the WhatsApp chat text file.
    :param search_strings: List of strings to search for in the messages.
    :return: Dictionary with the first occurrence of each search string for each person.
    """
    first_occurrences = defaultdict(dict)

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                # Check if the line contains a message (format: "date, time - sender: message")
                if " - " in line and ": " in line:
                    try:
                        # Extract sender and message
                        sender, message = line.split(" - ", 1)[1].split(": ", 1)
                        # Check for first occurrence of each search string
                        for string in search_strings:
                            if string in message and string not in first_occurrences[sender]:
                                first_occurrences[sender][string] = line.strip()
                    except ValueError:
                        # Skip lines that don't match the expected format
                        continue
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

    return first_occurrences


if __name__ == "__main__":
    # Example usage
    chat_file = "Conversa do WhatsApp com Benzinho ❤️.txt"  # Replace with your file path
    search_terms = ["Te amo", "Meu bem", "Amor"]  # Replace with your search strings

    results = parse_whatsapp_chat(chat_file, search_terms)

    for person, counts in results.items():
        print(f"{person}:")
        for term, count in counts.items():
            print(f"  {term}: {count}")

    first_occurrences = find_first_occurrences(chat_file, search_terms)

    print("\nFirst occurrences:")
    for person, occurrences in first_occurrences.items():
        print(f"{person}:")
        for term, occurrence in occurrences.items():
            print(f"  {term}: {occurrence}")