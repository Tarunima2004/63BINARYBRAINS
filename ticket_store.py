import json
import os

def save_ticket(ticket, filename="tickets.json"):
    # Load existing tickets if file exists
    if os.path.exists(filename):
        with open(filename, "r") as f:
            try:
                tickets = json.load(f)
            except json.JSONDecodeError:
                tickets = []
    else:
        tickets = []

    # Optional: Avoid duplicates based on ticket_id
    if any(t.get("ticket_id") == ticket.get("ticket_id") for t in tickets):
        print("⚠️ Ticket already saved. Skipping.")
        return

    tickets.append(ticket)

    with open(filename, "w") as f:
        json.dump(tickets, f, indent=4)

    print("🎫 Ticket saved to file.")

# ✅ Make sure this is correctly indented
if __name__ == "__main__":
    sample_ticket = {
        "ticket_id": "12345",
        "customer_name": "John Doe",
        "issue_type": "technical",
        "description": "Internet not working."
    }

    save_ticket(sample_ticket)
