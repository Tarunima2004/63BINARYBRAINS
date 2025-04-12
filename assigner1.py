from classify import classify_issue  # ✅ import at the top

def assign_to_team(ticket, category):
    team_mapping = {
        "technical": "Technical Support Team",
        "billing": "Billing Support Team",
        "account": "Account Support Team",
        "general": "General Support Team"  # fallback
    }

    team = team_mapping.get(category.lower(), "General Support Team")
    ticket["assigned_team"] = team
    print(f"Assigned to: {team}")

    return ticket


# ✅ Test
if __name__ == "__main__":
    sample_ticket = {
        "ticket_id": "abc123",
        "customer_name": "Jane Doe",
        "description": "My internet is not working."  # No manual category!
    }

    # 🔁 Use classifier instead of manually specifying issue_type
    category = classify_issue(sample_ticket["description"])
    assign_to_team(sample_ticket, category)
    print(sample_ticket)
