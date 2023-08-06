# Tracking-system

### Customer Support Ticketing System
The Customer Support Ticketing System is a console-based application written in Python to organize and prioritize customer inquiries for efficient resolution. It allows support agents or customers to create, view, and manage support tickets, while providing automated workflows for handling routine tasks.

### Features
** Ticket Creation: **  Allows support agents or customers to create new support tickets for their inquiries or issues.
View Inquiries: Provides a list of all customer inquiries, showing their details and current status.
Sort Inquiries by Priority: Sorts the inquiries based on their priorities, from high to low.
Resolve Inquiry: Marks a customer inquiry as "Resolved" once it has been successfully addressed.
Assign Ticket: Assigns support agents or teams to specific tickets based on their expertise or workload.
View Ticket Details: Displays detailed information about a specific ticket, including customer details, priority, status, and history.
Update Ticket Status: Allows users to change the status of a ticket from "Open" to "In-progress" or "Resolved."
Automation and Workflows: Automates routine tasks and predefined workflows, including auto-assigning high and medium priority tickets to specific agents.
How to Use
Clone or download the repository to your local machine.
Make sure you have Python installed (Python 3.6 or later recommended).
Open a terminal or command prompt and navigate to the project directory.
Run the entry.py file by executing the following command:
Copy code
python entry.py
The application will start, and you will see a menu with options to interact with the ticketing system.
Follow the on-screen instructions to create new tickets, view inquiries, update ticket status, assign tickets, and more.
Notes
When creating a new ticket, you need to provide the customer name, issue description, and priority (low, medium, or high).
To update the status of a ticket, choose option 7 and provide the index of the ticket you wish to update.
The application will automatically assign high priority tickets to "John Doe" and medium priority tickets to "Jane Smith" as per the predefined workflow.
Saving Data
The application will save ticket data to a file named inquiries.json in the project directory.
When you choose option 9 to exit the application, all ticket data will be saved, and you can resume where you left off the next time you run the application.
Contributing
If you find any bugs, issues, or have suggestions for improvements, please feel free to open an issue or submit a pull request. Your contributions are welcomed!

License
This project is licensed under the MIT License - see the LICENSE file for details.