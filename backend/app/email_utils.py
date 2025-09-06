import imaplib, email
from email.header import decode_header

def fetch_support_emails(imap_user, imap_pass, imap_server="imap.gmail.com"):
    msgs = []
    mail = imaplib.IMAP4_SSL(imap_server)
    mail.login(imap_user, imap_pass)
    mail.select("inbox")
    typ, data = mail.search(None, 'ALL')
    for num in data.split():
        typ, msg_data = mail.fetch(num, '(RFC822)')
        msg = email.message_from_bytes(msg_data[1])
        subject = decode_header(msg["Subject"])
        if isinstance(subject, bytes):
            subject = subject.decode()
        if any(t in subject for t in ["Support", "Query", "Request", "Help"]):
            msgs.append({...})  # Parse details as needed
    mail.logout()
    return msgs
