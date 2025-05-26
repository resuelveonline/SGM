import React, { useState } from 'react';
import axios from 'axios';

interface Mensaje {
  texto: string;
  esBot: boolean;
  timestamp: Date;
}

const ChatWidget: React.FC = () => {
  const [mensajes, setMensajes] = useState<Mensaje[]>([
    {
      texto: "¡Hola! Soy el asistente virtual del Municipio de Puebla. ¿En qué puedo ayudarte?",
      esBot: true,
      timestamp: new Date()
    }
  ]);
  const [inputMensaje, setInputMensaje] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [chatAbierto, setChatAbierto] = useState(false);

  const enviarMensaje = async () => {
    if (!inputMensaje.trim()) return;

    // Agregar mensaje del usuario
    const nuevoMensajeUsuario: Mensaje = {
      texto: inputMensaje,
      esBot: false,
      timestamp: new Date()
    };

    setMensajes(prev => [...prev, nuevoMensajeUsuario]);
    setInputMensaje('');
    setIsLoading(true);

    try {
      // Llamar a tu API backend
      const response = await axios.post('http://127.0.0.1:8000/chat', {
        mensaje: inputMensaje
      });

      // Agregar respuesta del bot
      const respuestaBot: Mensaje = {
        texto: response.data.chatbot_respuesta,
        esBot: true,
        timestamp: new Date()
      };

      setMensajes(prev => [...prev, respuestaBot]);
    } catch (error) {
      // Respuesta de error si la API no está disponible
      const errorBot: Mensaje = {
        texto: "Lo siento, el servicio no está disponible en este momento. Por favor intenta más tarde.",
        esBot: true,
        timestamp: new Date()
      };
      setMensajes(prev => [...prev, errorBot]);
    }

    setIsLoading(false);
  };

  const manejarEnter = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      enviarMensaje();
    }
  };

  return (
    <>
      {/* Botón flotante para abrir chat */}
      {!chatAbierto && (
        <button
          onClick={() => setChatAbierto(true)}
          className="fixed bottom-6 right-6 bg-puebla-blue hover:bg-blue-700 text-white p-4 rounded-full shadow-lg transition-all duration-300 z-50"
        >
          💬
        </button>
      )}

      {/* Widget de chat */}
      {chatAbierto && (
        <div className="fixed bottom-6 right-6 w-80 h-96 bg-white rounded-lg shadow-xl border z-50 flex flex-col">
          {/* Header del chat */}
          <div className="bg-puebla-blue text-white p-4 rounded-t-lg flex justify-between items-center">
            <h3 className="font-semibold">Asistente Municipal</h3>
            <button
              onClick={() => setChatAbierto(false)}
              className="text-white hover:text-gray-200"
            >
              ✕
            </button>
          </div>

          {/* Área de mensajes */}
          <div className="flex-1 overflow-y-auto p-4 space-y-3">
            {mensajes.map((mensaje, index) => (
              <div
                key={index}
                className={`flex ${mensaje.esBot ? 'justify-start' : 'justify-end'}`}
              >
                <div
                  className={`max-w-xs p-3 rounded-lg ${
                    mensaje.esBot
                      ? 'bg-gray-100 text-gray-800'
                      : 'bg-puebla-blue text-white'
                  }`}
                >
                  <p className="text-sm whitespace-pre-wrap">{mensaje.texto}</p>
                  <span className="text-xs opacity-70">
                    {mensaje.timestamp.toLocaleTimeString([], {
                      hour: '2-digit',
                      minute: '2-digit'
                    })}
                  </span>
                </div>
              </div>
            ))}

            {/* Indicador de carga */}
            {isLoading && (
              <div className="flex justify-start">
                <div className="bg-gray-100 p-3 rounded-lg">
                  <div className="flex space-x-1">
                    <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce"></div>
                    <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{animationDelay: '0.1s'}}></div>
                    <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{animationDelay: '0.2s'}}></div>
                  </div>
                </div>
              </div>
            )}
          </div>

          {/* Input para escribir */}
          <div className="p-4 border-t">
            <div className="flex space-x-2">
              <input
                type="text"
                value={inputMensaje}
                onChange={(e) => setInputMensaje(e.target.value)}
                onKeyPress={manejarEnter}
                placeholder="Escribe tu pregunta..."
                className="flex-1 border rounded-lg px-3 py-2 focus:outline-none focus:border-puebla-blue"
                disabled={isLoading}
              />
              <button
                onClick={enviarMensaje}
                disabled={isLoading || !inputMensaje.trim()}
                className="bg-puebla-blue hover:bg-blue-700 disabled:bg-gray-300 text-white px-4 py-2 rounded-lg transition-colors"
              >
                📤
              </button>
            </div>
          </div>
        </div>
      )}
    </>
  );
};

export default ChatWidget;