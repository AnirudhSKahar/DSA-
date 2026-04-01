class PatientNode:
    def __init__(self, pid, name, age, disease, priority):
        self.id = pid
        self.name = name
        self.age = age
        self.disease = disease
        self.priority = priority
        self.next = None


class LinkedList(PatientNode):
    def __init__(self):
        self.head = None

    def add_patient(self, pid, name, age, disease, priority):
        # Check for duplicate ID
        temp = self.head
        while temp:
            if temp.id ==pid:
                print("Error: Patient ID already exists. Please use a unique ID.")
                return
            temp = temp.next

        # If no duplicate, insert new node
        new_node = PatientNode(pid, name, age, disease, priority)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
        print("Patient added successfully!")

    def display_patients(self):
        if self.head is None:
            print("No patients available.")
        else:
            temp = self.head
            print("\n--- Patient List ---")
            while temp:
                print("ID:", temp.id, "| Name:", temp.name,
                      "| Age:", temp.age, "| Disease:", temp.disease,
                      "| Priority:", temp.priority)
                temp = temp.next

    def search_patient(self, search_id):
        temp = self.head
        while temp:
            if temp.id == search_id:
                print("Patient Found → ID:", temp.id, ", Name:", temp.name,
                      ", Age:", temp.age, ", Disease:", temp.disease,
                      ", Priority:", temp.priority)
                return
            temp = temp.next
        print("Patient not found.")

waiting_queue = []

def add_to_queue(pid):
    waiting_queue.append(pid)
    print("Patient added to waiting queue.")

def serve_patient():
    if len(waiting_queue) == 0:
        print("Waiting queue is empty.")
    else:
        served = waiting_queue.pop(0)
        print("Patient ID", served, "served from waiting queue.")
patients = LinkedList()

while True:
    print("\n--- Hospital Patient Management System ---")
    print("1. Add Patient")
    print("2. Display Patient List")
    print("3. Search Patient by ID")
    print("4. Manage Waiting Queue")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        pid = int(input("Enter Patient ID: "))
        name = input("Enter Patient Name: ")
        age = int(input("Enter Age: "))
        disease = input("Enter Disease: ")
        priority = int(input("Enter Priority (1=Emergency, 2=Normal): "))
        patients.add_patient(pid, name, age, disease, priority)

    elif choice == 2:
        patients.display_patients()

    elif choice == 3:
        search_id = int(input("Enter Patient ID to search: "))
        patients.search_patient(search_id)

    elif choice == 4:
        print("1. Add to Waiting Queue")
        print("2. Serve Patient (Dequeue)")
        sub_choice = int(input("Enter choice: "))
        if sub_choice == 1:
            pid = int(input("Enter Patient ID to add to queue: "))
            add_to_queue(pid)
        elif sub_choice == 2:
            serve_patient()

    elif choice == 5:
        print("Exiting system. Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
        
        
