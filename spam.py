#pip install pyautogui pyperclip en cmd o terminal
import pyautogui
import time
import pyperclip


#                                                   <<---================= COMO USARLO =================--->>
# ============================================================
# 📌 Guía de uso del script para enviar mensajes en WhatsApp Web 
#    o en cualquier plataforma donde se pueda escribir
# ============================================================
#
# ⚠️ Nota:
# - Si se envían emojis demasiado grandes, puede que no se vean correctamente 
#   en algunas redes sociales o dispositivos. Esto se mejorará en futuras versiones.
#
# ------------------------------------------------------------
# 🔧 Preparación
# ------------------------------------------------------------
# 1. Instala las librerías necesarias en tu entorno de Python:
#       pip install pyautogui pyperclip
#    (Asegúrate también de tener las extensiones de Python configuradas).
#
# 2. Abre WhatsApp Web (o la red social donde quieras enviar mensajes) 
#    en tu computadora desde el navegador.
#
# ------------------------------------------------------------
# ▶️ Ejecución
# ------------------------------------------------------------
# 3. Selecciona el chat en el que deseas enviar los mensajes.
#
# 4. Ejecuta el script (haz clic en el botón de ejecución, normalmente el
#    triángulo " ▶ " en la parte superior derecha del editor).
#    - Tendrás unos segundos para hacer clic en el chat antes de que el script
#      empiece a enviar mensajes.
#    - Si deseas modificar este tiempo de espera inicial, cambia el valor de:
#          tiempo_de_espera_inicial
#
# 5. Durante ese tiempo, asegúrate de posicionarte en el chat correcto.
#    Si te sobra tiempo, espera tranquilamente a que el envío comience.
#
# ------------------------------------------------------------
# ✉️ Envío automático
# ------------------------------------------------------------
# 6. El script enviará de forma automática el contenido configurado en las
#    siguientes variables:
#       - mensaje_texto → el texto que quieras enviar.
#       - emoji         → los emojis que quieras incluir junto al mensaje 
#                         (también funciona con texto).
#
# ✅ ¡Listo! Con estos pasos, tus mensajes y emojis se enviarán automáticamente
#    al chat seleccionado.
# ============================================================
#                                                  ================= CONFIGURACIÓN DE USUARIO =================

# aquí dejo la url de la pagina de emoji https://www.messletters.com/es/text-art/ para remplazar el emoji por otro ...

# 1. REPETICIONES
ciclos =2         # Cuantas veces hace todo el proceso
total_textos = 1    # Cuantos "mensaje de texto" por cada ciclo
total_corazon = 1   # Cuantos emojis por cada ciclo

# 2. CONTENIDO
mensaje_texto = " ... "  # <--- AQUÍ VA EL TEXTO A ENVIAR --->
emoji = """⬛️⬛️⬛️🟥🟥⬛️⬛️⬛️🟥🟥⬛️⬛️⬛️
⬛️⬛️🟥🟥🟥🟥⬛️🟥🟥🟥🟥⬛️⬛️
⬛️🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥⬛️
⬛️🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥⬛️
⬛️🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥⬛️
⬛️⬛️🟥🟥🟥🟥🟥🟥🟥🟥🟥⬛️⬛️
⬛️⬛️⬛️🟥🟥🟥🟥🟥🟥🟥⬛️⬛️⬛️
⬛️⬛️⬛️⬛️🟥🟥🟥🟥🟥⬛️⬛️⬛️⬛️
⬛️⬛️⬛️⬛️⬛️🟥🟥🟥⬛️⬛️⬛️⬛️⬛️
⬛️⬛️⬛️⬛️⬛️⬛️🟥⬛️⬛️⬛️⬛️⬛️⬛️"""  # <--- AQUÍ va el diseño de la pagina https://www.messletters.com/es/text-art/ A ENVIAR 
                                                                        #  para que se guarde en la memoria  --->

# 3. TIEMPOS (Aquí es donde controlas la velocidad)
tiempo_de_espera_inicial = 5  # Tiempo para que selecciones el chat
tiempo_de_envio = 0.1         # <--- ESTA ES LA VARIABLE DE TIEMPO --->
                              # Define la pausa tras cada envío. 
                              # (0.1 = Muy rápido | 0.5 = Medio | 1.0 = Lento)

# ===========================================================

# Ajuste de PyAutoGUI para que no haya retrasos ocultos
pyautogui.PAUSE = 0.01 

def enviar_al_chat(contenido):
    # Copia el dibujo o texto al portapapeles de Windows
    pyperclip.copy(contenido) 
    # Pega (Ctrl + V)
    pyautogui.hotkey('ctrl', 'v') 
    # Presiona Enter
    pyautogui.press('enter')
    # Aplica la pausa de envío que configuraste arriba
    time.sleep(tiempo_de_envio)

# --- INICIO DEL PROCESO ---

print(f"CORRE AL WP Tienes {tiempo_de_espera_inicial} segundos para activar el chat...")
time.sleep(tiempo_de_espera_inicial) 

for i in range(ciclos):
    print(f"Enviando ciclo {i+1}...")

    # Bucle para enviar los textos
    for _ in range(total_textos):
        enviar_al_chat(mensaje_texto)

    # Bucle para enviar los emoji
    for _ in range(total_corazon):
        enviar_al_chat(emoji)

    # Pausa extra opcional entre ciclos para no saturar la app
    time.sleep(0.5)

print("¡Tarea completada!")