📱✨ HTML + CSS Copy Tool v2.1 ✨📱

<div align="center">

![🔥](https://i.postimg.cc/KYp3rG11/IMG-20250223-WA0031.jpg)  
*Developed by ProxArmy*  
🔥 Your Trusted Web Extractor 🔥

</div>

---

⚙️ Requirements

- 📱 Android device (Recommended: Redmi Fire or higher)  
- 📲 Termux app installed  
- 🔥 Android 7.0+ (Nougat) or higher for best performance

---

🚀 Installation & Setup

```bash
Update & upgrade packages
pkg update && pkg upgrade -y

Install Python and Git
pkg install python git -y

Install required Python libraries
pip install requests bs4

Clone the repository
git clone https://github.com/AbheeBhaiMod/html-css-extractor.git
cd html-css-extractor
```

---

▶️ How to Run

```bash
python extractor.py
```

- Enter the *website URL* when prompted  
- Extracted files will be saved in the *extracted_site/* folder  

---

📂 Access Extracted Files on Your Phone

To access the saved extracted files easily, run these commands in Termux:


termux-setup-storage

cp -r extracted_site /data/data/com.termux/files/home/storage/shared/

Copy the extracted_site folder to your phone's Internal Storage

Now Successfully Done Check Your Files And Get Html Code ✅
