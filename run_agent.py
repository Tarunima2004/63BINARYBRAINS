# run_agent.py
from datetime import datetime
from classify1 import classify_issue
from assigner import assign_to_team
from send_email_notification1 import send_email_notification  # correct import

# Your credentials
SENDER_EMAIL = "deekdeekshitha70@gmail.com"
SENDER_PASSWORD = "xcdu ydfh dakv gzql"

# Sample ticket
sample_ticket = {
    "ticket_id": "abc123",
    "customer_email": "jane.doe@example.com",
    "message": "My internet is not working since morning.",
    "status": "Open",
    "timestamp": str(datetime.now())
}

# Step 1: Classify issue
category = classify_issue(sample_ticket["message"])
print("Predicted category:", category)
sample_ticket["category"] = category

# Step 2: Assign to team
assign_to_team(sample_ticket, category)

# Step 3: Send notification
send_email_notification(sample_ticket, SENDER_EMAIL, SENDER_PASSWORD)
print("Notification sent to team!")
