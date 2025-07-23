import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    CallbackQueryHandler,
)

# Configurações
TOKEN = "7521462337:AAFVvmYHCJKV4X-IWeg6pVRoywxtUppjaSg"
CHANNEL_ID = "-1002576277480"

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

# /start envia logo + legenda, depois envia os botões separadamente
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    with open('logo.png.jpeg', 'rb') as photo:  # ajuste extensão se precisar
        welcome_text = (
            "👋 *Welcome to Spicy Latinas BR!* 🔥\n\n"
            "You’re about to unlock *exclusive access* to the hottest and most authentic Latina content on the web. Here’s what you get as a valued member:\n\n"
            "🌶️ Over *1800 verified OnlyFans Latina models* curated just for you.\n"
            "🎥 Access to more than *500,000 premium adult videos and photos* — all legal and fresh.\n"
            "📅 *Daily updates* so you’ll never miss out on new and exciting content.\n\n"
            "This is more than just a channel — it’s a *private VIP experience* designed to bring you *pleasure, excitement, and entertainment like no other*.\n\n"
            "💡 *Why join us?*\n"
            "Because you deserve *quality, exclusivity*, and a community that values your passion. *No spam, no bots* — just real, top-tier content delivered straight to you.\n\n"
            "🚀 *Ready to dive in?* Choose the plan that fits you best and let the fun begin!"
        )
        await update.message.reply_photo(photo, caption=welcome_text, parse_mode="Markdown")

    # Agora envia os botões numa mensagem separada
    keyboard = [
        [
            InlineKeyboardButton("🔓 7 Days – $7", callback_data='plan_7days'),
            InlineKeyboardButton("📆 Monthly – $17", callback_data='plan_monthly')
        ],
        [
            InlineKeyboardButton("💎 6 Months – $67", callback_data='plan_6months')
        ],
        [InlineKeyboardButton("⚠️ Support: @RayReddingtonBR", callback_data='support')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Choose your plan or contact support:",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

# Botões enviam link na DM e avisam no chat
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == 'plan_7days':
        await context.bot.send_message(
            chat_id=query.from_user.id,
            text=(
                "🔥 You chose the *$7 – 7 Days Plan*.\n\n"
                "[👉 Click here to pay and get access](https://edudigital.mycartpanda.com/checkout/190673843:1)"
            ),
            parse_mode="Markdown",
            disable_web_page_preview=True
        )
        

    elif data == 'plan_monthly':
        await context.bot.send_message(
            chat_id=query.from_user.id,
            text=(
                "📆 You chose the *$17 – Monthly Plan*.\n\n"
                "[👉 Click here to pay and get access](https://edudigital.mycartpanda.com/checkout/190771471:1)"
            ),
            parse_mode="Markdown",
            disable_web_page_preview=True
        )
        

    elif data == 'plan_6months':
        await context.bot.send_message(
            chat_id=query.from_user.id,
            text=(
                "💎 You chose the *$67 – 6 Months Plan*.\n\n"
                "[👉 Click here to pay and get access](https://edudigital.mycartpanda.com/checkout/190771482:1)"
            ),
            parse_mode="Markdown",
            disable_web_page_preview=True
        )
        

    elif data == 'support':
        await query.edit_message_text("🛠 For support, contact @RayReddingtonBR.")

if __name__ == '__main__':
    bot_app = ApplicationBuilder().token(TOKEN).build()

    bot_app.add_handler(CommandHandler("start", start))
    bot_app.add_handler(CallbackQueryHandler(button_handler))

    bot_app.run_polling()
