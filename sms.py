from twilio.rest import Client

account_sid = 'AC6e92d968b3ed992527281ca252c34c0d'
auth_token = ''
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+',
  body='hello noor',
  to='whatsapp:+'
)

print(message.sid)