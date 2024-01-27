print("This is my file to test Python's execution methods.")
print("The variable __name__ tells me which context this file is running in.")
print("The value of __name__ is:", repr(__name__))

from time import sleep

print("This is my file to demonstrate best practices.")


def process_data(data):
    print("Beginning data processing...")
    modified_data = data + " that has been modified"
    sleep(3)
    print("Data processing finished.")
    return modified_data


if __name__ == "__main__":
    data = "My data read from the Web"
    print(data)
    modified_data = process_data(data)
    print(modified_data)
