import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def get_team_email(team_name):
    team_emails = {
        "Account Management Team": "receiver@example.com",  # Replace with receiver email
        "Tech Support Team": "receiver@example.com",
        "Billing Support Team": "receiver@example.com",
    }
    email = team_emails.get(team_name, "fallback.team@example.com")
    print(f"➡️ Sending to team: {team_name}, Email: {email}")
    return email

def send_email_notification(ticket, sender_email, sender_password):
    receiver_email = get_team_email(ticket["assigned_team"])

    subject = f"New Support Ticket - {ticket['ticket_id']}"
    body = f"""
New support ticket generated:

Ticket ID: {ticket['ticket_id']}
Customer: {ticket['customer_email']}
Issue: {ticket['message']}
Category: {ticket['category']}
Assigned Team: {ticket['assigned_team']}
Status: {ticket['status']}
Timestamp: {ticket['timestamp']}
"""

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print("✅ Notification email sent successfully.")
    except Exception as e:
        print("❌ Failed to send notification email:", e)

if __name__ == "__main__":
    # Dummy ticket info for testing
    sample_ticket = {
        "ticket_id": "TICKET123",
        "customer_email": "customer@example.com",
        "message": "Issue with login.",
        "category": "account",
        "assigned_team": "Account Management Team",
        "status": "Open",
        "timestamp": "2025-04-12 16:00:00"
    }

    # UPDATE THESE:
    sender_email = "deekdeekshitha70@gmail.com"           # ✅ Your Gmail
    sender_password = "xcdu ydfh dakv gzql"        # ✅ Your App Password (remove spaces!)

    # Remove spaces if needed
    sender_password = sender_password.replace(" ", "")
    send_email_notification(sample_ticket, sender_email, sender_password)