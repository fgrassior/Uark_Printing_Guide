# 🖼️ UARC Printing Bot - QUICK START WITH IMAGES

## ✅ What You Get

- ✓ **Bot script** with image support
- ✓ **19 PNG images** from your PDF
- ✓ **11 interactive steps** with screenshots
- ✓ **English only**
- ✓ **Ready to deploy**

---

## 🚀 FASTEST Deploy: 5 Minutes

### Option 1: Local Testing (Your PC)

```bash
# 1. Install Python (if not installed)
#    Download from https://python.org

# 2. Create folder
mkdir uarc-bot
cd uarc-bot

# 3. Copy these files into this folder:
#    - uarc_bot_final.py
#    - page_1.png through page_19.png
#    - requirements.txt

# 4. Install dependencies
pip install python-telegram-bot==20.3 Pillow==10.0.0

# 5. Run bot
python uarc_bot_final.py

# 6. Open Telegram, search for your bot, type /start
# Done! 🎉
```

**Note:** Bot only runs while this terminal is open.

---

### Option 2: Railway Deploy (Always Running)

```bash
# 1. Go to https://railway.app → Sign up with GitHub

# 2. Create folder structure on GitHub:
uarc-printing-bot/
├── uarc_bot_final.py
├── page_1.png
├── page_2.png
├── ... (all 19 images)
├── requirements.txt
└── README.md

# 3. In Railway Dashboard:
#    - Click "+ New Project"
#    - "Deploy from GitHub"
#    - Select your repo

# 4. Set Start Command:
python uarc_bot_final.py

# 5. Done! Bot runs 24/7 🚀
```

---

## 📦 Files Needed

### Main Script:
**`uarc_bot_final.py`** - The bot (ready to use)

### Images (19 total):
```
page_1.png   → Title page
page_2.png   → Building Access
page_3.png   → Internet Access
page_4.png   → UARC Computers
page_5.png   → PC Lab Rules
page_6.png   → PC Lab Rules continued
page_7.png   → Printing intro
page_8.png   → First PaperCut setup
page_9.png   → Printing with credentials
page_10.png  → Printing dialog
page_11.png  → How to print step-by-step
page_12.png  → Print Release process
page_13.png  → Release print job
page_14.png  → Printing costs
page_15.png  → Scanning & Copying
page_16.png  → Scanning tips
page_17.png  → Questions/Support
page_18.png  → Support info
page_19.png  → Footer/Credits
```

### Dependencies:
**`requirements.txt`**
```
python-telegram-bot==20.3
Pillow==10.0.0
```

---

## 📱 On Telegram

### User sees:
```
[IMAGE: Step 1 screenshot]

🖨️ Step 1: Before You Start
Prepare everything you need

Make sure you have:
✓ Your personal badge
✓ A computer in the PC Lab
✓ Your documents ready to print

📌 Important: The badge number is located 
on the front, top, or side of your badge.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Step 1/11

[⬅️ Back] [1/11] [Next ➡️]
[1] [4] [7] [10]
```

### User clicks "Next ➡️":
```
[IMAGE: Step 2 screenshot]

💻 Step 2: Log into the PC
...
[⬅️ Back] [2/11] [Next ➡️]
[1] [4] [7] [10]
```

**Each step shows:** Screenshot + Instructions + Navigation

---

## ⚙️ Customization

### Change bot token:
Edit `uarc_bot_final.py` line 14:
```python
TOKEN = "your_token_here"
```

### Change images:
Replace `page_X.png` files with your own

### Add/remove steps:
Edit `STEPS` array in the bot script

### Change text:
Edit titles, subtitles, content in `STEPS`

---

## 🔧 Troubleshooting

### Q: Bot doesn't respond?
- Check TOKEN is correct
- Ensure bot is running
- Restart with `Ctrl+C` then `python uarc_bot_final.py`

### Q: Images not showing?
- Check all 19 PNG files are in bot folder
- Verify file names: `page_1.png` through `page_19.png`
- Run bot again

### Q: Command /start not working?
- Make sure bot script is running
- Type `/start` in Telegram chat with bot
- Wait 2 seconds

### Q: "FileNotFoundError"?
- Ensure images are in **same folder** as bot script
- Check file paths are correct
- Verify PNG files exist

---

## 📊 Bot Features

✅ **11 Complete Steps** - From start to finish  
✅ **Screenshots Included** - Visual guide from PDF  
✅ **Interactive Buttons** - Easy navigation  
✅ **Quick Jump** - Click step numbers  
✅ **Mobile Friendly** - Perfect on phones  
✅ **English Only** - Professional  
✅ **Credentials Included** - All usernames/passwords  
✅ **Error Messages** - Clear help text  

---

## 🎯 Next Steps

### 1. Download Files
- Get `uarc_bot_final.py`
- Get all 19 `page_X.png` images
- Get `requirements.txt`

### 2. Test Locally (Optional)
```bash
python uarc_bot_final.py
```
Test on Telegram to make sure it works

### 3. Deploy to Railway
- Push to GitHub with all files
- Connect Railway to GitHub
- Set start command: `python uarc_bot_final.py`
- Bot runs 24/7! ✨

### 4. Share with Students
- Give bot username: `@your_bot_name`
- Students type `/start`
- They get interactive guide with images!

---

## 📞 Support

**Bot Issues:**
- Check all files are in same folder
- Verify token is correct
- Look at printed error messages

**UARC Questions:**
📧 fgrassi@uark.edu

---

## 🎉 You're All Set!

Bot is ready to deploy with full images. Choose local or Railway deploy above and go! 🚀

**Status:** ✅ Ready  
**Files:** ✅ Complete (19 images)  
**Token:** ✅ Valid  
**Tested:** ✅ Yes  

Deploy now! 🤖
