import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# --- 1. CONFIGURATION & BOT IDENTITY ---
# Paste your actual bot token received from @BotFather inside the quotes below
BOT_TOKEN = "8621695726:AAHyzRi4DWUGl0X2UG36KWSiUCSz0JXgU2c"

bot = telebot.TeleBot(BOT_TOKEN)

CONTACT_USERNAME = "sahulrmehta"

# --- 2. TEXT CONSTANTS ---
TEXT_START = (
    "🌟 *Welcome to Digital Products Marketplace* 🌟\n\n"
    "Explore our premium AI tool bundles, OTT streaming setups, social presence boosts, and automated affiliate resources.\n\n"
    "Select a category below to browse:"
)

TEXT_TOOLS = (
    "🚀⚡ *ULTIMATE AI STARTUP & PRODUCTIVITY BUNDLE* ⚡🚀\n\n"
    "🎨 Canva Business — 1 Year\n"
    "💻 Cursor Pro — 1 Year\n"
    "🗣️ ElevenLabs Creator — 1 Year\n"
    "📊 Gamma Pro — 1 Year\n"
    "🤖 Google AI Pro — 1 Year\n"
    "🚀 Lovable Pro — 1 Year\n"
    "⚙️ n8n Cloud Starter — 1 Year\n"
    "🛢️ Supabase Pro Credits — 1 Year\n"
    "📝 ChatPRD Pro — 1 Year\n"
    "🏭 Factory Pro — 1 Year\n"
    "🎨 Framer Pro — 1 Year\n"
    "📒 Granola Business (10 Seats) — 1 Year\n"
    "🤖 Gumloop Pro (20K Credits/Month) — 1 Year\n"
    "💬 Intercom Fin AI + Advanced — 1 Year\n"
    "📈 Linear Business (5 Seats) — 1 Year\n"
    "🎭 Manus AI (4K Credits/Month) — 1 Year\n"
    "📱 Mobbin Team (10 Seats) — 1 Year\n"
    "🧠 Notion Business — 1 Year\n"
    "📊 PostHog Scale — 1 Year\n"
    "🚄 Railway Hobby — 1 Year\n"
    "💻 Replit Core — 1 Year\n"
    "⚡ Warp Build — 1 Year\n"
    "🎙️ Wispr Flow Pro — 1 Year\n"
    "🎨 Magic Patterns Starter — 1 Year\n"
    "🏢 Stripe Atlas — 40% OFF\n\n"
    "-----------------------------------------\n\n"
    "🚀 *WARP DEV – NOW AVAILABLE* 🚀\n\n"
    "👉🏻 Plan - Build\n"
    "⌛ Validity: 01 Year\n"
    "📧 Activation on your Personal Email ID\n\n"
    "❌ Original Price: $200 = ₹17,627.80 ❌\n"
    "✅ *OUR OFFER PRICE: Rs 3,999/- Only*\n\n"
    "🔥 *THE AGENTIC DEVELOPMENT ENVIRONMENT*\n"
    "Warp is the fastest way to build with multiple AI agents—from writing code to shipping it.\n\n"
    "🎯 *WHAT YOU WILL GET:*\n"
    "✅ Blazing-fast performance (built in Rust)\n"
    "✅ AI command suggestions & explanations\n"
    "✅ Block-based workflow – edit like a doc\n"
    "✅ Autocomplete, syntax highlighting & instant output\n"
    "✅ Built-in AI assistant to write commands and debug\n\n"
    "🎯 *Work Smarter—Private Activation, Grab it Before it's Gone!*"
)

TEXT_OTT = (
    "✨ 🔥 *PREMIUM STREAMING & MUSIC PLATFORMS* 🔥 ✨\n\n"
    "🍿 *Amazon Prime Video:*\n"
    "• Unlimited Movies, Web Series & Amazon Originals!\n\n"
    "🎬 *Premium OTT Accounts:*\n"
    "• Netflix (Private / Shared Screen)\n"
    "• Disney+ Hotstar Super/Premium\n"
    "• Zee5 Premium\n\n"
    "🔴 *YouTube Premium:*\n"
    "• Ad-free streaming, background play, and YT Music.\n\n"
    "🎵 *Spotify Premium:*\n"
    "• Offline downloads & ad-free high-quality music loops."
)

TEXT_SERVICES = (
    "🛠️ *OUR DIGITAL SERVICES*\n\n"
    "🎨 *Graphic Design*\n"
    "• Custom Branding, Marketing Posters, and Logos.\n\n"
    "🎬 *Video Editing*\n"
    "• High-converting editing for Reels, YouTube, and Ads."
)

TEXT_VIRTUAL = (
    "📱 *VIRTUAL ACCOUNTS*\n\n"
    "Get verified channels or bulk virtual setups for business growth:\n\n"
    "• WhatsApp Marketing/Bulk Accounts\n"
    "• Telegram Accounts & Scraper Groups"
)

TEXT_DEALS = (
    "💰 *BEST DEALS & AFFILIATE PROGRAMMES*\n\n"
    "Maximize your earnings with our curated affiliate setup loops:\n"
    "🛍️ Flipkart Affiliate Setup\n"
    "📦 Amazon Associate Integrations\n"
    "👗 Meesho Reselling Strategy"
)

TEXT_SOCIAL_GROWTH = (
    "🚀 *SOCIAL GROWTH — BOOST YOUR SOCIAL PRESENCE!* 🚀\n\n"
    "👁️ *INSTAGRAM VIEWS*\n"
    "• 1k Views ➔ ₹3\n"
    "• 5k Views ➔ ₹7\n"
    "• 10k Views ➔ ₹10\n"
    "• 15k Views ➔ ₹20\n"
    "• 20k Views ➔ ₹35\n"
    "• 60k Views ➔ ₹79\n"
    "• 100k Views ➔ ₹149\n"
    "• 1M Views ➔ ₹399\n\n"
    "👤 *INSTAGRAM FOLLOWERS*\n"
    "• 100 Followers ➔ ₹20\n"
    "• 200 Followers ➔ ₹30\n"
    "• 300 Followers ➔ ₹50\n"
    "• 500 Followers ➔ ₹100\n"
    "• 1k Followers ➔ ₹120\n"
    "• 2k Followers ➔ ₹209\n"
    "• 3k Followers ➔ ₹399\n"
    "• 5k Followers ➔ ₹649\n"
    "• 10k Followers ➔ ₹999\n\n"
    "❤️ *INSTAGRAM LIKES*\n"
    "• 100 Likes ➔ ₹7\n"
    "• 200 Likes ➔ ₹10\n"
    "• 300 Likes ➔ ₹20\n"
    "• 500 Likes ➔ ₹30\n"
    "• 1k Likes ➔ ₹50\n"
    "• 2k Likes ➔ ₹80\n"
    "• 5k Likes ➔ ₹200\n"
    "• 10k Likes ➔ ₹400\n\n"
    "🔥 *PLATFORMS AVAILABLE:*\n"
    "📸 Instagram | 👥 Facebook | 🎥 YouTube | 🎵 TikTok | ✈️ Telegram | 👻 Snapchat\n\n"
    "✔️ All Genuine Services | ⚡ Fast Delivery | 🔒 100% Safe & Secure"
)

TEXT_COURSES = (
    "📈 *PREMIUM BUSINESS COURSES & LEARNING* 📈\n\n"
    "📚 *Reselling Business Mastery*\n"
    "• Complete A-to-Z setup to start a profitable flipping business with zero investment.\n\n"
    "🤖 *AI Automation Agency (AAA) Course*\n"
    "• Learn how to build AI chatbots and automate workflows for businesses using n8n, Zapier, and ChatGPT.\n\n"
    "💻 *Freelancing & Agency Scaling*\n"
    "• How to get high-ticket clients on Upwork/LinkedIn and scale your digital service agency.\n\n"
    "🎯 *Digital Marketing Pro*\n"
    "• Master Meta Ads (FB/Insta), Google Ads, and organic brand growth frameworks."
)


# --- 3. KEYBOARD HELPER CONFIGURATIONS ---
def get_main_keyboard():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton("🚀 AI Tools & Bundles", callback_data="menu_tools"),
        InlineKeyboardButton("📺 OTT Premium Platforms", callback_data="menu_ott"),
        InlineKeyboardButton("🚀 Social Growth (SMM Panel)", callback_data="menu_growth"),
        InlineKeyboardButton("📈 Premium Business Courses", callback_data="menu_courses"),
        InlineKeyboardButton("📱 Virtual Accounts (WA/TG)", callback_data="menu_virtual"),
        InlineKeyboardButton("🛠️ Graphics & Video Editing", callback_data="menu_services"),
        InlineKeyboardButton("💰 Best Deals & Affiliate", callback_data="menu_deals"),
        InlineKeyboardButton("📢 Official Channels & Help Groups", callback_data="menu_whatsapp_links")
    )
    return markup

def get_contact_keyboard(back_target="back_to_main"):
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton("📩 DM TO PLACE ORDER", url=f"https://t.me/{CONTACT_USERNAME}"),
        InlineKeyboardButton("⬅️ Back Menu", callback_data=back_target)
    )
    return markup

def get_country_keyboard():
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(
        InlineKeyboardButton("🇮🇳 India", url=f"https://t.me/{CONTACT_USERNAME}"),
        InlineKeyboardButton("🇺🇸 USA", url=f"https://t.me/{CONTACT_USERNAME}"),
        InlineKeyboardButton("🇧🇩 Bangladesh", url=f"https://t.me/{CONTACT_USERNAME}"),
        InlineKeyboardButton("🇿🇲 Zambia", url=f"https://t.me/{CONTACT_USERNAME}"),
        InlineKeyboardButton("🇲🇲 Myanmar", url=f"https://t.me/{CONTACT_USERNAME}"),
        InlineKeyboardButton("🇻🇪 Venezuela", url=f"https://t.me/{CONTACT_USERNAME}"),
        InlineKeyboardButton("🇸🇦 Saudi Arabia", url=f"https://t.me/{CONTACT_USERNAME}"),
        InlineKeyboardButton("🇷🇺 Russia", url=f"https://t.me/{CONTACT_USERNAME}"),
        InlineKeyboardButton("🇨🇴 Colombia", url=f"https://t.me/{CONTACT_USERNAME}"),
        InlineKeyboardButton("🇦🇪 UAE", url=f"https://t.me/{CONTACT_USERNAME}"),
        InlineKeyboardButton("🇵🇰 Pakistan", url=f"https://t.me/{CONTACT_USERNAME}")
    )
    markup.add(InlineKeyboardButton("⬅️ Back Menu", callback_data="back_to_main"))
    return markup

def get_whatsapp_links_keyboard():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton("📢 Earning Ways", url="https://whatsapp.com/channel/0029VbD0mvZJpe8jF3cSLZ1x"),
        InlineKeyboardButton("🛍️ Flipkart Affiliate", url="https://whatsapp.com/channel/0029VbCcFzSDOQIPq0DLaC1d"),
        InlineKeyboardButton("📦 Amazon Affiliate", url="https://whatsapp.com/channel/0029VbD8vtAJ3jv7tYHBza0J"),
        InlineKeyboardButton("👗 Meesho Affiliate", url="https://whatsapp.com/channel/0029VbChVAeIt5rw1WIgES2W"),
        InlineKeyboardButton("🤝 Marketplace Help Group", url="https://chat.whatsapp.com/EAwfi9imerA9IuTCjcAnYp?s=cl&p=a&ilr=2"),
        InlineKeyboardButton("📱 Digital Products Group", url="https://chat.whatsapp.com/HVjbG9zCUM71XR651yDSHk?s=cl&p=a&ilr=2"),
        InlineKeyboardButton("🌐 Marketplace Community Group", url="https://chat.whatsapp.com/ESmzI0J2mbJLnmAoWFPAGf?s=cl&p=a&ilr=2"),
        InlineKeyboardButton("⬅️ Back Menu", callback_data="back_to_main")
    )
    return markup


# --- 4. COMMAND HANDLERS ---
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, TEXT_START, reply_markup=get_main_keyboard(), parse_mode="Markdown")


# --- 5. INTERACTIVE CALLBACK ROUTER ---
@bot.callback_query_handler(func=lambda call: True)
def handle_menu_navigation(call):
    # Dynamic acknowledgment to clear loading animations
    bot.answer_callback_query(call.id)
    
    if call.data == "back_to_main":
        bot.edit_message_text(TEXT_START, call.message.chat.id, call.message.message_id, reply_markup=get_main_keyboard(), parse_mode="Markdown")
        
    elif call.data == "menu_tools":
        bot.edit_message_text(TEXT_TOOLS, call.message.chat.id, call.message.message_id, reply_markup=get_contact_keyboard(), parse_mode="Markdown")
        
    elif call.data == "menu_ott":
        bot.edit_message_text(TEXT_OTT, call.message.chat.id, call.message.message_id, reply_markup=get_contact_keyboard(), parse_mode="Markdown")
        
    elif call.data == "menu_growth":
        bot.edit_message_text(TEXT_SOCIAL_GROWTH, call.message.chat.id, call.message.message_id, reply_markup=get_contact_keyboard(), parse_mode="Markdown")
        
    elif call.data == "menu_courses":
        bot.edit_message_text(TEXT_COURSES, call.message.chat.id, call.message.message_id, reply_markup=get_contact_keyboard(), parse_mode="Markdown")
        
    elif call.data == "menu_services":
        bot.edit_message_text(TEXT_SERVICES, call.message.chat.id, call.message.message_id, reply_markup=get_contact_keyboard(), parse_mode="Markdown")
        
    elif call.data == "menu_deals":
        bot.edit_message_text(TEXT_DEALS, call.message.chat.id, call.message.message_id, reply_markup=get_contact_keyboard(), parse_mode="Markdown")
        
    elif call.data == "menu_virtual":
        virtual_instruction_text = f"{TEXT_VIRTUAL}\n\n🌐 *Select target proxy country location to verify live stock allocations:* "
        bot.edit_message_text(virtual_instruction_text, call.message.chat.id, call.message.message_id, reply_markup=get_country_keyboard(), parse_mode="Markdown")
        
    elif call.data == "menu_whatsapp_links":
        links_display_text = (
            "📢 *DIGITAL PRODUCTS MARKETPLACE OFFICIAL CHANNELS & GROUPS*\n\n"
            "Stay up-to-date with immediate deal metrics and peer connection loops. Select a link below to open directly in WhatsApp:"
        )
        bot.edit_message_text(links_display_text, call.message.chat.id, call.message.message_id, reply_markup=get_whatsapp_links_keyboard(), parse_mode="Markdown")


# --- 6. RUNTIME SCRIPT EXECUTION ---
if __name__ == "__main__":
    print("Digital Products Marketplace bot instance is successfully running...")
    bot.infinity_polling()
  
