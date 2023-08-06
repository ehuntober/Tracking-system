import json
from datetime import datetime
import time

class CustomerInquiry:
    def __init__(self, customer_name, issue_description, priority, status="Open", assigned_to=None, history=None):
        self.customer_name = customer_name
        self.issue_description = issue_description
        self.priority = priority
        self.status = status
        self.assigned_to = assigned_to
        self.history = history if history is not None else []
        
        
def display_intro():
    print("Customer Support Ticketing System")
    print("The Customer Support Ticketing System is a console-based application")
    print("written in Python to organize and prioritize customer inquiries for efficient resolution.")
    print("It allows support agents or customers to create, view, and manage support tickets, \n while providing automated workflows for handling routine tasks.")
    time.sleep(1)

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

# def sort_inquiries_by_priority(inquiries):
#     inquiries.sort(key=lambda x: x.priority, reverse=True)
def sort_inquiries_by_priority(inquiries):
    priority_order = {"low": 1, "medium": 2, "high": 3}
    inquiries.sort(key=lambda x: priority_order[x.priority.lower()], reverse=True)
    view_inquiries(inquiries)




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
    event = f"{action.capitalize()}, {datetime.now().isoformat()} by {inquiry.assigned_to if inquiry.assigned_to else 'Customer'}"
    inquiry.history.append(event)
    
def automated_workflow(inquiries):
    for inquiry in inquiries:
        if inquiry.priority.lower() == "high" and not inquiry.assigned_to:
            inquiry.assigned_to = "John Doe"
            update_ticket_history(inquiry, f"Auto-assigned to John Doe")
        elif inquiry.priority.lower() == "medium" and not inquiry.assigned_to:
            inquiry.assigned_to = "Jane Smith"
            update_ticket_history(inquiry, f"Auto-assigned to Jane Smith")

def update_ticket_status(inquiries):
    view_inquiries(inquiries)
    inquiry_index = int(input("Enter the index of the ticket to update status: ")) - 1

    if 0 <= inquiry_index < len(inquiries):
        status = input("Enter the new status (Open/In-Progress/Resolved): ")
        inquiries[inquiry_index].status = status
        update_ticket_history(inquiries[inquiry_index], f"Status updated to {status}")
        print("Ticket status updated.")
    else:
        print("Invalid inquiry index.")

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
    display_intro()
    inquiries = load_data_from_file('inquiries.json')
    while True:
        print("\n1. Create new ticket")
        print("2. View inquiries")
        print("3. Sort inquiries by priority")
        print("4. Resolve inquiry")
        print("5. Assign ticket")
        print("6. View ticket details")
        print("7. Update ticket status")
        print("8. Automation and Workflows")
        print("9. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6/7/8/9): ")

        if choice == '1':
            time.sleep(1)  # Introduce a 2-second delay before performing the task
            add_inquiry(inquiries)
        elif choice == '2':
            time.sleep(1)
            view_inquiries(inquiries)
        elif choice == '3':
            time.sleep(1)
            sort_inquiries_by_priority(inquiries)
            print("Inquiries sorted by priority.")
        elif choice == '4':
            time.sleep(1)
            resolve_inquiry(inquiries)
        elif choice == '5':
            time.sleep(1)
            assign_ticket(inquiries)
        elif choice == '6':
            time.sleep(1)
            display_ticket_details(inquiries)
        elif choice == '7':
            time.sleep(1)
            update_ticket_status(inquiries)
        elif choice == '8':
            time.sleep(1)
            automated_workflow(inquiries)
            print("Automation tasks executed.")
        elif choice == '9':
            print('exiting..')
            time.sleep(1)
            print('exiting...')
            time.sleep(2)
            save_data_to_file(inquiries, 'inquiries.json')
            break
        else:
            time.sleep(2)
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


