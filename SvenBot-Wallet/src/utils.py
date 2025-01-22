import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def validate_address(address):
    return address.startswith("SVEN")

if __name__ == "__main__":
    print(validate_address("SVEN12345"))
