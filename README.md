# 📊 Dashboard Interativo de Marketing Digital

Bem-vindo ao dashboard interativo de marketing digital, uma ferramenta poderosa para monitorar e analisar o desempenho de campanhas de marketing digital em tempo real.

## 🚀 Descrição

Este projeto cria um dashboard interativo para monitorar e analisar o desempenho de campanhas de marketing digital em diversas plataformas, facilitando a tomada de decisões baseada em dados. Ele permite a visualização centralizada de métricas chave de marketing, fornecendo insights valiosos para otimizar campanhas.

**Nota:** Os dados de Facebook Ads utilizados neste projeto são fictícios, já que não há campanhas reais disponíveis. No entanto, o código está preparado para extrair dados reais de campanhas de Facebook Ads caso você configure a API corretamente.

## 🌟 Benefícios

- **Monitoramento em Tempo Real**: Acompanhe suas campanhas de marketing digital em tempo real.
- **Insights Aprofundados**: Obtenha insights detalhados sobre o desempenho de suas campanhas.
- **Visualizações Interativas**: Utilize gráficos dinâmicos e interativos para explorar seus dados.
- **Decisões Informadas**: Facilite a tomada de decisões baseada em dados precisos e atualizados.

## 🛠️ Ferramentas Utilizadas

- **Python**: Pandas, Plotly, Dash
- **APIs**: Google Analytics API, Facebook Graph API
- **Jupyter Notebook**: Para análise e prototipagem
- **Dash**: Para criação do dashboard interativo

## 📁 Estrutura do Projeto

```plaintext
marketing_dashboard_project/
├── data/
│   ├── google_analytics_data.json
│   ├── facebook_ads_data.json
├── notebooks/
│   ├── criacao_dados_ficticios.ipynb
│   ├── data_analysis.ipynb
│   ├── data_visualization.ipynb
├── src/
│   ├── data_loader.py
│   ├── data_visualization.py
│   ├── dashboard.py
├── assets/
│   ├── styles.css
├── .gitignore
├── Procfile
├── README.md
├── requirements.txt
```

## 📝 Guia Rápido

### Pré-requisitos

- **Python 3.7 ou superior**
- **Conta no Google Cloud Platform e Facebook Developers**
- **Credenciais para APIs do Google Analytics e Facebook**

### Instalação

1. **Clonar o repositório**:
   ```bash
   git clone https://github.com/seu_usuario/dashboard_interativo_marketing_digital.git
   cd dashboard_interativo_marketing_digital
   ```

2. **Criar e ativar um ambiente virtual**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instalar as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar credenciais das APIs**:
   - Adicione os arquivos `client_secret.json` e `config.json` na pasta `data`.

### Extração de Dados do Facebook Ads

O código está preparado para extrair dados de campanhas do Facebook Ads através da API do Facebook Graph. Para configurar a API e extrair dados reais, siga os passos abaixo:

1. **Criar uma aplicação no Facebook Developers**:
   - Acesse [Facebook Developers](https://developers.facebook.com/) e crie uma nova aplicação.
   - Adicione o produto "Marketing API" à sua aplicação.

2. **Gerar um Token de Acesso**:
   - Vá para a seção "Ferramentas" no Facebook Developers e gere um token de acesso para autenticação.

3. **Configurar o código**:
   - Insira o token de acesso e outras credenciais necessárias no arquivo `config.json` localizado na pasta `data`.

4. **Extração dos Dados**:
   - Se houver campanhas ativas configuradas na API do Facebook, o código automaticamente extrairá esses dados.
   - Caso não existam dados reais, o código gerará automaticamente dados fictícios para fins de demonstração.

5. **Gerar dados fictícios (se necessário)**:
   - Execute o notebook `notebooks/criacao_dados_ficticios.ipynb` no Jupyter Notebook para gerar dados fictícios.

### Análise e Visualização de Dados

1. **Analisar dados**:
   - Execute o notebook `notebooks/data_analysis.ipynb` para análise de dados.

2. **Visualizar dados**:
   - Execute o notebook `notebooks/data_visualization.ipynb` para visualização de dados.

### Executar o Dashboard

1. **Iniciar o servidor do Dash**:
   - Execute o seguinte comando para iniciar o dashboard:
     ```bash
     python src/dashboard.py
     ```
   - Abra o navegador e acesse [http://127.0.0.1:8050/](http://127.0.0.1:8050/) para visualizar o dashboard.

### Deploy no Heroku

1. **Inicializar repositório Git e criar aplicativo Heroku**:
   ```bash
   git init
   heroku create
   git add .
   git commit -m "Initial commit"
   git push heroku master
   heroku open
   ```

## 📂 Estrutura dos Arquivos

### `data_loader.py`

Carrega e processa dados das APIs.

### `data_visualization.py`

Cria gráficos interativos usando Plotly.

### `dashboard.py`

Configura o layout e a lógica do dashboard com Dash.

## 📝 Licença

Este projeto está licenciado sob os termos da licença MIT.

## 🤝 Contribuição

Sinta-se à vontade para abrir issues e enviar pull requests. Toda contribuição é bem-vinda!