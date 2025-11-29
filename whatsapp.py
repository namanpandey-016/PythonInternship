import pywhatkit
number = input("Enter the message you wants to send")
message = input("Enter the message you wants to send")

pywhatkit.sendwhatmsg_instantly(f"+91{message}" , f"{message}")
