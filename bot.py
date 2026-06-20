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
    PREMIUM_STOCK = {
    "TOP_SELLING": [
        "⚡ Vapi – 200 USD Credits (12M)\n",
        "⚡ Perplexity Pro – 1Y\n",
        "⚡ Beautiful.ai Pro – 1Y\n",
        "⚡ Gamma.AI Pro – 1Y\n",
        "⚡ N8N Starter – 1Y\n",
        "⚡ Replit Core – 1Y\n",
        "⚡ Raycast Pro – 1Y\n",
        "⚡ Superhuman Starter – 1Y\n",
        "⚡ Linear Business – 1Y\n",
        "⚡ Granola Business – 1Y\n",
        "⚡ Webflow CMS – 1Y\n",
        "⚡ Webflow Business – 1Y\n",
        "⚡ Webflow Growth – 1Y\n",
        "⚡ Notion Business + AI – 3M / 6M\n",
        "⚡ Otter.ai Pro – 1Y\n",
        "⚡ ClickUp Enterprise – 1Y\n"
    ],
    "AI_DESIGN_CREATIVITY": [
        "🎨 Beautiful.ai Pro – 1Y\n",
        "🎨 Magic Patterns Hobby – 1Y\n",
        "🖼️ Slidebean Starter – 1Y\n",
        "🖼️ PNGTree Premium – Lifetime\n",
        "🖼️ Pixpa Pro – 6M\n",
        "🖼️ Pikbest Premium – 1Y\n",
        "🎞️ Flixier Pro – 1Y\n",
        "🎬 Movavi Unlimited (1 PC) – 1Y\n",
        "🎨 Rive.app Cadet – 1Y\n",
        "🎨 3D Swymer + Creator + Collaborative Industry Innovator – 1Y\n",
        "🎨 3D Swymer + Sculptor + Collaborative Industry Innovator – 1Y\n",
        "🎨 3D Swymer + Collaborative Industry Innovator – 1Y\n"
    ],
    "AI_TOOLS": [
        "🤖 Mobbin Pro – 1Y\n",
        "🤖 ChatPRD Pro – 1Y\n",
        "🔍 Perplexity Pro – 1Y\n",
        "⚡ Raycast Pro – 1Y\n",
        "🧠 Wispr Flow Pro – 1Y\n",
        "🧠 Reclaim AI Starter – 1Y\n",
        "🤖 Fireflies Pro – 1Y\n",
        "🤖 Fireflies Business – 1Y\n",
        "🤖 Consensus Pro – 1Y\n",
        "🤖 Dreamlit Pro – 6M\n",
        "🤖 Firecrawl AI – 50K Credits (1Y)\n",
        "🤖 AppWrite Pro – 4M\n"
    ],
    "BUSINESS_MARKETING_PRODUCTIVITY": [
        "📬 Enginemailer Free Forever 10K/mo – Lifetime\n",
        "📈 Gummysearch Pro – 1M\n",
        "📊 Requestly Pro – 6M\n",
        "📊 Full Enrich Pro (1000 Credits) – 1M\n",
        "🎥 Screenspace.io Launch – 1M\n",
        "🖼️ Clipping Mini – 3M\n",
        "⚙️ Trace Pro – 3M\n",
        "⚙️ Trace Teams – 3M\n",
        "📈 Viral Launch Core – 1M\n",
        "📈 Viral Launch Growth – 1M\n",
        "📊 Keyword Hero – 6M\n",
        "📨 Typefully Creator / Team / Agency – 1M\n",
        "📨 Postiz (Standard / Teams / Pro / Ultimate) – 1M\n",
        "📨 Planoly Social Planner Starter – 1Y\n",
        "📊 SmartScout (Basic / Essentials) – 1M\n",
        "📊 AMZScout AI Bundle – 1M\n",
        "📊 Omnisend Standard – 3M\n",
        "📊 Schematic Growth – 1M\n"
    ],
    "WEB_DEV_CLOUD_HOSTING": [
        "🌐 Webflow CMS – 1Y\n",
        "🌐 Webflow Business – 1Y\n",
        "🌐 Webflow Growth – 1Y\n",
        "☁️ Hostinger Cloud Startup – 1Y\n",
        "☁️ Backblaze Cloud Unlimited Backup – 1Y\n",
        "☁️ SendAnywhere Lite / Standard – 1Y\n",
        "☁️ WeTransfer Ultimate – 1Y\n",
        "☁️ AppWrite Pro – 4M\n",
        "☁️ Exa AI Websets – 8000 Credits (14D)\n",
        "☁️ Exa AI API – 50 USD Credits (1Y)\n",
        "🛠️ PostHog Scale – 1Y\n",
        "🛠️ AppWizzy Basic – 1M\n",
        "🛠️ OpenArt AI Advanced – 1M\n"
    ],
    "EDU_CAREER_LEARNING": [
        "🎓 Rezi AI – Lifetime\n",
        "🎓 Scrimba Pro – 1Y\n",
        "📚 PNGTree Premium – Lifetime\n",
        "📚 No Code MBA Unlimited – 1M\n",
        "📚 Whizlabs Premium / Premium Plus – 1M\n",
        "📚 Whizlabs Premium – 1Y\n",
        "📝 Paperpal Prime – 1M\n",
        "💼 LinkedIn Career Premium – 3M\n"
    ],
    "CAD_3D_ENGINEERING": [
        "🟣 3D Swymer + Creator + Collaborative Industry Innovator – 1Y\n",
        "🟣 3D Swymer + Sculptor + Collaborative Industry Innovator – 1Y\n",
        "🟣 3DEXPERIENCE SOLIDWORKS Pro + Swymer + Collaborative Industry Innovator – 1Y\n",
        "🟣 3D Swymer + Collaborative Industry Innovator – 1Y\n",
        "🟣 3D Swymer + NC Shop Floor Programmer + Collaborative Industry Innovator – 1Y\n",
        "🟣 Full 6-Product 3D Suite – 1Y\n"
    ],
    "SHORT_TERM_POWER_DEALS": [
        "🧠 Jasper AI Pro – 1M\n",
        "🧠 Lex Pro – 1M\n",
        "⚡ CodeRabbit Pro – 1M / 2M\n",
        "⚡ FlutterFlow Premium – 2M\n",
        "✨ Cosine.sh Hobby / Pro – 1M\n",
        "📚 Figma Pro – 1M\n",
        "☁️ Cloudinary Plus – 1M\n",
        "📝 Wordtune Unlimited – 1M\n",
        "🔍 Notion Business + AI – 3M / 6M\n",
        "⚙️ Sentry.io Teams – 1Y\n",
        "⚙️ Sentry.io Business – 1Y\n",
        "🔧 CreeperSEOAudit Standard / Pro – 6M\n",
        "📝 Jenni Unlimited – 1M\n",
        "📚 Ebookmaker.ai Starter / Creator / Enterprise – 1M\n",
        "🧠 Humanic AI Growth / Scale – 1M\n",
        "🧪 Dev.to Plus Plus – 1M\n",
        "📁 Airtable Teams / Business – 1M\n",
        "🧰 Frame.io Teams – 3M\n",
        "🧰 Zeplin Advanced – 1Y\n",
        "🧰 Miro Business – 3M\n",
        "🧰 Miro Starter (1 Seat) – 1Y\n",
        "🧰 AhaSlides Essentials / Pro – 12M\n"
    ],
    "SECURITY_DEV_TOOLS": [
        "🔐 Bitwarden Premium + Family – 1Y\n",
        "💻 GitLab Ultimate – 12M\n",
        "💻 IntelliJ IDEA Ultimate – 3M / 6M\n",
        "💻 PyCharm Pro – 6M\n",
        "🧪 Postman Basic – 1Y\n",
        "🛠️ Sentry.io Teams / Business – 1Y\n",
        "🛠️ Requestly Pro – 6M\n",
        "🛠️ Termly.io Starter / Pro+ – 1Y\n"
    ],
    "VIDEO_AUDIO_CONTENT": [
        "🎥 Flixier Pro – 1Y\n",
        "🎥 Tella Pro / Premium – 1M\n",
        "🎥 Restream.io Standard – 1Y\n",
        "🎥 LiveReacting Small / Medium / 24/7 / Countdown – 1M\n",
        "🎧 Moises AI Premium / Pro – 1Y\n",
        "🎧 MusicGPT Ultra – 1M\n",
        "🎙️ Augie Studio Unlimited – 1M\n",
        "🎙️ Fireflies Pro / Business – 1Y / 1M\n",
        "🎙️ Maestra AI Premium – 1M\n"
    ],
    "SOCIAL_BRANDING_LANDING": [
        "🔗 Linktree Pro – 1Y / 3M\n",
        "📄 Pagemaker Pro / Agency – 1Y\n",
        "📄 Framer Basic / Pro – 1Y\n",
        "📄 Tilda Personal – 1Y\n",
        "📄 PluginsForWP Unlimited Downloads – 1Y\n",
        "📄 Trendtrack Starter / Pro / Business – 1M\n"
    ],
    "MISC_PREMIUM": [
        "🧠 ZeroEssay Premium – 1M\n",
        "🧠 ComputerX AI Pro / Premium – 1M\n",
        "🧠 Dynal AI Starter / Pro / Ultimate – 1M\n",
        "🧠 Reforge AI Build – 1M\n",
        "📷 Letsenhance Starter / Pro / Max – 1M\n",
        "📷 Tripo Studio Pro / Advanced / Premium – 1M\n",
        "📷 Collov AI Standard / Advanced / Premium – 1M\n",
        "📊 Scalelist Scaler (3000 Credits) – 1M\n",
        "📊 Gencraft AI Pro – 1M\n",
        "📊 Trendtrack Starter / Pro / Business – 1M\n"
    ]
}
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
  
