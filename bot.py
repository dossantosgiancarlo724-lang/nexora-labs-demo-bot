import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
)

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

PLATFORM_LINKS = {
    "fiverr": "INSERISCI_QUI_IL_LINK_FIVERR",
    "freelancer": "INSERISCI_QUI_IL_LINK_FREELANCER",
    "workana": "INSERISCI_QUI_IL_LINK_WORKANA",
    "upwork": "INSERISCI_QUI_IL_LINK_UPWORK",
}


def main_menu():
    keyboard = [
        [
            InlineKeyboardButton("🧠 AI Solutions", callback_data="ai"),
            InlineKeyboardButton("🤖 Telegram Bots", callback_data="telegram"),
        ],
        [
            InlineKeyboardButton("⚙️ Automation", callback_data="automation"),
            InlineKeyboardButton("🔗 API Integrations", callback_data="api"),
        ],
        [
            InlineKeyboardButton("🌐 Web Solutions", callback_data="web"),
            InlineKeyboardButton("📊 Business Tools", callback_data="business"),
        ],
        [
            InlineKeyboardButton("🛍️ E-commerce Automation", callback_data="ecommerce"),
            InlineKeyboardButton("💬 Chatbots", callback_data="chatbots"),
        ],
        [
            InlineKeyboardButton("📩 Request a Project", callback_data="project"),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🚀 <b>NEXORA LABS</b>\n\n"
        "AI • AUTOMATION • BOTS • INTEGRATIONS\n\n"
        "Explore our interactive demos and discover "
        "what Nexora Labs can build for you."
    )

    await update.message.reply_text(
        text,
        parse_mode="HTML",
        reply_markup=main_menu(),
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data

    if data == "ai":
        text = (
            "🧠 <b>AI SOLUTIONS</b>\n\n"
            "We build practical AI-powered solutions for businesses.\n\n"
            "• AI assistants\n"
            "• Intelligent customer support\n"
            "• AI content workflows\n"
            "• Automated data processing\n"
            "• Custom AI integrations"
        )

    elif data == "telegram":
        text = (
            "🤖 <b>TELEGRAM BOTS</b>\n\n"
            "Interactive and automated Telegram solutions.\n\n"
            "• Custom bots\n"
            "• Notifications\n"
            "• User management\n"
            "• Interactive menus\n"
            "• Automated publishing\n"
            "• API integrations"
        )

    elif data == "automation":
        text = (
            "⚙️ <b>AUTOMATION</b>\n\n"
            "Turn repetitive tasks into automated workflows.\n\n"
            "Example:\n\n"
            "📩 Trigger\n"
            "↓\n"
            "🤖 Processing\n"
            "↓\n"
            "⚙️ Automation\n"
            "↓\n"
            "📤 Action"
        )

    elif data == "api":
        text = (
            "🔗 <b>API INTEGRATIONS</b>\n\n"
            "Connect your services and applications.\n\n"
            "Example:\n\n"
            "Telegram → API → Database → Response\n\n"
            "We can build custom integrations around "
            "authorized APIs and services."
        )

    elif data == "web":
        text = (
            "🌐 <b>WEB SOLUTIONS</b>\n\n"
            "Modern digital solutions for your business.\n\n"
            "• Landing pages\n"
            "• Web dashboards\n"
            "• Client portals\n"
            "• API-connected websites\n"
            "• Automation interfaces"
        )

    elif data == "business":
        text = (
            "📊 <b>BUSINESS TOOLS</b>\n\n"
            "Custom tools designed to simplify business operations.\n\n"
            "• Dashboards\n"
            "• Statistics\n"
            "• User management\n"
            "• Automated reports\n"
            "• Workflow management"
        )

    elif data == "ecommerce":
        text = (
            "🛍️ <b>E-COMMERCE AUTOMATION — LIVE DEMO</b>\n\n"
            "🔥 SUPER DEAL – DEMO\n\n"
            "🎮 PlayStation 5 Slim\n"
            "━━━━━━━━━━━━━━━━\n"
            "💸 Before: €549.00\n"
            "✅ Now: €449.00\n"
            "📉 Discount: -18.21%\n"
            "💰 You save: €100.00\n"
            "━━━━━━━━━━━━━━━━\n\n"
            "This demo shows how an automation system "
            "can process product information and calculate "
            "discounts automatically."
        )

    elif data == "chatbots":
        text = (
            "💬 <b>CHATBOTS</b>\n\n"
            "Smart conversational experiences for businesses.\n\n"
            "• Customer support\n"
            "• FAQ assistants\n"
            "• Lead generation\n"
            "• Booking assistants\n"
            "• Sales assistants"
        )

    elif data == "project":
        keyboard = [
            [
                InlineKeyboardButton(
                    "💼 Fiverr",
                    url=PLATFORM_LINKS["fiverr"],
                )
            ],
            [
                InlineKeyboardButton(
                    "💼 Freelancer",
                    url=PLATFORM_LINKS["freelancer"],
                )
            ],
            [
                InlineKeyboardButton(
                    "💼 Workana",
                    url=PLATFORM_LINKS["workana"],
                )
            ],
            [
                InlineKeyboardButton(
                    "💼 Upwork",
                    url=PLATFORM_LINKS["upwork"],
                )
            ],
            [
                InlineKeyboardButton(
                    "⬅️ Back",
                    callback_data="back",
                )
            ],
        ]

        text = (
            "🚀 <b>Ready to get started?</b>\n\n"
            "Continue your project with <b>Nexora Labs</b> "
            "on your preferred platform."
        )

        await query.edit_message_text(
            text,
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )
        return

    elif data == "back":
        await query.edit_message_text(
            "🚀 <b>NEXORA LABS</b>\n\n"
            "AI • AUTOMATION • BOTS • INTEGRATIONS\n\n"
            "Explore our interactive demos:",
            parse_mode="HTML",
            reply_markup=main_menu(),
        )
        return

    else:
        return

    keyboard = [
        [InlineKeyboardButton("⬅️ Back to Demo", callback_data="back")]
    ]

    await query.edit_message_text(
        text,
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


def run():
    if not TOKEN:
        raise RuntimeError(
            "TELEGRAM_BOT_TOKEN is not configured."
        )

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("Nexora Labs Demo Bot is running...")

    app.run_polling()


if __name__ == "__main__":
    run()
