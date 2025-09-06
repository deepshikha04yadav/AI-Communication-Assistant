from fastapi import FastAPI, Depends
from .database import SessionLocal, init_db
from .models import Email
from .email_utils import fetch_support_emails
from .ai_utils import analyze_sentiment, extract_info, generate_reply

app = FastAPI()
init_db()

@app.get("/emails")
def get_emails():
    db = SessionLocal()
    emails = db.query(Email).order_by(Email.priority.desc(), Email.received_at.desc()).all()
    return [e.__dict__ for e in emails]

@app.post("/refresh")
def refresh_emails():
    support_msgs = fetch_support_emails("EMAIL_USER", "EMAIL_PASS")
    db = SessionLocal()
    for msg in support_msgs:
        # Analyze sentiment, extract info, generate reply, save to DB
        sentiment = analyze_sentiment(msg["body"])
        info = extract_info(msg["body"])
        reply = generate_reply(msg["body"], sentiment, info.get("product", ""))
        email = Email(sender=msg["from"], subject=msg["subject"],
                      body=msg["body"], received_at=msg["date"],
                      sentiment=sentiment, priority="Urgent" if "critical" in msg["subject"] else "Normal",
                      phone=info.get("phone"), alternate_email=info.get("alternate_email"),
                      product=info.get("product"), ai_reply=reply)
        db.add(email)
    db.commit()
    return {"status": "refreshed"}
