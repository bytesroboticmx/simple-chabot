
"""
Autor: Dr. Aldo Gonzalez Vazquez
Version: 1.0
Licencia: MIT

Este chatbot tiene las siguientes características:

Reconocimiento de patrones usando expresiones regulares
Respuestas aleatorias para cada tipo de entrada
Manejo de funciones dinámicas (como mostrar la hora actual)
Sistema de respuestas por defecto
Interfaz de conversación simple

Para usar el chatbot:

Copia el código en un archivo .py
Ejecútalo con Python
Escribe "ayuda" para ver las opciones disponibles
Escribe "salir" para terminar la conversación

Puedes expandir el chatbot añadiendo más patrones y respuestas al diccionario patterns. Por ejemplo, podrías agregar:

Más preguntas y respuestas
Cálculos matemáticos
Búsqueda de información
Integración con APIs externas
"""
import re
import random
from datetime import datetime

class ChatBot:
    def __init__(self):
        self.patterns = {
            r'hola|hey|saludos': [
                'Hola, ¿cómo estás?',
                '¡Hola! ¿En qué puedo ayudarte?',
                '¡Saludos! ¿Qué necesitas?'
            ],
            r'(que hora|hora actual|qué hora)': [
                lambda: f'Son las {datetime.now().strftime("%H:%M")}',
            ],
            r'(como estas|cómo estás)': [
                'Muy bien, gracias por preguntar. ¿Y tú?',
                '¡Excelente! ¿Qué tal tú?'
            ],
            r'adios|chau|hasta luego': [
                'Hasta luego, ¡que tengas un buen día!',
                '¡Adiós! Fue un gusto chatear contigo',
            ],
            r'(tu nombre|como te llamas|cómo te llamas)': [
                'Me llamo BotPy, ¡un gusto conocerte!',
            ],
            r'(ayuda|help|opciones)': [
                '''Puedo ayudarte con:
                - Saludos y despedidas
                - Decirte la hora actual
                - Responder preguntas básicas
                - Mantener una conversación simple
                
                ¡Pregúntame lo que quieras!'''
            ]
        }
        
        # Respuesta por defecto cuando no hay coincidencias
        self.default_responses = [
            "Lo siento, no entiendo. ¿Podrías reformular tu pregunta?",
            "No estoy seguro de cómo responder a eso. ¿Podrías ser más específico?",
            "Disculpa, no comprendí bien. ¿Puedes decirlo de otra manera?"
        ]

    def get_response(self, user_input):
        # Convertir entrada a minúsculas
        user_input = user_input.lower()
        
        # Buscar coincidencias en los patrones
        for pattern, responses in self.patterns.items():
            if re.search(pattern, user_input):
                response = random.choice(responses)
                # Si la respuesta es una función, ejecutarla
                if callable(response):
                    return response()
                return response
        
        # Si no hay coincidencias, devolver respuesta por defecto
        return random.choice(self.default_responses)

    def start(self):
        print("Bot: ¡Hola! Soy BotPy. Escribe 'ayuda' para ver qué puedo hacer.")
        
        while True:
            user_input = input("Tú: ").strip()
            
            if user_input.lower() in ['salir', 'exit', 'quit']:
                print("Bot: ¡Hasta luego! Que tengas un buen día.")
                break
                
            response = self.get_response(user_input)
            print("Bot:", response)

# Crear y ejecutar el chatbot
if __name__ == "__main__":
    bot = ChatBot()
    bot.start()
