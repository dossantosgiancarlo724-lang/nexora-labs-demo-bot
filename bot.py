import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
)

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


# =========================
# MAIN MENU
# =========================

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
            InlineKeyboardButton(
                "🛍️ E-commerce Automation",
                callback_data="ecommerce",
            )
        ],
        [
            InlineKeyboardButton("💬 Chatbots", callback_data="chatbots"),
        ],
        [
            InlineKeyboardButton(
                "📩 Request a Project",
                callback_data="project",
            )
        ],
    ]

    return InlineKeyboardMarkup(keyboard)


# =========================
# START
# =========================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = (
        "🚀 <b>NEXORA LABS</b>\n\n"
        "<b>AI • AUTOMATION • BOTS • INTEGRATIONS</b>\n\n"
        "Welcome to our interactive demo.\n\n"
        "Explore our services and see what "
        "Nexora Labs can build for you."
    )

    await update.message.reply_text(
        text,
        parse_mode="HTML",
        reply_markup=main_menu(),
    )


# =========================
# BUTTON HANDLER
# =========================

async def button_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    query = update.callback_query
    await query.answer()

    data = query.data

    # -------------------------
    # AI
    # -------------------------

    if data == "ai":

        text = (
            "🧠 <b>AI SOLUTIONS</b>\n\n"
            "We build practical AI-powered solutions "
            "designed around real business needs.\n\n"
            "• AI assistants\n"
            "• Customer support AI\n"
            "• AI content workflows\n"
            "• Intelligent data processing\n"
            "• Custom AI integrations"
        )

    # -------------------------
    # TELEGRAM BOTS
    # -------------------------

    elif data == "telegram":

        text = (
            "🤖 <b>TELEGRAM BOTS</b>\n\n"
            "Custom Telegram bots for automation "
            "and business workflows.\n\n"
            "• Interactive menus\n"
            "• Notifications\n"
            "• User management\n"
            "• Automated publishing\n"
            "• Admin systems\n"
            "• API integrations"
        )

    # -------------------------
    # AUTOMATION
    # -------------------------

    elif data == "automation":

        text = (
            "⚙️ <b>AUTOMATION</b>\n\n"
            "Turn repetitive tasks into automated workflows.\n\n"
            "<b>Example workflow:</b>\n\n"
            "📩 Trigger\n"
            "   ↓\n"
            "🤖 Processing\n"
            "   ↓\n"
            "⚙️ Automation\n"
            "   ↓\n"
            "📤 Automatic Action\n\n"
            "Designed to save time and reduce repetitive work."
        )

    # -------------------------
    # API
    # -------------------------

    elif data == "api":

        text = (
            "🔗 <b>API INTEGRATIONS</b>\n\n"
            "Connect applications and services through "
            "authorized APIs.\n\n"
            "<b>Example:</b>\n\n"
            "Telegram\n"
            "↓\n"
            "API\n"
            "↓\n"
            "Database\n"
            "↓\n"
            "Automatic Response"
        )

    # -------------------------
    # WEB
    # -------------------------

    elif data == "web":

        text = (
            "🌐 <b>WEB SOLUTIONS</b>\n\n"
            "Modern web solutions connected to your "
            "business workflows.\n\n"
            "• Landing pages\n"
            "• Web dashboards\n"
            "• Client portals\n"
            "• Custom interfaces\n"
            "• API-connected websites"
        )

    # -------------------------
    # BUSINESS
    # -------------------------

    elif data == "business":

        text = (
            "📊 <b>BUSINESS TOOLS</b>\n\n"
            "Custom digital tools that simplify "
            "business operations.\n\n"
            "• Dashboards\n"
            "• Statistics\n"
            "• User management\n"
            "• Reports\n"
            "• Workflow management\n"
            "• Internal tools"
        )

    # -------------------------
    # E-COMMERCE
    # -------------------------

    elif data == "ecommerce":

        original_price = 1159.00
        current_price = 1059.00

        savings = original_price - current_price
        discount = (savings / original_price) * 100

        text = (
            "🛍️ <b>E-COMMERCE AUTOMATION</b>\n\n"
            "🔥 <b>SUPER DEAL – LIVE DEMO</b>\n\n"
            "🎮 Apple iPad Air 13\" M4\n"
            "━━━━━━━━━━━━━━━━\n"
            f"💸 Before: <s>€{original_price:,.2f}</s>\n"
            f"✅ Now: <b>€{current_price:,.2f}</b>\n"
            f"📉 Discount: <b>-{discount:.0f}%</b>\n"
            f"💰 You save: <b>€{savings:,.2f}</b>\n"
            "━━━━━━━━━━━━━━━━\n\n"
            "This demo automatically calculates the "
            "discount from the original and current prices."
        )

    # -------------------------
    # CHATBOTS
    # -------------------------

    elif data == "chatbots":

        text = (
            "💬 <b>CHATBOTS</b>\n\n"
            "Conversational solutions designed for businesses.\n\n"
            "• Customer support\n"
            "• FAQ assistants\n"
            "• Lead generation\n"
            "• Booking assistants\n"
            "• Sales assistants\n"
            "• Automated responses"
        )

    # -------------------------
    # REQUEST PROJECT
    # -------------------------

    elif data == "project":

        text = (
            "🚀 <b>Ready to get started?</b>\n\n"
            "Continue your project with "
            "<b>Nexora Labs</b> on your preferred platform.\n\n"
            "Please return to the platform where you "
            "are currently discussing your project with "
            "<b>Nexora Labs</b>."
        )

        keyboard = [
            [
                InlineKeyboardButton(
                    "⬅️ Back to Demo",
                    callback_data="back",
                )
            ]
        ]

        await query.edit_message_text(
            text,
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )

        return

    # -------------------------
    # BACK
    # -------------------------

    elif data == "back":

        text = (
            "🚀 <b>NEXORA LABS</b>\n\n"
            "<b>AI • AUTOMATION • BOTS • INTEGRATIONS</b>\n\n"
            "Explore our interactive demos:"
        )

        await query.edit_message_text(
            text,
            parse_mode="HTML",
            reply_markup=main_menu(),
        )

        return

    else:
        return

    # -------------------------
    # BACK BUTTON FOR SERVICES
    # -------------------------

    keyboard = [
        [
            InlineKeyboardButton(
                "⬅️ Back to Demo",
                callback_data="back",
            )
        ]
    ]

    await query.edit_message_text(
        text,
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


# =========================
# RUN BOT
# =========================

def main():

    if not TOKEN:
        raise RuntimeError(
            "TELEGRAM_BOT_TOKEN is not configured."
        )

    application = (
        Application
        .builder()
        .token(TOKEN)
        .build()
    )

    application.add_handler(
        CommandHandler("start", start)
    )

    application.add_handler(
        CallbackQueryHandler(button_handler)
    )

    print("🚀 Nexora Labs Demo Bot is running...")

    application.run_polling()


if __name__ == "__main__":
    main()
