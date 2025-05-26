import React from 'react';

const HomePage: React.FC = () => {
  return (
    <div className="min-h-screen bg-gray-50">
      {/* Hero Section */}
      <section className="bg-gradient-to-r from-puebla-blue to-blue-600 text-white py-20">
        <div className="container mx-auto px-4 text-center">
          <h2 className="text-4xl md:text-6xl font-bold mb-6">
            Bienvenido al Portal Ciudadano
          </h2>
          <p className="text-xl md:text-2xl mb-8 opacity-90">
            Sistema inteligente para trámites municipales de Puebla
          </p>
          <div className="flex flex-col md:flex-row justify-center space-y-4 md:space-y-0 md:space-x-4">
            <button className="bg-puebla-gold hover:bg-yellow-600 text-white px-8 py-3 rounded-lg font-semibold transition-colors">
              Iniciar Trámite
            </button>
            <button className="bg-transparent border-2 border-white hover:bg-white hover:text-puebla-blue px-8 py-3 rounded-lg font-semibold transition-colors">
              Consultar Expediente
            </button>
          </div>
        </div>
      </section>

      {/* Services Section */}
      <section className="py-16">
        <div className="container mx-auto px-4">
          <h3 className="text-3xl font-bold text-center mb-12 text-gray-800">
            Servicios Disponibles
          </h3>
          <div className="grid md:grid-cols-3 gap-8">
            <div className="bg-white p-6 rounded-lg shadow-md hover:shadow-lg transition-shadow">
              <div className="text-puebla-blue text-4xl mb-4">📋</div>
              <h4 className="text-xl font-semibold mb-2">Licencias de Funcionamiento</h4>
              <p className="text-gray-600">Obtén tu licencia para operar tu negocio de manera rápida y sencilla.</p>
            </div>
            <div className="bg-white p-6 rounded-lg shadow-md hover:shadow-lg transition-shadow">
              <div className="text-puebla-blue text-4xl mb-4">🏗️</div>
              <h4 className="text-xl font-semibold mb-2">Permisos de Construcción</h4>
              <p className="text-gray-600">Solicita permisos para construcción y remodelación de inmuebles.</p>
            </div>
            <div className="bg-white p-6 rounded-lg shadow-md hover:shadow-lg transition-shadow">
              <div className="text-puebla-blue text-4xl mb-4">📍</div>
              <h4 className="text-xl font-semibold mb-2">Uso de Suelo</h4>
              <p className="text-gray-600">Verifica y obtén certificados de uso de suelo para tu propiedad.</p>
            </div>
          </div>
        </div>
      </section>

      {/* Chat Prompt Section */}
      <section className="bg-puebla-blue text-white py-16">
        <div className="container mx-auto px-4 text-center">
          <h3 className="text-3xl font-bold mb-6">¿Tienes Preguntas?</h3>
          <p className="text-xl mb-8 opacity-90">
            Nuestro asistente virtual está aquí para ayudarte 24/7
          </p>
          <button className="bg-puebla-gold hover:bg-yellow-600 text-white px-8 py-3 rounded-lg font-semibold transition-colors">
            💬 Chatear Ahora
          </button>
        </div>
      </section>
    </div>
  );
};

export default HomePage;