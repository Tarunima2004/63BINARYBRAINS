import uuid
from datetime import datetime
def assign_to_team(category):
    team_map = {
        "billing": "Finance Team",
        "technical": "Tech Support Team",
        "account": "Account Management Team",
        "product": "Logistics Team"
    }
    return team_map.get(category, "General Support Team")
def generate_ticket(sender_email, message, category):
    ticket = {
        "ticket_id": str(uuid.uuid4()),  # unique ID
        "customer_email": sender_email,
        "message": message,
        "category": category,
        "status": "open",
        "timestamp": datetime.now().isoformat(),
        "assigned_team": assign_to_team(category)
    }
    return ticket
# Replace with actual sender and message if you connected email
sender = "deekdeekshitha70@gmail.com"
message = "My internet is not working"
category = "technical"  # this would come from classify_issue(message)

ticket = generate_ticket(sender, message, category)
print("Generated Ticket:")
for key, value in ticket.items():
    print(f"{key}: {value}")