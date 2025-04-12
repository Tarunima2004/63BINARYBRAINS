import imaplib
import email

def read_latest_email(username, password):
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(username, password)
    mail.select("inbox")
    
    status, data = mail.search(None, "UNSEEN")  # get unread emails
    email_ids = data[0].split()
    
    for eid in email_ids[-1:]:  # get the latest one
        status, msg_data = mail.fetch(eid, '(RFC822)')
        raw_email = msg_data[0][1]
        msg = email.message_from_bytes(raw_email)

        subject = msg["subject"]
        sender = msg["from"]
        body = ""

        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True).decode()
        else:
            body = msg.get_payload(decode=True).decode()

        return sender, subject, body

# Example usage
email_user = "deekdeekshitha70@gmail.com"
email_pass = "xcdu ydfh dakv gzql"
sender, subject, message = read_latest_email(email_user, email_pass)
print("Sender:", sender)
print("Subject:", subject)
print("Message:", message)