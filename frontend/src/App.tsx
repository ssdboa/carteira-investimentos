import { useState, useEffect } from 'react';
import reactLogo from './assets/react.svg';
import viteLogo from '/vite.svg';
import './App.css';

function App() {
  const [message, setMessage] = useState('Buscando mensagem da API...');
  
  // Lendo a variável de ambiente que configuramos na Vercel
  const apiUrl = import.meta.env.VITE_API_URL;

  useEffect(() => {
    // Verificação de segurança
    if (!apiUrl) {
      setMessage('Erro: A variável de ambiente VITE_API_URL não está configurada na Vercel.');
      return;
    }

    // O ponto principal: chamando a URL completa da API na Render
    fetch(`${apiUrl}/api/public/teste/`)
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
        setMessage(`Falha ao conectar com a API. Verifique o console do navegador (tecla F12) para erros de CORS ou rede.`);
      });
  }, [apiUrl]); // O array de dependências garante que isso rode apenas uma vez

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