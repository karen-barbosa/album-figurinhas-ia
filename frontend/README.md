# Copa do Mundo Tech - Álbum de Figurinhas Alura

Este é um projeto interativo de um **Álbum de Figurinhas Digital** focado em grandes personalidades e tecnologias do mundo tech (como pioneiros da Inteligência Artificial, criadores do Python e arquitetos de Banco de Dados). Ele simula a experiência de folhear um álbum físico de figurinhas diretamente no navegador.

---

## 🎯 Objetivo do Projeto

O objetivo principal é criar um álbum de figurinhas interativo e dinâmico que sirva como um portfólio e um tributo a grandes nomes da tecnologia. Ele utiliza uma biblioteca JavaScript para gerar uma transição suave de folheamento de páginas e se conecta a uma API backend (desenvolvida com FastAPI) para carregar e preencher as figurinhas de forma dinâmica.

---

## 📂 Estrutura e Funcionalidades dos Arquivos

O projeto está estruturado na pasta `frontend` com os seguintes arquivos principais:

### 1. 📄 [index.html](file:///c:/Users/Karen%20Barbosa/Downloads/i-arq-ia-alura-album-main/frontend/index.html)
* **Função**: Estrutura e conteúdo do Álbum.
* **Detalhes**:
  * Define a marcação de todas as páginas do livro, incluindo a capa e as páginas internas de categorias (ex: *IA*, *Python*, *Banco de Dados*).
  * Cria os espaços vazios (*slots*) onde as figurinhas serão coladas com base nos IDs (ex: `#01`, `#02`).
  * Contém os elementos de navegação (botões de anterior e próximo) e controles de som.

### 2. 🎨 [style.css](file:///c:/Users/Karen%20Barbosa/Downloads/i-arq-ia-alura-album-main/frontend/style.css)
* **Função**: Estilização, layout e efeitos visuais.
* **Detalhes**:
  * Define a identidade visual do projeto, com uma paleta de cores moderna inspirada no espaço e tecnologia (tons de azul escuro, preto e brilhos neon).
  * Controla os efeitos de animação 3D, rotações, o efeito de texto em estilo "glitch" e transições de hover.
  * Define a exibição responsiva e o layout em grid para o alinhamento das figurinhas.

### 3. ⚡ [app.js](file:///c:/Users/Karen%20Barbosa/Downloads/i-arq-ia-alura-album-main/frontend/app.js)
* **Função**: Comportamento dinâmico e consumo de dados.
* **Detalhes**:
  * Inicializa e configura a biblioteca `St.PageFlip` para possibilitar o efeito realista de folhear as páginas do álbum.
  * Realiza uma requisição do tipo `fetch` para o backend FastAPI (por padrão em `http://localhost:8000/figurinhas`) para obter os dados das figurinhas.
  * Preenche automaticamente os espaços vazios do álbum com as imagens correspondentes obtidas da API.
  * Gerencia os controles de áudio (mudo/ativado) e os eventos de clique e arrastar das páginas.

---

## 🛠️ Tecnologias Utilizadas

* **HTML5** & **CSS3** (Variáveis CSS, CSS Grid, Flexbox, Animações).
* **JavaScript** (ES6+, Fetch API, manipulação de DOM).
* **St.PageFlip** (Biblioteca JS para o efeito de transição de páginas de livro).
* **FastAPI** (Backend opcional para servir os dados e imagens das figurinhas).
