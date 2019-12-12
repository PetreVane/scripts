


from twilio.rest import TwilioRestClient

account_sid = "{{ xxx }}" # Your Account SID from www.twilio.com/console
auth_token  = "{{ xxx }}"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Mos Craciun la butoane",
    to="+xxx",    # Replace with your phone number
    from_="+xxxss") # Replace with your Twilio number

print(message.sid)

