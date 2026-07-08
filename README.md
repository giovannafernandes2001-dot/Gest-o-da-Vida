# Gestão da Vida — protótipo

Esboço de alta fidelidade do app "Gestão da Vida", construído a partir do conteúdo já compartilhado por Rubens Luiz Bernardes da Costa (Declarações de Fé, lema de vida, estrutura da planilha original, roteiro devocional de 7 passos).

Não é o produto final — é uma base concreta pra conversa e ajuste antes da construção real.

## Ver o protótipo

Abra `index.html` diretamente no navegador, ou publique numa hospedagem estática (Netlify, GitHub Pages, etc.) e acesse pela URL.

`index.html` é um arquivo único e autocontido: fontes, imagens e o vídeo de abertura já estão embutidos nele (base64), sem nenhuma requisição externa.

## Estrutura do repositório

- `index.html` — o protótipo, pronto pra abrir ou publicar.
- `src/gestao-da-vida-preview.template.html` — o código-fonte editável (com placeholders `__TOKEN__` no lugar dos assets).
- `src/build.py` — script que substitui os placeholders pelos assets em base64 e gera `index.html`.
- `src/fonts/`, `src/fonts2/`, `src/fonts3/` — fontes usadas (Karla, Gilda Display, Cormorant Garamond, Space Mono), em arquivo original e em `.b64`.
- `src/kittl2/` — símbolo, monograma e ícones da marca (gerados no Kittl), em PNG e `.b64`.
- `src/video/` — vídeo de abertura da marca (mp4 e webm), em arquivo original e em `.b64`.

## Editar e reconstruir

1. Edite `src/gestao-da-vida-preview.template.html`.
2. Rode `python3 build.py` de dentro de `src/` — ele gera um `gestao-da-vida-preview.html` ali mesmo.
3. Copie o resultado pra `index.html` na raiz do repositório.
