# 📊 Dashboard Interativo de Marketing Digital

Bem-vindo ao dashboard interativo de marketing digital, uma ferramenta poderosa para monitorar e analisar o desempenho de campanhas de marketing digital em tempo real.

## 🚀 Descrição

Este projeto cria um dashboard interativo para monitorar e analisar o desempenho de campanhas de marketing digital em diversas plataformas, facilitando a tomada de decisões baseada em dados. Ele permite a visualização centralizada de métricas chave de marketing, fornecendo insights valiosos para otimizar campanhas.

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

5. **Gerar dados fictícios**:
   - Execute o notebook `notebooks/criacao_dados_ficticios.ipynb` no Jupyter Notebook.

6. **Analisar dados**:
   - Execute o notebook `notebooks/data_analysis.ipynb` para análise de dados.

7. **Visualizar dados**:
   - Execute o notebook `notebooks/data_visualization.ipynb` para visualização de dados.

8. **Executar o dashboard**:
   ```bash
   python src/dashboard.py
   ```

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

## 📸 Exemplos Visuais

### Capturas de Tela

![Exemplo de Gráfico](path/to/screenshot.png)

*Adicione uma captura de tela do dashboard aqui para ilustrar o que os usuários podem esperar.*

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