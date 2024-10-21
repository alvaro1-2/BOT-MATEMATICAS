from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    CallbackQueryHandler,
)
import logging
import random
import time

# Configurar el registro de logs
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Función para manejar errores globalmente
async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Maneja los errores y excepciones."""
    logger.error(msg="Ocurrió un error:", exc_info=context.error)
    # Puedes implementar más lógica aquí si lo deseas, como notificar al administrador, etc.

# Función para iniciar el bot y mostrar el menú principal
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Álgebra 🔢", callback_data='algebra')],
        [InlineKeyboardButton("Trigonometría 📐", callback_data='trigonometria')],
        [InlineKeyboardButton("Aritmética 🧮", callback_data='aritmetica')],
        [InlineKeyboardButton("Geometría 📏", callback_data='geometria')],
        [InlineKeyboardButton("Señor Meeseeks 🔵", callback_data='meeseeks')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    if update.message:
        await update.message.reply_text(
            "📚 *Menú Principal*:\nSeleccione una categoría:",
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )
    elif update.callback_query:
        await update.callback_query.edit_message_text(
            "📚 *Menú Principal*:\nSeleccione una categoría:",
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )

# Función para manejar las interacciones con los botones
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    # Menú principal
    if data == 'algebra':
        keyboard = [
            [InlineKeyboardButton("Números Reales y Complejos", callback_data='numeros_reales_complejos')],
            [InlineKeyboardButton("Ecuaciones e Inecuaciones", callback_data='ecuaciones_inecuaciones')],
            [InlineKeyboardButton("Sistemas de Ecuaciones", callback_data='sistemas_ecuaciones')],
            [InlineKeyboardButton("Expresiones Algebraicas", callback_data='expresiones_algebraicas')],
            [InlineKeyboardButton("Funciones Reales de Variable Real", callback_data='funciones_reales')],
            [InlineKeyboardButton("⬅️ Volver al Menú Principal", callback_data='start')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "🔢 *Álgebra*:\nSeleccione un subtema:",
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )

    elif data == 'trigonometria':
        await query.edit_message_text("📐 La funcionalidad de Trigonometría aún no está disponible.")

    elif data == 'aritmetica':
        await query.edit_message_text("🧮 La funcionalidad de Aritmética aún no está disponible.")

    elif data == 'geometria':
        await query.edit_message_text("📏 La funcionalidad de Geometría aún no está disponible.")

    elif data == 'meeseeks':
        await send_meeseeks(update, context)

    elif data == 'start':
        # Volver al menú principal
        await start(update, context)

    # Subtemas de Álgebra
    elif data == 'numeros_reales_complejos':
        keyboard = [
            [InlineKeyboardButton("Operaciones con Números Reales", callback_data='operaciones_numeros_reales')],
            [InlineKeyboardButton("Intervalos", callback_data='intervalos')],
            [InlineKeyboardButton("Valor Absoluto", callback_data='valor_absoluto')],
            [InlineKeyboardButton("Representación Binomial", callback_data='representacion_binomial')],
            [InlineKeyboardButton("Módulo y Conjugado", callback_data='modulo_conjugado')],
            [InlineKeyboardButton("⬅️ Volver a Álgebra", callback_data='algebra')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "🔢 *Números Reales y Complejos*:\nSeleccione un tema:",
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )

    elif data == 'ecuaciones_inecuaciones':
        keyboard = [
            [InlineKeyboardButton("Ecuaciones de Primer y Segundo Grado", callback_data='ecuaciones_una_variable')],
            [InlineKeyboardButton("Ecuaciones Bicuadradas", callback_data='ecuaciones_bicuadradas')],
            [InlineKeyboardButton("Inecuaciones de Primer y Segundo Grado", callback_data='inecuaciones_una_variable')],
            [InlineKeyboardButton("⬅️ Volver a Álgebra", callback_data='algebra')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "📏 *Ecuaciones e Inecuaciones*:\nSeleccione un tema:",
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )

    elif data == 'sistemas_ecuaciones':
        keyboard = [
            [InlineKeyboardButton("Sistemas Lineales", callback_data='sistemas_lineales')],
            [InlineKeyboardButton("Métodos de Cramer y Gauss", callback_data='metodos_cramer_gauss')],
            [InlineKeyboardButton("Sistemas de Inecuaciones", callback_data='sistemas_inecuaciones')],
            [InlineKeyboardButton("Programación Lineal", callback_data='programacion_lineal')],
            [InlineKeyboardButton("⬅️ Volver a Álgebra", callback_data='algebra')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "📐 *Sistemas de Ecuaciones*:\nSeleccione un tema:",
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )

    elif data == 'expresiones_algebraicas':
        keyboard = [
            [InlineKeyboardButton("Operaciones", callback_data='operaciones_exp_alg')],
            [InlineKeyboardButton("Potenciación", callback_data='potenciacion')],
            [InlineKeyboardButton("Radicación", callback_data='radicacion')],
            [InlineKeyboardButton("Polinomios con Coeficientes en ℝ", callback_data='polinomios_coeficientes')],
            [InlineKeyboardButton("Grado de Expresiones Algebraicas", callback_data='grado_expresiones')],
            [InlineKeyboardButton("Operaciones con Polinomios", callback_data='operaciones_polinomios')],
            [InlineKeyboardButton("División de Polinomios", callback_data='division_polinomios')],
            [InlineKeyboardButton("Teorema del Resto", callback_data='teorema_resto')],
            [InlineKeyboardButton("Teorema del Factor", callback_data='teorema_factor')],
            [InlineKeyboardButton("Productos Notables", callback_data='productos_notables')],
            [InlineKeyboardButton("Factorización", callback_data='factorizacion')],
            [InlineKeyboardButton("MCD y MCM de Polinomios", callback_data='mcd_mcm_polinomios')],
            [InlineKeyboardButton("Teorema Fundamental del Álgebra", callback_data='teorema_fundamental')],
            [InlineKeyboardButton("Relación entre Raíces y Coeficientes", callback_data='raices_coeficientes')],
            [InlineKeyboardButton("⬅️ Volver a Álgebra", callback_data='algebra')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "🧮 *Expresiones Algebraicas*:\nSeleccione un tema:",
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )

    elif data == 'funciones_reales':
        keyboard = [
            [InlineKeyboardButton("Dominio y Rango", callback_data='dominio_rango')],
            [InlineKeyboardButton("Representación de Funciones", callback_data='representacion_funciones')],
            [InlineKeyboardButton("Funciones Elementales", callback_data='funciones_elementales')],
            [InlineKeyboardButton("Funciones Par e Impar", callback_data='funciones_par_impar')],
            [InlineKeyboardButton("Funciones Monótonas", callback_data='funciones_monotonas')],
            [InlineKeyboardButton("Funciones Inyectivas y Sobreyectivas", callback_data='funciones_iny_sobre')],
            [InlineKeyboardButton("Funciones Inversas", callback_data='funciones_inversas')],
            [InlineKeyboardButton("Función Exponencial", callback_data='funcion_exponencial')],
            [InlineKeyboardButton("Función Logarítmica", callback_data='funcion_logaritmica')],
            [InlineKeyboardButton("Modelación con Funciones", callback_data='modelacion_funciones')],
            [InlineKeyboardButton("⬅️ Volver a Álgebra", callback_data='algebra')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "📈 *Funciones Reales de Variable Real*:\nSeleccione un tema:",
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )

    # Aquí manejamos los subtemas finales que envían imágenes y textos
    else:
        # Asumimos que el data coincide con el nombre de la función
        # Llamamos a la función correspondiente
        await send_topic(update, data)

# Función para enviar el contenido de cada tema
async def send_topic(update: Update, topic_key):
    topic_dict = {
        'operaciones_numeros_reales': ('images/operaciones_numeros_reales.png', "➕➖✖️➗ *Operaciones con Números Reales*"),
        'intervalos': ('images/intervalos.png', "📏 *Intervalos en la Recta Real*"),
        'valor_absoluto': ('images/valor_absoluto.png', "➕ *Valor Absoluto*"),
        'representacion_binomial': ('images/representacion_binomial.png', "🔢 *Representación Binomial de un Número Complejo*"),
        'modulo_conjugado': ('images/modulo_conjugado.png', "📐 *Módulo y Conjugado. Propiedades*"),
        'ecuaciones_una_variable': ('images/ecuaciones_una_variable.png', "➗ *Ecuaciones de Primer y Segundo Grado con una Variable*"),
        'ecuaciones_bicuadradas': ('images/ecuaciones_bicuadradas.png', "✖️ *Ecuaciones Bicuadradas*"),
        'inecuaciones_una_variable': ('images/inecuaciones_una_variable.png', "➖ *Inecuaciones de Primer y Segundo Grado con una Variable*"),
        'sistemas_lineales': ('images/sistemas_lineales.png', "📝 *Sistemas de Ecuaciones Lineales*"),
        'metodos_cramer_gauss': ('images/metodos_cramer_gauss.png', "📊 *Métodos de Cramer y Gauss*"),
        'sistemas_inecuaciones': ('images/sistemas_inecuaciones.png', "📈 *Sistemas de Inecuaciones*"),
        'programacion_lineal': ('images/programacion_lineal.png', "💹 *Introducción a la Programación Lineal*"),
        'operaciones_exp_alg': ('images/operaciones_exp_alg.png', "🧮 *Operaciones con Expresiones Algebraicas*"),
        'potenciacion': ('images/potenciacion.png', "💥 *Potenciación*"),
        'radicacion': ('images/radicacion.png', "🌿 *Radicación*"),
        'polinomios_coeficientes': ('images/polinomios_coeficientes.png', "🔢 *Polinomios con Coeficientes en ℝ*"),
        'grado_expresiones': ('images/grado_expresiones.png', "📏 *Grado de Expresiones Algebraicas*"),
        'operaciones_polinomios': ('images/operaciones_polinomios.png', "➕ *Operaciones con Polinomios*"),
        'division_polinomios': ('images/division_polinomios.png', "➗ *División de Polinomios*"),
        'teorema_resto': ('images/teorema_resto.png', "🧩 *Teorema del Resto*"),
        'teorema_factor': ('images/teorema_factor.png', "🔑 *Teorema del Factor*"),
        'productos_notables': ('images/productos_notables.png', "🌟 *Productos Notables*"),
        'factorizacion': ('images/factorizacion.png', "🛠️ *Factorización*"),
        'mcd_mcm_polinomios': ('images/mcd_mcm_polinomios.png', "🔗 *MCD y MCM de Polinomios*"),
        'teorema_fundamental': ('images/teorema_fundamental_algebra.png', "📚 *Teorema Fundamental del Álgebra*"),
        'raices_coeficientes': ('images/raices_coeficientes.png', "🌱 *Relación entre Raíces y Coeficientes*"),
        'dominio_rango': ('images/dominio_rango.png', "🌐 *Dominio y Rango de una Función*"),
        'representacion_funciones': ('images/representacion_funciones.png', "📊 *Representación de Funciones*"),
        'funciones_elementales': ('images/funciones_elementales.png', "🔢 *Funciones Elementales*"),
        'funciones_par_impar': ('images/funciones_par_impar.png', "⚖️ *Funciones Par e Impar*"),
        'funciones_monotonas': ('images/funciones_monotonas.png', "📈 *Funciones Monótonas*"),
        'funciones_iny_sobre': ('images/funciones_inyectivas_sobreyectivas.png', "🔄 *Funciones Inyectivas y Sobreyectivas*"),
        'funciones_inversas': ('images/funciones_inversas.png', "🔃 *Funciones Inversas*"),
        'funcion_exponencial': ('images/funcion_exponencial.png', "💹 *Función Exponencial*"),
        'funcion_logaritmica': ('images/funcion_logaritmica.png', "📈 *Función Logarítmica*"),
        'modelacion_funciones': ('images/modelacion_funciones.png', "🌍 *Modelación del Mundo Real con Funciones*")
    }

    if topic_key in topic_dict:
        image_path, caption = topic_dict[topic_key]
        await send_photo_with_caption(update.callback_query, image_path, caption)
    else:
        await update.callback_query.edit_message_text("Lo siento, este contenido no está disponible.")

# Función para enviar fotos con mensaje y manejar excepciones
async def send_photo_with_caption(query, image_path: str, caption: str):
    try:
        with open(image_path, 'rb') as photo:
            await query.message.reply_photo(photo=photo, caption=caption, parse_mode='Markdown')
    except FileNotFoundError:
        await query.message.reply_text("Lo siento, la imagen no está disponible en este momento.")
    except Exception as e:
        logger.error(f"Error al enviar la imagen: {e}")
        await query.message.reply_text("Ocurrió un error al enviar la imagen.")

# Función para enviar una imagen y una frase aleatoria de Señor Meeseeks
async def send_meeseeks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query

    frases_meeseeks = [
        "¡Soy el Señor Meeseeks! ¡Mírame!",
        "¡Puedo hacerlo!",
        "¡La existencia es dolor para un Meeseeks!",
        "¡Ooh, sí! ¡Claro que sí!",
        "Los Meeseeks no suelen existir tanto tiempo.",
        "¡Estamos creados para servir un propósito singular!",
        "¡Vamos, Jerry! ¡Tienes que relajarte!",
        "Lo siento, pero es tu culpa que estés atascado con nosotros.",
        "¡Todos queremos morir! ¡Somos Meeseeks!",
        "¡Vivimos para servir!",
        "¡Solo intenta relajarte!",
        "¡El Señor Meeseeks te ayudará!"
    ]

    frase = random.choice(frases_meeseeks)
    image_path = 'images/meeseeks.png'  # Asegúrate de tener esta imagen en la carpeta 'images'

    try:
        with open(image_path, 'rb') as photo:
            await query.message.reply_photo(photo=photo, caption=frase)
    except FileNotFoundError:
        await query.message.reply_text(frase)
    except Exception as e:
        logger.error(f"Error al enviar la imagen de Meeseeks: {e}")
        await query.message.reply_text("Ocurrió un error al enviar la imagen de Meeseeks.")

# Configuración principal del bot
def main():
    # Reemplaza 'YOUR_BOT_TOKEN' con el token de tu bot
    TOKEN = '8099377584:AAG_yiQtBroxjgtnsuwnTmQfDZ622-PfnVY'

    # Construir la aplicación
    application = Application.builder().token(TOKEN).build()

    # Agregar manejador de errores
    application.add_error_handler(error_handler)

    # Comandos principales
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('comandos', start))

    # Manejo de botones
    application.add_handler(CallbackQueryHandler(button))

    # Iniciar el bot y mantenerlo corriendo
    application.run_polling(drop_pending_updates=True)

if __name__ == '__main__':
    while True:
        try:
            main()
        except Exception as e:
            logger.error(f"El bot se detuvo debido a un error: {e}")
            logger.info("Reiniciando el bot en 5 segundos...")
            time.sleep(5)
