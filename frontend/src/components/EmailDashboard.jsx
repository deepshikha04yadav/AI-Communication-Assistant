import React, { useState, useEffect } from 'react';
import { getEmails, refreshEmails } from '../api';

function EmailDashboard() {
  const [emails, setEmails] = useState([]);
  useEffect(() => {
    getEmails().then(res => setEmails(res.data));
  }, []);

  return (
    <div>
      <button onClick={() => refreshEmails().then(() => getEmails().then(res => setEmails(res.data)))}>Refresh</button>
      <table>
        <thead>
          <tr>
            <th>Sender</th>
            <th>Subject</th>
            <th>Received At</th>
            <th>Sentiment</th>
            <th>Priority</th>
            <th>Info</th>
            <th>AI Reply</th>
          </tr>
        </thead>
        <tbody>
          {emails.map(e => (
            <tr key={e.id}>
              <td>{e.sender}</td>
              <td>{e.subject}</td>
              <td>{e.received_at}</td>
              <td>{e.sentiment}</td>
              <td>{e.priority}</td>
              <td>{e.phone || e.alternate_email || e.product || ''}</td>
              <td>{e.ai_reply}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default EmailDashboard;
