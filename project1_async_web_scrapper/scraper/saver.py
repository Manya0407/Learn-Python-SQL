import json

def save_data(data, filename="output.json"):
    """ Save extracted data as JSON """
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
    print(f"✅ Data saved to {filename}")
