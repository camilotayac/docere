// =============================================================================
// typst-show.typ  —  Orquestador principal de estilo (Natura Docens)
// =============================================================================
//
// PROPÓSITO:
//   Aplica la estética editorial completa de quimica_tayac sin dependencias
//   externas ni marginalia restrictiva. Integra:
//     • Tipografía Palatino con interlineado editorial.
//     • Páginas de apertura de capítulo con patrón de iconos educativos.
//     • Jerarquía de encabezados (Niveles 2-4) con tracking y acentos.
//     • Tabla de contenidos clásica con líneas de puntos y enlaces activos.
//     • Páginas divisorias de Parte (I, II, III...) con diseño centrado.
//     • Colofón final de edición académica.
// =============================================================================

#import "_templates/typst/chapter-page.typ": apply-chapter-style
#import "_templates/typst/headings.typ":     apply-section-styles
#import "_templates/typst/elements.typ":     apply-elements
#import "_templates/typst/frontmatter.typ":    render-frontmatter

// ── Tipografía (Palatino / Hermann Zapf) ──
#let main-font  = "$if(mainfont)$$mainfont$$else$Palatino$endif$"
#let main-fonts = (main-font, "Libertinus Serif", "New Computer Modern")

$if(sansfont)$
#let title-font  = "$sansfont$"
#let title-fonts = (title-font, "Helvetica Neue", "Arial")
#let is-dual-font = true
$else$
#let title-font  = main-font
#let title-fonts = main-fonts
#let is-dual-font = false
$endif$

// ── Metadatos del documento ──
#set document(
  title: "$if(title)$$title$$endif$",
  author: "$if(by-author)$$for(by-author)$$it.name.literal$$sep$, $endfor$$elseif(author)$$author$$endif$",
)

#set text(
  font:     main-fonts,
  size:     $if(fontsize)$$fontsize$$else$11pt$endif$,
  lang:     "$if(lang)$$lang$$else$es$endif$",
)

#set par(
  justify:  true,
  leading:  ($if(linestretch)$$linestretch$$else$1.4$endif$ - 0.7) * 1em,
)

// ── Numeración de secciones ──
$if(section-numbering)$
#set heading(numbering: "$section-numbering$")
$endif$

// ── Divisores de Parte (Quarto book parts) ──
#let part-counter = counter("book-part")

#let part(title) = {
  part-counter.step()
  page(
    paper: "a4",
    header: none,
    footer: none,
    fill: rgb("#f6f3ee"),
  )[
    #v(1fr)
    #align(center)[
      #context {
        let p-num = part-counter.get().first()
        let romans = ("I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X")
        let rom-str = if p-num > 0 and p-num <= romans.len() { romans.at(p-num - 1) } else { str(p-num) }
        text(size: 13pt, tracking: 0.25em, fill: rgb("#a06050"), weight: "bold")[
          #upper("Parte " + rom-str)
        ]
      }
      #v(0.8em)
      #text(size: 26pt, font: title-fonts, weight: "bold", fill: rgb("#2b2b2b"))[
        #smallcaps(title)
      ]
      #v(1em)
      #rect(width: 80pt, height: 2pt, fill: rgb("#a06050"))
    ]
    #v(1fr)
  ]
}

// ── Apéndices ──
#let appendices(title, hide-parent: false, body) = {
  pagebreak(weak: true)
  if not hide-parent {
    v(2em)
    align(center, text(size: 20pt, weight: "bold", fill: rgb("#a06050"))[#title])
    v(1em)
  }
  body
}

// ── Aplicar módulos de estilo ──
#show: apply-chapter-style.with(main-fonts, title-fonts, is-dual-font)
#show: apply-section-styles.with(main-fonts, title-fonts, is-dual-font)
#show: apply-elements.with(main-fonts, title-fonts, is-dual-font)

// ── Bloques de código con fondo suave y borde fino ──
#show raw.where(block: true): set block(
  fill:   luma(246),
  width:  100%,
  inset:  8pt,
  radius: 3pt,
  stroke: 0.4pt + luma(225),
)

// ── Secuencia Preliminar (Portada, Portadilla, Créditos Institucionales) ──
#render-frontmatter(main-fonts, title-fonts)

// ── Tabla de contenidos ──
$if(toc)$
#outline(
  title: "$if(toc-title)$$toc-title$$else$Tabla de contenidos$endif$",
  depth: $if(toc-depth)$$toc-depth$$else$2$endif$,
  indent: 1.5em,
)
#pagebreak()
$endif$

// ── Configuración de Bibliografía nativa (el título proviene de bibliografia.qmd) ──
#set bibliography(title: none, full: true)

// ── Reemplazar líneas divisorias horizontales por espacio vertical en blanco ──
#let horizontalrule = v(1.8em)
