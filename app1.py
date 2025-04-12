# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS

from reademail import read_latest_email
from classify import classify_issue
from ticket import generate_ticket, save_ticket
from notifier import notify_team

app = Flask(__name__)
CORS(app)

@app.route("/send-message", methods=["POST"])
def handle_user_message():
    data = request.get_json()
    message = data.get("message", "")

    category = classify_issue(message)
    ticket = generate_ticket(message, category)
    save_ticket(ticket)
    notify_team(category, ticket)

    reply = f"Your issue has been categorized as **{category}** and sent to the {category} support team."
    return jsonify({"reply": reply})

@app.route("/process-emails", methods=["GET"])
def process_emails(): 
    emails = read_latest_email()
    for email in emails:
        full_msg = f"{email['subject']} - {email['body']}"
        category = classify_issue(full_msg)
        ticket = generate_ticket(full_msg, category)
        save_ticket(ticket)
        notify_team(category, ticket)
    return jsonify({"status": f"Processed {len(emails)} email(s)."})

if __name__ == "__main__":
    app.run(debug=True)