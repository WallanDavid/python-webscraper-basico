# 🌐 Python Web Scraper com Interface Gráfica

Este é um projeto de Web Scraper desenvolvido em **Python** que permite extrair **informações, imagens e vídeos** de páginas web. A aplicação conta com uma **interface gráfica intuitiva**, construída com `Tkinter`, e utiliza as bibliotecas `BeautifulSoup`, `requests`, `Pillow` e `moviepy` para realizar a extração e manipulação dos dados.

---

## 🧠 Funcionalidades

- 💻 Interface Gráfica Amigável: Insira uma URL e extraia informações com um clique
- 🖼️ Extração de Mídia: Coleta URLs de imagens e vídeos da página fornecida
- 📁 Salvamento de Arquivos: Imagens extraídas são salvas automaticamente no diretório do projeto
- 🕘 Histórico de Consultas: Registra a data e hora de cada extração realizada
- 📜 Área de Resultados: Exibe todas as URLs e dados extraídos na tela de forma organizada

---

## 🔧 Como Executar

1. Clone o repositório:  
   git clone https://github.com/WallanDavid/python-webscraper-basico.git

2. Acesse o diretório:  
   cd python-webscraper-basico

3. Instale as dependências:  
   pip install requests beautifulsoup4 Pillow moviepy

4. Execute o script principal:  
   python scrapping.py

---

## 🖱️ Modo de Uso

- Digite a URL desejada na caixa de entrada
- Clique no botão **"Obter Informações"**
- Os dados extraídos aparecerão na área de texto
- As imagens e vídeos serão salvos localmente
- Consulte o histórico no painel da interface

---

## 📌 Observações

- As imagens são salvas na mesma pasta do script
- Certifique-se de estar conectado à internet ao rodar o scraper
- Sites com conteúdo dinâmico (JavaScript) podem exigir técnicas mais avançadas (Selenium, etc.)
- O código está organizado de forma simples para facilitar futuras expansões

---

## 🚀 Possíveis Melhorias Futuras

- Suporte a scraping assíncrono com `aiohttp`
- Filtragem por tipos de mídia ou palavras-chave
- Exportação dos resultados para CSV ou JSON
- Extração de textos, links, títulos e metadados
- Integração com navegador via `selenium` para lidar com páginas dinâmicas

---

## 🤝 Contribuições

Contribuições são bem-vindas!  
Sinta-se à vontade para abrir issues com ideias, relatar bugs ou enviar pull requests com melhorias e novos recursos.

---

## 📜 Licença

Este projeto está licenciado sob os termos da [MIT License](LICENSE).

---

## 📫 Contato

**Desenvolvedor:** Wallan David Peixoto  
**Email:** bobwallan2@gmail.com  
**LinkedIn:** https://www.linkedin.com/in/wallanpeixoto
