"""
A console-based customer support ticketing system that organises and 
prioritizes customer inquiries for efficient resolution.

"""

import json

class CustomerInquiry:
    def __init__(self, customer_name, issue_description, priority, status="Open", assigned_to=None, history=None):
        self.customer_name = customer_name
        self.issue_description = issue_description
        self.priority = priority
        self.status = status
        self.assigned_to = assigned_to
        self.history = history if history is not None else []

def add_inquiry(inquiries):
    customer_name = input("Enter customer name: ")
    issue_description = input("Enter issue description: ")
    priority = input("Enter priority (low/medium/high): ")

    inquiry = CustomerInquiry(customer_name, issue_description, priority)
    inquiries.append(inquiry)

    print("Ticket created successfully.")

def view_inquiries(inquiries):
    if not inquiries:
        print("No inquiries found.")
    else:
        print("\n--- Customer Inquiries ---")
        for index, inquiry in enumerate(inquiries, 1):
            print(f"{index}. {inquiry.customer_name} - {inquiry.priority} priority: {inquiry.issue_description}")

def sort_inquiries_by_priority(inquiries):
    inquiries.sort(key=lambda x: x.priority, reverse=True)

def resolve_inquiry(inquiries):
    view_inquiries(inquiries)
    inquiry_index = int(input("Enter the index of the resolved inquiry: ")) - 1

    if 0 <= inquiry_index < len(inquiries):
        inquiries[inquiry_index].status = "Resolved"
        print("Inquiry resolved.")
    else:
        print("Invalid inquiry index.")

def assign_ticket(inquiries):
    view_inquiries(inquiries)
    inquiry_index = int(input("Enter the index of the ticket to be assigned: ")) - 1

    if 0 <= inquiry_index < len(inquiries):
        agent_name = input("Enter the name of the support agent or team: ")
        inquiries[inquiry_index].assigned_to = agent_name
        print(f"Ticket assigned to {agent_name}.")
    else:
        print("Invalid inquiry index.")

def display_ticket_details(inquiries):
    view_inquiries(inquiries)
    inquiry_index = int(input("Enter the index of the ticket to view details: ")) - 1

    if 0 <= inquiry_index < len(inquiries):
        inquiry = inquiries[inquiry_index]
        print("\n--- Ticket Details ---")
        print(f"Customer Name: {inquiry.customer_name}")
        print(f"Priority: {inquiry.priority}")
        print(f"Status: {inquiry.status}")
        print(f"Assigned To: {inquiry.assigned_to}")
        print("Issue Description: ")
        print(inquiry.issue_description)
        print("\n--- Ticket History ---")
        for event in inquiry.history:
            print(event)
    else:
        print("Invalid inquiry index.")

def update_ticket_history(inquiry, action):
    event = f"{action.capitalize()} by {inquiry.assigned_to if inquiry.assigned_to else 'Customer'}"
    inquiry.history.append(event)

def save_data_to_file(inquiries, file_name):
    with open(file_name, 'w') as file:
        data = [vars(inquiry) for inquiry in inquiries]
        json.dump(data, file)

def load_data_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
            inquiries = [CustomerInquiry(**inquiry) for inquiry in data]
            return inquiries
    except FileNotFoundError:
        return []

def main():
    inquiries = load_data_from_file('inquiries.json')
    while True:
        print("\n1. Create new ticket")
        print("2. View inquiries")
        print("3. Sort inquiries by priority")
        print("4. Resolve inquiry")
        print("5. Assign ticket")
        print("6. View ticket details")
        print("7. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6/7): ")

        if choice == '1':
            add_inquiry(inquiries)
        elif choice == '2':
            view_inquiries(inquiries)
        elif choice == '3':
            sort_inquiries_by_priority(inquiries)
            print("Inquiries sorted by priority.")
        elif choice == '4':
            resolve_inquiry(inquiries)
        elif choice == '5':
            assign_ticket(inquiries)
        elif choice == '6':
            display_ticket_details(inquiries)
        elif choice == '7':
            save_data_to_file(inquiries, 'inquiries.json')
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
