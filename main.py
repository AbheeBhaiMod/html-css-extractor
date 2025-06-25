import os

def banner():
    os.system("clear")
    print("\033[1;32m")
    print("┌────────────────────────────────────┐")
    print("│     HTML + CSS COPY TOOL v2.1     │")
    print("└────────────────────────────────────┘")
    print("\033[1;31m     DEVELOPED BY PROXARMY")
    print("\033[1;36m")
    print("[1] COPY WEBSITE HTML + CSS")
    print("[2] JOIN TOOL OWNER WHATSAPP CHANNEL")
    print("\033[0m")

def copy_site():
    url = input("\n🔗 Enter Website URL: ")
    os.system(f"python extractor.py {url}")

def join_whatsapp():
    print("\n🔗 Opening WhatsApp Channel...")
    os.system("xdg-open https://whatsapp.com/channel/0029VbAaGncLNSa92oMbmm2A")  # اپنا نمبر یہاں لکھو

def main():
    banner()
    option = input("🍰 ENTER OPTION (1/2): ")
    
    if option == '1':
        copy_site()
    elif option == '2':
        join_whatsapp()
    else:
        print("\n❌ Invalid option!")

if _name_ == "_main_":
    main()