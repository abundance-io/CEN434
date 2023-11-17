import redis

# Connect to Redis
r = redis.Redis(host='localhost', port=6379)

# Create Operation
def create_data():
    key = input("Enter key: ")
    firstname = input("Enter person's first name: ")
    lastname = input("Enter person's last name: ")
    matric_no = input("Enter person's matriculation number: ")

    # Create a dictionary to store person's information
    person_info = {
        'firstname': firstname,
        'lastname': lastname,
        'matricno': matric_no
    }

    # Convert dictionary to a string for storage in Redis
    value = str(person_info)

    r.set(key, value)
    print(f"Created key: {key}, value: {value}")

# Read Operation
def read_data():
    key = input("Enter key to read: ")
    value = r.get(key)
    if value:
        print(f"Value for key {key}: {value.decode('utf-8')}")
    else:
        print(f"Key {key} not found")

# Update Operation
def update_data():
    key = input("Enter key to update: ")
    firstname = input("Enter updated first name: ")
    lastname = input("Enter updated last name: ")
    matric_no = input("Enter updated matriculation number: ")

    # Create a dictionary to store updated person's information
    person_info = {
        'firstname': firstname,
        'lastname': lastname,
        'matricno': matric_no
    }

    # Convert dictionary to a string for storage in Redis
    new_value = str(person_info)

    if r.exists(key):
        r.set(key, new_value)
        print(f"Updated value for key {key}: {new_value}")
    else:
        print(f"Key {key} not found, cannot update")

# Delete Operation
def delete_data():
    key = input("Enter key to delete: ")
    if r.exists(key):
        r.delete(key)
        print(f"Deleted key: {key}")
    else:
        print(f"Key {key} not found, cannot delete")

# Loop for user interaction
while True:
    print("\nOperations:")
    print("1. Create")
    print("2. Read")
    print("3. Update")
    print("4. Delete")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == '1':
        create_data()
    elif choice == '2':
        read_data()
    elif choice == '3':
        update_data()
    elif choice == '4':
        delete_data()
    elif choice == '5':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter a valid option (1-5).")
