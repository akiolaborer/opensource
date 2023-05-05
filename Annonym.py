import smtplib
import PySimpleGUI as sg
from email.mime.text import MIMEText

port = "25"

dns = "example@dns.com"
smtp = "example@smtp.com"
pop3 = "example@pop3.com"
subject = "subject"
attach = "example.jpg"
message = "sentence"
mime = "text\html"

sg.theme("Dark Blue")

layout = [
    [sg.Text("DNS", size = (10, 1)), sg.Input(dns, size = (25, 1), key = "-dns-")],
    [sg.Text("SMTP", size = (10, 1)), sg.Input(smtp, size = (25, 1), key = "-smtp-")],
    [sg.Text("POP3", size = (10, 1)), sg.Input(pop3, size = (25, 1), key = "-pop3-")],
    [sg.Text("SUBJECT", size = (10, 1)), sg.Input(subject, size = (25, 1), key = "-subject-")],
    [sg.Text("ATTACH", size = (10, 1)), sg.Input(attach, size = (30, 1)), sg.FileBrowse(key = "-attach-")],  
    [sg.Text("MESSAGE", size = (10, 1)), sg.Multiline(message, size = (30, 10), key = "-message-")],
    [sg.Button("New", size = (10, 1), enable_events = True, key = "-new-"),
    sg.Button("Send", size = (10, 1), enable_events = True, key = "-send-"),
    sg.Button("Exit", size = (10, 1), enable_events = True, key = "-exit-")]
 ]

window = sg.Window("", layout, size=(400, 400))

msg = MIMEText(message, mime)
msg[ "Smtp" ] = smtp
msg[ "Pop3" ] = pop3
msg[ "Subject" ] = subject
msg[ "Attach" ] = attach
msg[ "Message"] = message

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED: break

    elif event == "-new-": 
     window['-dns-'].Update('')
     window['-smtp-'].Update('')
     window['-pop3-'].Update('')
     window['-subject-'].Update('')
     window['-message-'].Update('')
     pass

    elif event == "-send-": 
     server = smtplib.SMTP(smtp, port)
     server.send_message(msg)
     server.quit()
     pass

    elif event == "-exit-": break
window.close()
