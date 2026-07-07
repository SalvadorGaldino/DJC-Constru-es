# DJC Construções — Site institucional

Site one-page para a DJC Construções, empresa de construção civil e
reformas no Litoral do Paraná. HTML/CSS/JS puro, sem frameworks e sem
build step — abre direto no navegador ou sobe em qualquer host estático.

## 📁 Estrutura do projeto

```
djc-construcoes/
├── index.html            → estrutura e conteúdo da página
├── css/
│   └── style.css          → estilos (tema claro padrão + escuro opcional)
├── js/
│   └── script.js           → interações (nav, tema, contadores, reveal)
├── img/
│   ├── LEIA-ME.txt         → avisos e lista do que ainda precisa ser trocado
│   ├── logo.png, favicon-*.png, apple-touch-icon.png → identidade visual real
│   └── obra1-5.jpg, sobre.jpg, og-image.jpg → ⚠️ IMAGENS PROVISÓRIAS (ver abaixo)
├── scripts/
│   └── generate_placeholders.py → gera as imagens provisórias (ferramenta de
│                                    dev; não precisa subir para produção)
├── robots.txt              → instruções para motores de busca
├── sitemap.xml             → mapa do site para o Google
├── site.webmanifest        → permite "adicionar à tela inicial" no mobile
└── README.md               → este arquivo
```

## ✅ O que foi entregue nesta versão

- **Segurança**: todos os links que abrem em nova aba agora usam
  `rel="noopener noreferrer"`, prevenindo o ataque de *tabnabbing*.
- **SEO**: meta tags Open Graph e Twitter Card (preview bonito ao
  compartilhar no WhatsApp/Instagram), `canonical`, dados estruturados
  Schema.org (`GeneralContractor`) para o Google entender que é uma
  empresa de construção local, `robots.txt` e `sitemap.xml`.
- **Performance**: imagens abaixo da dobra com `loading="lazy"` e
  `decoding="async"`, dimensões (`width`/`height`) declaradas para
  evitar layout shift (CLS), script carregado com `defer`.
- **Acessibilidade**: link "Pular para o conteúdo" (skip-link), estado
  `aria-expanded` no botão do menu mobile, fechamento do menu com a
  tecla ESC, foco visível ao navegar por teclado, animação de contador
  respeita `prefers-reduced-motion`.
- **Manutenibilidade**: ano do rodapé agora é gerado automaticamente
  via JavaScript — nunca mais fica desatualizado.
- **Organização**: CSS e JS movidos para pastas próprias (`css/`, `js/`),
  como em qualquer projeto profissional.

## 🖼️ Imagens provisórias — ação necessária antes de ir ao ar

O projeto já vem com **7 imagens provisórias geradas** (`obra1-5.jpg`,
`sobre.jpg`, `og-image.jpg`) no mesmo estilo visual da marca, só para o
site não ficar com espaços vazios durante a apresentação.

**Elas não são fotos reais.** Antes do lançamento definitivo, troque-as
por fotos verdadeiras das obras da DJC — veja `img/LEIA-ME.txt` para a
lista exata de nomes de arquivo esperados por cada seção.

## 🚀 Deploy

Qualquer uma destas opções funciona sem nenhuma configuração extra:

- **Vercel**: arraste a pasta em vercel.com/new, ou `vercel deploy` via CLI.
- **Cloudflare Pages**: conecte o repositório Git e aponte para a raiz.
- **GitHub Pages**: suba para um repositório e ative Pages nas configurações.

Antes do deploy final, troque `https://www.djcconstrucoes.com.br/` pelo
domínio real da DJC em:
- `index.html` (tags `canonical`, `og:url`, `og:image`, JSON-LD)
- `robots.txt`
- `sitemap.xml`

## 📊 Sugestões de evolução (não incluídas nesta entrega)

- Google Analytics 4 ou Plausible para medir tráfego e conversões.
- Formulário de contato próprio (além do WhatsApp) com envio por e-mail.
- Depoimentos de clientes (prova social aumenta conversão).
- Blog simples para SEO de conteúdo (ex: "quanto custa construir em
  Pontal do Paraná").
