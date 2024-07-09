import time
import os

class DeveloperProfile:
    def __init__(self, name, role, company):
        self.name = name
        self.role = role
        self.company = company
    
    def present_profile(self):
        profile = f"Developer Profile:\n\nName: {self.name}\nRole: {self.role}\nCompany: {self.company}"
        return profile

GREEN = '\033[92m'
RESET = '\033[0m'

def animate_ascii():
    frames = [
        GREEN + r"  /| ________________",
        GREEN + r'O|===|* >________________>',
        GREEN + r"  \|",
        RESET
    ]
    for frame in frames:
        os.system('clear')
        print(frame)
        time.sleep(0.5)

tirawat_profile = DeveloperProfile("Tirawat Nantamas", "CEO and Founder", "Dotmini Software & Defense")

animate_ascii()
print("\n")
print(tirawat_profile.present_profile())
