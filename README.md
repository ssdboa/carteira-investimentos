# 📋 Documentação da Arquitetura e Planejamento do Projeto: Carteira de Investimentos Inteligente
**Última Atualização:** 14 de junho de 2025  
**Versão:** 1.0.0 (Versão Definitiva com Estrutura Completa)

---

## 🎯 0. Definição do Projeto: Carteira de Investimentos Inteligente

### 0.1. Problema a Ser Resolvido
Muitos investidores, desde iniciantes até os mais experientes, enfrentam desafios significativos no gerenciamento de suas carteiras de investimento:

* **Fragmentação de Informações:** Ativos espalhados por diversas corretoras e plataformas.
* **Acompanhamento Manual e Ineficiente:** Dificuldade em rastrear desempenho, proventos e impostos.
* **Análise Superficial:** Falta de ferramentas para análises profundas de diversificação e risco.
* **Tomada de Decisão Reativa:** Decisões baseadas em intuição em vez de dados concretos.
* **Complexidade para Iniciantes:** Alta barreira de entrada para o gerenciamento de investimentos.

### 0.2. Solução Proposta
Plataforma web intuitiva e poderosa que centraliza, analisa e oferece insights sobre as carteiras de investimento dos usuários, além de fornecer ferramentas de pesquisa de ativos para o público em geral.

### 0.3. Público-Alvo
* **Investidores Individuais (Pessoa Física):** De iniciantes a experientes.
* **Visitantes Interessados em Mercado Financeiro:** Buscando informações sobre ativos.
* **Foco Inicial:** Mercado brasileiro de investimentos.

### 0.4. Proposta de Valor Única (PVU)
* **Consolidação Abrangente:** Integração de diversos tipos de ativos.
* **Análises Inteligentes e Personalizadas:** Insights sobre diversificação, risco x retorno e projeções.
* **Ferramentas de Pesquisa Pública:** Acesso aberto a informações e indicadores de ativos.
* **Interface Intuitiva e Educacional:** Design amigável com recursos de aprendizado.
* **Foco na Experiência do Usuário:** Plataforma rápida, responsiva e agradável.

### 0.5. Objetivos Chave e Funcionalidades do MVP
O MVP focará na consolidação manual e acompanhamento básico para usuários logados, ao mesmo tempo que oferecerá seções públicas para engajamento geral.

* **Acesso Público (Não Logado):** Navegação em seções abertas (ex: fundamentos de ativos).
* **Acesso Privado (Logado):** Funcionalidades personalizadas que exigem autenticação.
* **Arquitetura Modular:** Projetada para permitir a adição de novas funcionalidades de forma escalável.

---

## 🏗️ 1. Arquitetura de Alto Nível e Tecnologias Definidas

### 1.1. Frontend (Interface do Usuário)
* **Tecnologia Principal:** `React.js`
* **Princípio Fundamental:** HTML5 Semântico para garantir acessibilidade (a11y), SEO e manutenibilidade.
* **Estilização/Componentes:** Design System customizado com componentes reutilizáveis.
* **Plataforma de Deploy:** Vercel
* **IaC/Configuração:** Arquivo `vercel.json`

### 1.2. Backend (Lógica de Negócio e APIs)
* **Tecnologia Principal:** Python com `Django`
* **Padrão Arquitetural:** Clean Architecture e Domain-Driven Design (DDD)
* **Empacotamento:** Contêineres Docker
* **Plataforma de Deploy:** Render
* **IaC/Configuração:** Arquivo `render.yaml`
* **Comunicação:** API RESTful

### 1.3. Banco de Dados Principal
* **Tecnologia:** `PostgreSQL`
* **Hospedagem:** Serviço Gerenciado de PostgreSQL da Render
* **Backup:** Automatizado com retenção de 30 dias

### 1.4. Cache e Sessões
* **Tecnologia:** `Redis`
* **Hospedagem:** Serviço Gerenciado Redis da Render
* **Funções:** Cache de queries, sessões, dados de mercado

### 1.5. Mensageria e Filas de Tarefas (EDA Interna)
* **Fila de Mensagens:** `RabbitMQ` (contêiner Docker na Render)
* **Processamento Assíncrono:** `Celery` (contêineres Docker na Render)
* **Scheduler:** `Celery Beat` para tarefas periódicas

### 1.6. API Gateway
* **Tecnologia:** `Kong` (contêiner Docker na Render)
* **Funções:** Roteamento, segurança (validação de token, rate limiting), logging

### 1.7. Autenticação e Autorização Centralizada
* **Tecnologia:** `Keycloak` (contêiner Docker com disco persistente na Render)
* **Funções:** Gerenciamento de identidades, emissão de tokens JWT (OAuth2/OIDC)

### 1.8. Containerização e Orquestração
* **Tecnologia:** `Docker` e `Docker Compose`
* **Desenvolvimento:** `Docker Compose` para ambiente local completo
* **Produção:** Containers individuais no Render
* **Imagens Base:** Python oficial (slim) para otimização

### 1.9. Versionamento de Código (SCM)
* **Ferramenta:** `Git`
* **Plataforma:** `GitHub`
* **Estratégia de Branching:** Gitflow
* **Versionamento de Releases:** Versionamento Semântico (SemVer)

### 1.10. Integração Contínua e Deploy Contínuo (CI/CD)
* **Frontend (Vercel):** CI/CD integrado com GitHub
* **Backend (Render):** CI/CD integrado com GitHub
* **Estratégia:** Deploy-First Approach com validação contínua
* **Testes:** Automatizados em todas as etapas

---

## 📁 2. Estrutura Completa de Pastas do Projeto

### 2.1. Estrutura Geral

```text
carteira-investimentos/
├── 📁 frontend/                     # Aplicação React (Vercel)
├── 📁 backend/                      # API Django (Render)
├── 📁 docker/                       # Configurações Docker
├── 📁 scripts/                      # Scripts de automação
├── 📁 docs/                         # Documentação
├── 📁 .github/                      # GitHub Actions (CI/CD)
├── 📄 docker-compose.yml           # Orquestração local
├── 📄 docker-compose.prod.yml      # Orquestração produção
├── 📄 README.md                     # Documentação principal
├── 📄 .gitignore                    # Arquivos ignorados
└── 📄 .env.example                  # Variáveis de ambiente exemplo
```

### 2.2. Frontend (React + Vercel)
```text
frontend/
├── 📁 public/
│   ├── 📄 index.html
│   ├── 📄 favicon.ico
│   ├── 📄 manifest.json
│   ├── 📄 robots.txt
│   └── 📁 icons/
│       ├── 📄 icon-192x192.png
│       └── 📄 icon-512x512.png
│
├── 📁 src/
│   ├── 📁 components/               # Componentes reutilizáveis
│   │   ├── 📁 ui/                     # Componentes base do Design System
│   │   │   ├── 📄 Button.jsx
│   │   │   ├── 📄 Input.jsx
│   │   │   ├── 📄 Card.jsx
│   │   │   ├── 📄 Modal.jsx
│   │   │   ├── 📄 Table.jsx
│   │   │   ├── 📄 Chart.jsx
│   │   │   └── 📄 index.js
│   │   ├── 📁 layout/                  # Componentes de layout
│   │   │   ├── 📄 Header.jsx
│   │   │   ├── 📄 Sidebar.jsx
│   │   │   ├── 📄 Footer.jsx
│   │   │   ├── 📄 Navigation.jsx
│   │   │   └── 📄 Layout.jsx
│   │   ├── 📁 forms/                   # Componentes de formulário
│   │   │   ├── 📄 LoginForm.jsx
│   │   │   ├── 📄 RegisterForm.jsx
│   │   │   ├── 📄 PortfolioForm.jsx
│   │   │   ├── 📄 TransactionForm.jsx
│   │   │   └── 📄 AssetForm.jsx
│   │   └── 📁 charts/                  # Componentes de gráficos
│   │       ├── 📄 PortfolioChart.jsx
│   │       ├── 📄 PerformanceChart.jsx
│   │       ├── 📄 AllocationChart.jsx
│   │       └── 📄 ComparisonChart.jsx
│   │
│   ├── 📁 pages/                      # Páginas da aplicação
│   │   ├── 📁 public/                 # Páginas públicas (sem auth)
│   │   │   ├── 📄 HomePage.jsx
│   │   │   ├── 📄 AssetSearchPage.jsx
│   │   │   ├── 📄 AssetDetailsPage.jsx
│   │   │   ├── 📄 AboutPage.jsx
│   │   │   └── 📄 ContactPage.jsx
│   │   ├── 📁 auth/                   # Páginas de autenticação
│   │   │   ├── 📄 LoginPage.jsx
│   │   │   ├── 📄 RegisterPage.jsx
│   │   │   ├── 📄 ForgotPasswordPage.jsx
│   │   │   └── 📄 ResetPasswordPage.jsx
│   │   ├── 📁 dashboard/              # Páginas privadas (com auth)
│   │   │   ├── 📄 DashboardPage.jsx
│   │   │   ├── 📄 PortfoliosPage.jsx
│   │   │   ├── 📄 PortfolioDetailsPage.jsx
│   │   │   ├── 📄 TransactionsPage.jsx
│   │   │   ├── 📄 AnalyticsPage.jsx
│   │   │   └── 📄 ProfilePage.jsx
│   │   └── 📁 errors/                 # Páginas de erro
│   │       ├── 📄 NotFoundPage.jsx
│   │       ├── 📄 UnauthorizedPage.jsx
│   │       └── 📄 ServerErrorPage.jsx
│   │
│   ├── 📁 hooks/                      # Custom React Hooks
│   │   ├── 📄 useAuth.js
│   │   ├── 📄 useApi.js
│   │   ├── 📄 usePortfolio.js
│   │   ├── 📄 useAssets.js
│   │   ├── 📄 useTransactions.js
│   │   └── 📄 useLocalStorage.js
│   │
│   ├── 📁 services/                   # Serviços e APIs
│   │   ├── 📄 api.js                 # Configuração base da API
│   │   ├── 📄 authService.js         # Serviços de autenticação
│   │   ├── 📄 portfolioService.js    # Serviços de carteiras
│   │   ├── 📄 assetService.js        # Serviços de ativos
│   │   ├── 📄 transactionService.js  # Serviços de transações
│   │   └── 📄 marketDataService.js   # Serviços de dados de mercado
│   │
│   ├── 📁 context/                    # Context API
│   │   ├── 📄 AuthContext.js
│   │   ├── 📄 ThemeContext.js
│   │   ├── 📄 PortfolioContext.js
│   │   └── 📄 NotificationContext.js
│   │
│   ├── 📁 utils/                      # Utilitários
│   │   ├── 📄 formatters.js          # Formatação de dados
│   │   ├── 📄 validators.js          # Validações
│   │   ├── 📄 constants.js           # Constantes
│   │   ├── 📄 helpers.js             # Funções auxiliares
│   │   └── 📄 calculations.js       # Cálculos financeiros
│   │
│   ├── 📁 styles/                     # Estilos globais
│   │   ├── 📄 globals.css            # Estilos globais
│   │   ├── 📄 variables.css          # Variáveis CSS
│   │   ├── 📄 components.css         # Estilos de componentes
│   │   └── 📄 responsive.css          # Media queries
│   │
│   ├── 📁 assets/                     # Assets estáticos
│   │   ├── 📁 images/
│   │   │   ├── 📄 logo.svg
│   │   │   ├── 📄 hero-bg.jpg
│   │   │   └── 📁 icons/
│   │   ├── 📁 fonts/
│   │   └── 📁 data/
│   │       └── 📄 mock-data.json
│   │
│   ├── 📁 tests/                  # Testes
│   │   ├── 📁 components/
│   │   ├── 📁 pages/
│   │   ├── 📁 hooks/
│   │   ├── 📁 services/
│   │   └── 📄 setupTests.js
│   │
│   ├── 📄 App.jsx                     # Componente principal
│   ├── 📄 App.css                     # Estilos do App
│   ├── 📄 index.js                    # Entry point
│   └── 📄 index.css                   # Estilos base
│
├── 📄 package.json                   # Dependências e scripts
├── 📄 package-lock.json              # Lock de dependências
├── 📄 vercel.json                    # Configuração Vercel
├── 📄 .env.local                     # Variáveis de ambiente local
├── 📄 .env.example                   # Exemplo de variáveis
├── 📄 .gitignore                     # Arquivos ignorados
├── 📄 README.md                      # Documentação do frontend
├── 📄 jsconfig.json                   # Configuração JavaScript
└── 📄 tailwind.config.js              # Configuração Tailwind (opcional)
```

### 2.3. Backend (Django + Render)

```text
backend/
├── 📁 config/                      # Configurações Django
│   ├── 📄 init.py
│   ├── 📄 asgi.py
│   ├── 📄 wsgi.py
│   ├── 📄 urls.py                  # URLs principais
│   ├── 📄 celery.py                # Configuração Celery
│   └── 📁 settings/                # Settings por ambiente
│       ├── 📄 init.py
│       ├── 📄 base.py              # Settings base
│       ├── 📄 development.py      # Settings desenvolvimento
│       ├── 📄 production.py       # Settings produção
│       └── 📄 testing.py          # Settings testes
│
├── 📁 apps/                       # Apps Django
│   ├── 📁 authentication/         # App de autenticação
│   │   ├── 📄 init.py
│   │   ├── 📄 admin.py
│   │   ├── 📄 apps.py
│   │   ├── 📄 models.py
│   │   ├── 📄 serializers.py
│   │   ├── 📄 views.py
│   │   ├── 📄 urls.py
│   │   ├── 📄 permissions.py
│   │   ├── 📄 services.py
│   │   ├── 📁 migrations/
│   │   └── 📁 tests/
│   │       ├── 📄 test_models.py
│   │       ├── 📄 test_views.py
│   │       └── 📄 test_services.py
│   │
│   ├── 📁 portfolios/             # App de carteiras
│   │   └── ...
│   ├── 📁 assets/                 # App de ativos
│   │   └── ...
│   ├── 📁 transactions/           # App de transações
│   │   └── ...
│   ├── 📁 market_data/            # App de dados de mercado
│   │   ├── 📄 tasks.py             # Tarefas Celery
│   │   └── ...
│   ├── 📁 analytics/              # App de analytics
│   │   └── ...
│   ├── 📁 public_api/             # App de API pública
│   │   └── ...
│   └── 📁 core/                   # App core (utilitários)
│       ├── 📄 models.py            # Modelos base
│       ├── 📄 exceptions.py        # Exceções customizadas
│       └── 📁 management/         # Comandos Django
│           └── 📁 commands/
│               ├── 📄 seed_data.py
│               └── 📄 update_prices.py
│
├── 📁 static/                     # Arquivos estáticos
│
├── 📁 media/                      # Arquivos de mídia
│
├── 📁 templates/                  # Templates Django
│
├── 📁 locale/                     # Internacionalização
│
├── 📁 fixtures/                   # Dados iniciais
│
├── 📁 logs/                       # Logs da aplicação
│
├── 📄 manage.py                    # Django management
├── 📄 requirements.txt             # Dependências Python
├── 📄 requirements-dev.txt         # Dependências desenvolvimento
├── 📄 Dockerfile                   # Container principal
├── 📄 Dockerfile.celery             # Container Celery
├── 📄 render.yaml                 # Configuração Render
├── 📄 .env.example                 # Exemplo variáveis ambiente
├── 📄 .gitignore                  # Arquivos ignorados
├── 📄 pytest.ini                  # Configuração pytest
├── 📄 setup.cfg                    # Configuração ferramentas
└── 📄 README.md                   # Documentação backend
```

### 2.4. Docker e Infraestrutura

```text
docker/
├── 📁 kong/                         # Kong API Gateway
│   ├── 📄 Dockerfile
│   ├── 📄 kong.yml                   # Configuração declarativa
│   └── 📄 plugins.lua                # Plugins customizados
│
├── 📁 keycloak/                     # Keycloak
│   ├── 📄 Dockerfile
│   ├── 📄 realm-config.json          # Configuração do realm
│   └── 📁 themes/                     # Temas customizados
│       └── 📁 carteira/
│
├── 📁 nginx/                        # Nginx (se necessário)
│   ├── 📄 Dockerfile
│   ├── 📄 nginx.conf
│   └── 📄 ssl.conf
│
└── 📁 monitoring/                   # Monitoramento
├── 📄 prometheus.yml
├── 📄 grafana-dashboard.json
└── 📄 alertmanager.yml
```

### 2.5. Scripts e Automação

```text
scripts/
├── 📄 docker-build.sh               # Build das imagens
├── 📄 docker-dev.sh                 # Ambiente desenvolvimento
├── 📄 docker-deploy.sh              # Deploy produção
├── 📄 setup-dev.sh                  # Setup inicial desenvolvimento
├── 📄 run-tests.sh                  # Execução de testes
├── 📄 backup-db.sh                  # Backup do banco
├── 📄 restore-db.sh                 # Restore do banco
├── 📄 migrate.sh                    # Migrações
├── 📄 seed-data.sh                  # Popular dados iniciais
└── 📄 health-check.sh               # Health check manual
```

### 2.6. Documentação

```text
docs/
├── 📄 README.md                     # Documentação principal
├── 📄 ARCHITECTURE.md               # Arquitetura detalhada
├── 📄 API.md                       # Documentação da API
├── 📄 DEPLOYMENT.md                 # Guia de deploy
├── 📄 DEVELOPMENT.md                # Guia de desenvolvimento
├── 📄 TESTING.md                    # Guia de testes
├── 📄 CONTRIBUTING.md               # Guia de contribuição
├── 📁 api/                          # Documentação OpenAPI
│   ├── 📄 openapi.yml
│   └── 📄 postman-collection.json
├── 📁 diagrams/                     # Diagramas
│   ├── 📄 architecture.png
│   ├── 📄 database-schema.png
│   └── 📄 user-flow.png
└── 📁 screenshots/                  # Screenshots da aplicação
├── 📄 dashboard.png
├── 📄 portfolio.png
└── 📄 mobile.png
```

### 2.7. CI/CD (GitHub Actions)

```text
.github/
├── 📁 workflows/
│   ├── 📄 frontend-ci.yml            # CI do frontend
│   ├── 📄 backend-ci.yml             # CI do backend
│   ├── 📄 deploy-staging.yml          # Deploy staging
│   ├── 📄 deploy-production.yml       # Deploy produção
│   ├── 📄 security-scan.yml           # Scan de segurança
│   └── 📄 performance-test.yml        # Testes de performance
├── 📁 ISSUE_TEMPLATE/
│   ├── 📄 bug_report.md
│   ├── 📄 feature_request.md
│   └── 📄 question.md
└── 📄 pull_request_template.md
```

---

## 🔧 3. Funcionalidades Detalhadas por Módulo

### 3.1. Autenticação e Gerenciamento de Usuário (Acesso Privado)
* **3.1.1:** Cadastro de Novo Usuário
* **3.1.2:** Login e "Esqueci minha senha"
* **3.1.3:** Logout
* **3.1.4:** Gerenciamento Básico de Perfil

### 3.2. Gerenciamento de Carteiras (Acesso Privado)
* **3.2.1:** Criação de Nova Carteira
* **3.2.2:** Listagem e Seleção de Carteiras
* **3.2.3:** Edição e Exclusão de Carteira

### 3.3. Registro de Ativos e Transações (Acesso Privado)
* **3.3.1:** Adicionar Novo Ativo (Registro Manual: Ações, FIIs, Renda Fixa)
* **3.3.2:** Registrar Novas Transações (Compra, Venda)
* **3.3.3:** Registrar Proventos (Dividendos, JCP, Rendimentos)
* **3.3.4:** Visualizar, Editar e Excluir Transações

### 3.4. Painel de Controle, Visualização e Análise
#### Sub-Módulo 3.4.A: Dashboard da Carteira (Privado)
* **3.4.A.1:** Visão Geral (Valor Total, Rentabilidade, Total Investido vs. Atual)
* **3.4.A.2:** Detalhamento de Ativos (Tabela com Posição, Preço Médio, Resultado)
* **3.4.A.3:** Gráficos de Composição (Por tipo de ativo, por ativo individual)

#### Sub-Módulo 3.4.B: Ferramentas de Consulta de Ativos (Público)
* **3.4.B.1:** Página de Fundamentos de Ativos (MVP)
* **3.4.B.2:** Comparador de Ativos (Pós-MVP)
* **3.4.B.3:** Screener/Filtro de Ativos (Pós-MVP)

### 3.5. Conteúdo Educacional e Informativo (Público - Pós-MVP)
* **3.5.1:** Blog/Artigos sobre Investimentos
* **3.5.2:** Glossário de Termos Financeiros

### 3.6. Interface Web Responsiva (MVP)
Todas as páginas serão acessíveis e funcionais em desktops, tablets e smartphones, baseadas em **HTML5 Semântico**.

---

## 📅 4. Cronograma Completo de Desenvolvimento

### 🚀 Fase 0: Smoke Test em Produção (Semana 1)
**Objetivo:** Validar toda a pipeline de deploy com aplicação mínima.

* **Dias 1-2: Setup Docker Completo**
    * ✅ Criar todos os Dockerfiles (API, Celery, Kong, Keycloak)
    * ✅ Configurar `docker-compose` para desenvolvimento
    * ✅ Testar ambiente local completo
    * ✅ Scripts de automação funcionando
* **Dias 3-4: Deploy Containerizado**
    * ✅ Configurar `render.yaml` com containers
    * ✅ Deploy de containers em produção
    * ✅ Validar comunicação entre serviços
    * ✅ Health checks funcionando
* **Dias 5-7: Validação e Otimização**
    * ✅ Testes de performance dos containers
    * ✅ Otimização de imagens Docker
    * ✅ Monitoramento de recursos
    * ✅ Documentação de containers

**Entregáveis da Semana 1:**
* URLs em produção funcionando
* Pipeline de deploy validada
* Infraestrutura base testada
* Baseline de performance estabelecida

### 🏗️ Fase 1: Fundação Robusta (Semanas 2-4)
**Objetivo:** Construir base sólida com deploy contínuo.

* **Semana 2: Infraestrutura Completa**
    * **Backend:** Estrutura Django com Clean Architecture
    * **Frontend:** Setup React com Design System básico
    * **DevOps:** Kong + Keycloak + RabbitMQ em produção
    * **Deploy:** Autenticação básica funcionando
* **Semana 3: Monitoramento e Segurança**
    * **Observabilidade:** Logs estruturados, métricas, alertas
    * **Segurança:** Rate limiting, CORS, validação de inputs
    * **Performance:** Cache básico com Redis, otimizações
    * **Deploy:** Sistema de monitoramento ativo
* **Semana 4: Backup e Disaster Recovery**
    * **Backup:** Automatizado com retenção configurada
    * **Recovery:** Procedimentos de restauração testados
    * **Documentação:** Runbooks operacionais
    * **Deploy:** Sistema de backup validado

**Entregáveis da Fase 1:**
* Infraestrutura completa e monitorada
* Autenticação funcionando em produção
* Procedimentos operacionais documentados
* Base sólida para desenvolvimento de features

### ⚡ Fase 2: MVP Incremental (Semanas 5-8)
**Objetivo:** Funcionalidades em produção a cada sprint.

* **Sprint 1 - Semana 5: Autenticação Completa**
    * **Backend:** APIs de cadastro, login, perfil
    * **Frontend:** Páginas de auth com HTML5 semântico
    * **Testes:** Cobertura de testes > 80%
    * **Deploy:** Fluxo completo de autenticação
* **Sprint 2 - Semana 6: Gestão de Carteiras**
    * **Backend:** CRUD completo de carteiras
    * **Frontend:** Interface para gerenciar carteiras
    * **Validação:** Usuários podem criar/editar carteiras
    * **Deploy:** Funcionalidade de carteiras ativa
* **Sprint 3 - Semana 7: Registro de Transações**
    * **Backend:** APIs para ativos e transações
    * **Frontend:** Formulários para registro de operações
    * **Validação:** Fluxo completo de adicionar ativos
    * **Deploy:** Sistema de transações funcionando
* **Sprint 4 - Semana 8: Dashboard Básico**
    * **Backend:** APIs de analytics e relatórios
    * **Frontend:** Dashboard com gráficos e métricas
    * **Validação:** Visualização de dados reais
    * **Deploy:** Dashboard completo em produção

**Entregáveis da Fase 2:**
* MVP funcional em produção
* Usuários podem gerenciar carteiras completas
* Dashboard com visualizações básicas
* Sistema de transações operacional

### 🔗 Fase 3: Integrações e Dados (Semanas 9-12)
**Objetivo:** Dados de mercado e funcionalidades públicas.

* **Sprint 5 - Semana 9: APIs de Terceiros**
    * **Backend:** Integração com provedores de cotações
    * **Cache:** Sistema inteligente de cache com Redis
    * **Async:** Processamento assíncrono com Celery
    * **Deploy:** Cotações em tempo real
* **Sprint 6 - Semana 10: Funcionalidades Públicas**
    * **Backend:** APIs públicas para consulta de ativos
    * **Frontend:** Páginas públicas (sem login)
    * **SEO:** Otimização para motores de busca
    * **Deploy:** Seção pública ativa
* **Sprint 7 - Semana 11: Analytics Avançadas**
    * **Backend:** Cálculos de performance e risco
    * **Frontend:** Gráficos avançados e comparações
    * **Performance:** Otimizações de queries
    * **Deploy:** Analytics completas
* **Sprint 8 - Semana 12: Polimento e Otimização**
    * **UX/UI:** Refinamentos de interface
    * **Performance:** Otimizações finais
    * **Testes:** Testes E2E completos
    * **Deploy:** Versão 1.0 estável

**Entregáveis da Fase 3:**
* Dados de mercado em tempo real
* Funcionalidades públicas ativas
* Analytics avançadas implementadas
* Plataforma completa e otimizada

