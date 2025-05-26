import React from 'react';

const Header: React.FC = () => {
  return (
    <header className="bg-puebla-blue text-white shadow-lg">
      <div className="container mx-auto px-4 py-6">
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-4">
            <h1 className="text-2xl font-bold">🏛️ Municipio de Puebla</h1>
            <span className="text-puebla-gold text-sm">Sistema Digital</span>
          </div>
          <nav className="hidden md:flex space-x-6">
            <a href="#inicio" className="hover:text-puebla-gold transition-colors">Inicio</a>
            <a href="#tramites" className="hover:text-puebla-gold transition-colors">Trámites</a>
            <a href="#consulta" className="hover:text-puebla-gold transition-colors">Consultar</a>
            <a href="#contacto" className="hover:text-puebla-gold transition-colors">Contacto</a>
          </nav>
        </div>
      </div>
    </header>
  );
};

export default Header;