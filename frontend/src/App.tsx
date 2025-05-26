import React from 'react';
import Header from './components/Header';
import HomePage from './components/HomePage';
import ChatWidget from './components/ChatWidget';
import './App.css';

function App() {
  return (
    <div className="App">
      <Header />
      <HomePage />
      <ChatWidget />
    </div>
  );
}

export default App;