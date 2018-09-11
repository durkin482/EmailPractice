import smtplib

from email.mime.multipart import MIMEMultipart
from email.MIMEText import MIMEText

SEMISPACE = "; "
FROM = "durkinsautoemail@gmail.com"
TO = ["durkin482@gmail.com"]

msg = MIMEMultipart()
msg["Subject"] = "Update Budget"

body = "Match current expenditures to the budget's limits. I'll be sure to remind you again in a week."
body = MIMEText(body)
msg.attach(body)

server = smtplib.SMTP(host='smtp.gmail.com', port=587)
server.starttls()
server.login(FROM, "252*33EMAIL!!")
server.sendmail(FROM, SEMISPACE.join(TO), msg.as_string())
server.quit()