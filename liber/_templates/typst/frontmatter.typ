// =============================================================================
// frontmatter.typ  —  Portada y Portadilla Interior
// =============================================================================
//
// PROPÓSITO:
//   Renderiza las páginas preliminares para la edición impresa / PDF:
//     1. Portada oficial a sangre completa (Portada.pdf).
//     2. Portadilla interior con título, subtítulo disciplinar, mención
//        de autoría de Camilo Tayac y sello de la colección.
//   La información institucional y curricular detallada se encuentra en
//   `index.qmd`, sincronizada tanto para la versión web como para el PDF.
// =============================================================================

#import "institucion.typ": datos-proyecto

#let render-frontmatter(main-fonts, title-fonts) = {
  let accent-color = rgb("#a06050")

  // ── 1. Portada Oficial a Sangre Completa ──
  page(
    paper: "a4",
    margin: 0pt,
    header: none,
    footer: none,
  )[
    #image("/Portada.pdf", width: 100%, height: 100%, fit: "cover")
  ]

  // ── 2. Portadilla Interna (Falsa Portada) ──
  page(
    paper: "a4",
    margin: (x: 2.5cm, top: 3.5cm, bottom: 3cm),
    header: none,
    footer: none,
    fill: rgb("#f7f5f0"),
  )[
    #set text(font: main-fonts, lang: "es")
    #v(1.5cm)

    #align(center)[
      #text(size: 10pt, tracking: 0.28em, fill: accent-color, weight: "bold")[
        PLAN DE ÁREA Y GUÍA DIDÁCTICA
      ]
      #v(0.8cm)

      #text(size: 32pt, font: title-fonts, weight: "bold", tracking: 0.08em, fill: rgb("#242424"))[
        #upper(datos-proyecto.titulo)
      ]
      #v(0.4cm)

      #text(size: 13.5pt, font: main-fonts, style: "italic", fill: luma(65))[
        #datos-proyecto.subtitulo
      ]
      #v(1.2cm)

      #rect(width: 70pt, height: 2pt, fill: accent-color)

      #v(1fr)

      #text(size: 9.5pt, style: "italic", fill: luma(90))[
        #datos-proyecto.rol-autor
      ]
      #v(0.4em)

      #text(size: 16pt, font: main-fonts, weight: "bold", tracking: 0.1em, fill: rgb("#242424"))[
        #upper(datos-proyecto.autor)
      ]

      #v(1.8cm)

      #text(size: 8.5pt, tracking: 0.2em, fill: luma(110), weight: "medium")[
        #upper(datos-proyecto.coleccion)
      ]
      #v(0.5cm)
    ]
  ]
}
