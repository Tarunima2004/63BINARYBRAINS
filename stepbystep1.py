import imaplib
import email
from email.header import decode_header
import time
from ticket_store import save_ticket
from classify import classify_issue
from ticket import generate_ticket
from assigner import assign_to_team
from notifier import send_notification

notifier_email = "deekdeekshitha70@gmail.com"
notifier_password = "xcduydfhdakvgzql"

def connect_to_gmail(email_id, app_password):
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(email_id, app_password)
        mail.select("inbox")
        print("Connected to Gmail.")
        return mail
    except Exception as e:
        print(f"Connection Error: {e}")
        return None

def fetch_latest_email(mail):
    try:
        result, data = mail.search(None, 'UNSEEN')  # get unseen (unread) emails
        email_ids = data[0].split()

        if not email_ids:
            return None, None

        latest_email_id = email_ids[-1]
        result, msg_data = mail.fetch(latest_email_id, "(RFC822)")
        raw_email = msg_data[0][1]
        msg = email.message_from_bytes(raw_email)

        sender = msg["From"]
        subject = msg["Subject"]
        body = ""

        # extract plain-text content
        if msg.is_multipart():
            for part in msg.walk():
                content_type = part.get_content_type()
                content_disposition = str(part.get("Content-Disposition"))
                if content_type == "text/plain" and "attachment" not in content_disposition:
                    body = part.get_payload(decode=True).decode(errors="ignore")
                    break
        else:
            body = msg.get_payload(decode=True).decode(errors="ignore")

        return sender, body.strip()

    except Exception as e:
        print(f"Error fetching email: {e}")
        return None, None

# Your Gmail credentials (Use environment variables or secure methods ideally)
email_id = "deekdeekshitha70@gmail.com"
app_password = "xcduydfhdakvgzql"

# Connect to Gmail
mail = connect_to_gmail(email_id, app_password)

if not mail:
    print("Failed to connect. Exiting.")
    exit()

# Loop to check for new emails
print("Checking for new emails every 60 seconds...\n")
while True:
    sender, message = fetch_latest_email(mail)
    if message:
        category = classify_issue(message)
        ticket = generate_ticket(sender, message, category)
        ticket = assign_to_team(ticket, category) 
        save_ticket(ticket) 
        send_notification(ticket, notifier_email, notifier_password)
        print(ticket)
    else:
        print("No new email.")
    time.sleep(10)