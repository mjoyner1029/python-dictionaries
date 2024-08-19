# Initial service tickets
service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

# Function to open a new service ticket
def open_ticket(ticket_id, customer, issue, status="open"):
    if ticket_id in service_tickets:
        print(f"Ticket ID {ticket_id} already exists.")
    else:
        service_tickets[ticket_id] = {"Customer": customer, "Issue": issue, "Status": status}
        print(f"Ticket ID {ticket_id} opened successfully.")

# Function to update the status of an existing ticket
def update_ticket_status(ticket_id, new_status):
    if ticket_id in service_tickets:
        service_tickets[ticket_id]["Status"] = new_status
        print(f"Ticket ID {ticket_id} status updated to {new_status}.")
    else:
        print(f"Ticket ID {ticket_id} not found.")

# Function to display all tickets or filter by status
def display_tickets(status=None):
    for ticket_id, details in service_tickets.items():
        if status is None or details["Status"] == status:
            print(f"ID: {ticket_id}")
            print(f"  Customer: {details['Customer']}")
            print(f"  Issue: {details['Issue']}")
            print(f"  Status: {details['Status']}")
            print()

# Example usage
open_ticket("Ticket003", "Charlie", "Network issue")
update_ticket_status("Ticket001", "closed")
display_tickets()  # Display all tickets
display_tickets("open")  # Display only open tickets
