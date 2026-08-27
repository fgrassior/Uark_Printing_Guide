#!/usr/bin/env python3
"""
UARC Printing Guide Bot - Full Version with Images
Telegram Bot for interactive step-by-step printing guide
"""
import logging
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Read TOKEN from environment variables (Railway)
TOKEN = os.getenv("TOKEN")
if not TOKEN:
    raise ValueError("TOKEN environment variable not set!")

# Image directory - adjust path based on deployment
IMAGE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define all steps
STEPS = [
    {
        "title": "Step 1: Before You Start",
        "subtitle": "Prepare everything you need",
        "content": """Make sure you have:
- Your personal badge
- A computer in the PC Lab
- Your documents ready to print

IMPORTANT: The badge number is on the front, top, or side of your badge.""",
        "image": "page_2.png"
    },
    {
        "title": "Step 2: Log into the PC",
        "subtitle": "Access the lab computer",
        "content": """Press CTRL+ALT+CANC

Username: Computer number
Password: Rome2019

If not auto-assigned, enter the computer number on the screen.""",
        "image": "page_4.png"
    },
    {
        "title": "Step 3: First Time Setup",
        "subtitle": "Associate your badge with PaperCut",
        "content": """This is only needed the FIRST TIME:

1. Go to HP printers (Gabrielli or Empire Wing)
2. Swipe badge on WHITE badge reader on top of printer
3. Enter your login credentials:

PaperCut Username: S + badge number (e.g. S1234)
PaperCut Password: 1234

WARNING: Change the default password immediately!""",
        "image": "page_8.png"
    },
    {
        "title": "Step 4: Open Your Document",
        "subtitle": "Prepare the file you want to print",
        "content": """From the lab computer, open your document to print (Word, PDF, etc.)

Make sure the document is formatted correctly and ready for printing.""",
        "image": None
    },
    {
        "title": "Step 5: Open Print Dialog",
        "subtitle": "Start the printing process",
        "content": """In your document, click File > Print

Printer Name: dc-01 VirtualPrinter HP
(See image for exact printer name)

Select this virtual printer from the available printers list.""",
        "image": "page_11.png"
    },
    {
        "title": "Step 6: Enter Credentials",
        "subtitle": "Login to PaperCut",
        "content": """A login window will appear. Enter:

Username: S + badge number (e.g. S1234)
Password: Your password (default: 1234)

Click OK to continue.""",
        "image": "page_11.png"
    },
    {
        "title": "Step 7: Confirm Print Settings",
        "subtitle": "Review and adjust print options",
        "content": """A second window will show print details. Verify:

- Number of copies
- Paper size (A4/A3)
- Color or black & white

Click PRINT to send your job to the queue.""",
        "image": "page_12.png"
    },
    {
        "title": "Step 8: Confirmation Sent",
        "subtitle": "Your job is in the print queue",
        "content": """You will see a notification:

PaperCut MF
Document held in print queue

Your job is now queued and ready to be released.""",
        "image": "page_13.png"
    },
    {
        "title": "Step 9: Release Print Job",
        "subtitle": "Complete the printing process",
        "content": """Go to the HP printer and:

1. Swipe your badge on WHITE badge reader on top
2. Select your print job from the list
3. Click "Print" to release the document

The printer will start printing immediately.""",
        "image": "page_13.png"
    },
    {
        "title": "Step 10: Print Costs",
        "subtitle": "How billing works",
        "content": """Printing costs are charged to your PaperCut account:

Initial credit: 20 EUR per semester
A4 Black & White: 0.05 EUR per page
A4 Color: 0.10 EUR per page
A3 Black & White: 0.10 EUR per page
A3 Color: 0.20 EUR per page
Large Formats (Plotter): 1.00 EUR

If you run out of credit, ask Fabio to recharge.""",
        "image": "page_14.png"
    },
    {
        "title": "Step 11: Useful Tips",
        "subtitle": "Additional helpful information",
        "content": """Change Password: 
Open PaperCut on lab PC > "Change Details" > "Change Password"

Cannot print from laptop: 
You must use lab computers only

Large scanner: 
Canon scanner at Gabrielli supports A0 format

Need help? 
Email: fgrassi@uark.edu

Locations:
- Gabrielli Printing Lab (Mark and Linda Area)
- Empire Wing (Fabio Printing Lab)

REMEMBER: Default password (1234) is visible to everyone!
Changing it is mandatory for account security!""",
        "image": "page_15.png"
    }
]

def get_image_path(filename):
    """Get full path to image file"""
    if not filename:
        return None
    return os.path.join(IMAGE_DIR, filename)

def get_keyboard(current_step):
    """Generate navigation keyboard"""
    buttons = []
    
    if current_step > 0:
        buttons.append(InlineKeyboardButton("Back", callback_data=f"step_{current_step-1}"))
    
    buttons.append(InlineKeyboardButton(f"{current_step+1}/{len(STEPS)}", callback_data="noop"))
    
    if current_step < len(STEPS) - 1:
        buttons.append(InlineKeyboardButton("Next", callback_data=f"step_{current_step+1}"))
    
    keyboard = [buttons]
    
    quick_access = []
    for i in range(0, len(STEPS), 3):
        if i != current_step:
            quick_access.append(InlineKeyboardButton(f"{i+1}", callback_data=f"step_{i}"))
    
    if quick_access:
        keyboard.append(quick_access)
    
    return InlineKeyboardMarkup(keyboard)

def format_message(step_num):
    """Format step message"""
    step = STEPS[step_num]
    progress = f"Step {step_num + 1}/{len(STEPS)}"
    
    message = f"{step['title']}\n"
    message += f"{step['subtitle']}\n\n"
    message += f"{step['content']}\n\n"
    message += f"---\n"
    message += f"{progress}"
    
    return message

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /start command"""
    chat_id = update.effective_chat.id
    step = STEPS[0]
    message = format_message(0)
    keyboard = get_keyboard(0)
    
    if step.get("image"):
        image_path = get_image_path(step["image"])
        if os.path.exists(image_path):
            with open(image_path, 'rb') as photo:
                await context.bot.send_photo(
                    chat_id=chat_id,
                    photo=photo,
                    caption=message,
                    reply_markup=keyboard
                )
        else:
            await context.bot.send_message(
                chat_id=chat_id,
                text=message,
                reply_markup=keyboard
            )
    else:
        await context.bot.send_message(
            chat_id=chat_id,
            text=message,
            reply_markup=keyboard
        )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /help command"""
    help_text = """UARC Printing Guide - Help

Commands:
/start - Show Step 1
/step 1-11 - Jump to specific step
/help - Show this message

How to use:
- Use Back and Next buttons to navigate
- Click step numbers (1, 4, 7, 10) for quick access
- Each step includes a screenshot and detailed instructions

Questions?
Email: fgrassi@uark.edu

Bot created for UARC Rome Center"""
    
    await update.message.reply_text(help_text)

async def step_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /step command"""
    if not context.args:
        await update.message.reply_text("Usage: /step 1-11")
        return
    
    try:
        step_num = int(context.args[0]) - 1
        if 0 <= step_num < len(STEPS):
            step = STEPS[step_num]
            message = format_message(step_num)
            keyboard = get_keyboard(step_num)
            
            if step.get("image"):
                image_path = get_image_path(step["image"])
                if os.path.exists(image_path):
                    with open(image_path, 'rb') as photo:
                        await update.message.reply_photo(
                            photo=photo,
                            caption=message,
                            reply_markup=keyboard
                        )
                else:
                    await update.message.reply_text(
                        message,
                        reply_markup=keyboard
                    )
            else:
                await update.message.reply_text(
                    message,
                    reply_markup=keyboard
                )
        else:
            await update.message.reply_text(f"Invalid step. Use /step 1-{len(STEPS)}")
    except ValueError:
        await update.message.reply_text("Use a number. Example: /step 5")

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle button clicks"""
    query = update.callback_query
    await query.answer()
    
    callback_data = query.data
    
    if callback_data.startswith("step_"):
        step_num = int(callback_data.split("_")[1])
        step = STEPS[step_num]
        message = format_message(step_num)
        keyboard = get_keyboard(step_num)
        
        has_photo = query.message.photo is not None
        
        if step.get("image"):
            image_path = get_image_path(step["image"])
            if os.path.exists(image_path):
                with open(image_path, 'rb') as photo:
                    media = InputMediaPhoto(
                        media=photo,
                        caption=message
                    )
                    try:
                        await query.edit_message_media(
                            media=media,
                            reply_markup=keyboard
                        )
                    except Exception as e:
                        logger.error(f"Error editing media: {e}")
                        await query.delete_message()
                        await context.bot.send_photo(
                            chat_id=query.message.chat_id,
                            photo=photo,
                            caption=message,
                            reply_markup=keyboard
                        )
            else:
                if has_photo:
                    await query.delete_message()
                    await context.bot.send_message(
                        chat_id=query.message.chat_id,
                        text=message,
                        reply_markup=keyboard
                    )
                else:
                    await query.edit_message_text(
                        text=message,
                        reply_markup=keyboard
                    )
        else:
            if has_photo:
                await query.delete_message()
                await context.bot.send_message(
                    chat_id=query.message.chat_id,
                    text=message,
                    reply_markup=keyboard
                )
            else:
                await query.edit_message_text(
                    text=message,
                    reply_markup=keyboard
                )
    
    elif callback_data == "noop":
        await query.answer("Use Back or Next to navigate", show_alert=False)

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Log errors"""
    logger.error(f"Update {update} caused error {context.error}")

def main() -> None:
    """Start the bot"""
    application = Application.builder().token(TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("step", step_command))
    application.add_handler(CallbackQueryHandler(button_callback))
    
    application.add_error_handler(error_handler)
    
    print("🤖 UARC Printing Bot is running (11 steps)...")
    print("📸 Bot will load images from local directory")
    print("Press Ctrl+C to stop")
    
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
