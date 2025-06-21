import { useState, useEffect } from 'react';
import reactLogo from './assets/react.svg';
import viteLogo from '/vite.svg';
import './App.css';

function App() {
  const [message, setMessage] = useState('Buscando mensagem da API...');

  useEffect(() => {
    // Fazendo a chamada para o caminho relativo da API
    fetch('/api/public/status/')
      .then(response => {
        if (!response.ok) {
          throw new Error(`Erro de Rede ou HTTP: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        setMessage(data.message || 'API respondeu, mas sem a mensagem esperada.');
      })
      .catch(error => {
        console.error('Erro ao buscar da API:', error);
        setMessage(`Falha ao conectar com a API.`);
      });
  }, []); // Array vazio para rodar só uma vez

  return (
    <>
      <div>
        <a href="https://vitejs.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://reactjs.org" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Carteira de Investimentos Inteligente</h1>
      <div className="card">
        <h2>Status da Conexão com a API:</h2>
        <p>
          <strong>{message}</strong>
        </p>
      </div>
    </>
  );
}

export default App;