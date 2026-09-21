// =============================================================================
// chapter-page.typ  —  Página de apertura de capítulo (Estilo quimica_tayac)
// =============================================================================
//
// PROPÓSITO:
//   Renderiza la página de inicio de capítulo (encabezados de Nivel 1) con
//   el diseño editorial de quimica_tayac, adaptado para Natura Docens:
//     • Fondo sutil con textura geométrica de iconos educativos (libro, birrete,
//       átomo, compás, hoja botánica, matraz).
//     • Rotulación: "Capítulo [en letras]" en itálica terracota (#a06050).
//     • Título de capítulo grande en negrita (2.2em).
//     • Filete horizontal de acento.
//     • Sin márgenes exagerados (aprovecha el ancho completo del documento).
//     • Reinicio automático de contadores de figuras, tablas y ecuaciones.
// =============================================================================

#import "icons.typ": icon-book, icon-mortarboard, icon-science, icon-compass, icon-leaf, icon-flask

// ── Parámetros de diseño ──
#let chapter-bg-color = rgb("#f6f3ee")
#let accent-color     = rgb("#a06050")
#let pattern-stroke   = 0.45pt + rgb("#dfd8cf")

#let apply-chapter-style(main-fonts, title-fonts, is-dual-font, body) = {
  show heading.where(level: 1): it => {
    // ── Reset de contadores por capítulo ──
    counter(figure.where(kind: "quarto-float-fig")).update(0)
    counter(figure.where(kind: "quarto-float-tbl")).update(0)
    counter(figure.where(kind: "quarto-float-lst")).update(0)
    counter(figure.where(kind: "quarto-callout-Note")).update(0)
    counter(figure.where(kind: "quarto-callout-Warning")).update(0)
    counter(figure.where(kind: "quarto-callout-Caution")).update(0)
    counter(figure.where(kind: "quarto-callout-Tip")).update(0)
    counter(figure.where(kind: "quarto-callout-Important")).update(0)
    counter(math.equation).update(0)

    // ── Encabezados de Nivel 1 ──
    if it.numbering == none {
      // Secciones preliminares o especiales sin numeración: flujo editorial continuo
      v(1.8em)
      block(width: 100%, breakable: false)[
        #text(
          size: 2em,
          weight: "bold",
          fill: accent-color,
          font: if is-dual-font { title-fonts } else { main-fonts },
        )[#it.body]
        #v(0.4em)
        #rect(width: 60pt, height: 2pt, fill: accent-color)
      ]
      v(1em)
    } else {
      // Página de apertura con fondo y patrón de iconos educativos para capítulos numerados
      page(
        paper: "a4",
        fill: chapter-bg-color,
        margin: (left: 2.5cm, right: 2.5cm, top: 3.2cm, bottom: 3cm),
        header: none,
        footer: none,
        background: {
          // Patrón reticular de iconos educativos sutiles
          for i-row in range(12) {
            for i-col in range(9) {
              let cx = i-col * 68pt + 12pt
              let cy = i-row * 68pt + 16pt
              let icon-idx = calc.rem(i-row * 3 + i-col * 5, 6)

              place(top + left, dx: cx, dy: cy)[
                #if icon-idx == 0 {
                  icon-book(size: 20pt, stroke-color: rgb("#d6cec4"))
                } else if icon-idx == 1 {
                  icon-mortarboard(size: 20pt, stroke-color: rgb("#d6cec4"))
                } else if icon-idx == 2 {
                  icon-science(size: 20pt, stroke-color: rgb("#d6cec4"))
                } else if icon-idx == 3 {
                  icon-compass(size: 20pt, stroke-color: rgb("#d6cec4"))
                } else if icon-idx == 4 {
                  icon-leaf(size: 20pt, stroke-color: rgb("#d6cec4"))
                } else {
                  icon-flask(size: 20pt, stroke-color: rgb("#d6cec4"))
                }
              ]
            }
          }
        },
      )[
        #set align(left)
        #set par(first-line-indent: 0pt, justify: false)
        #set text(font: main-fonts, lang: "es", hyphenate: false)
        #v(2.5cm)

        // ── Bloque de título de capítulo ──
        #block(width: 80%)[
          #let ch-int = counter(heading).get().first()
          #let num-words = (
            "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez",
            "once", "doce", "trece", "catorce", "quince", "dieciséis", "diecisiete", "dieciocho", "diecinueve", "veinte",
            "veintiuno", "veintidós", "veintitrés", "veinticuatro", "veinticinco", "veintiséis", "veintisiete", "veintiocho", "veintinueve", "treinta"
          )
          #let word-str = if ch-int > 0 and ch-int <= num-words.len() { num-words.at(ch-int - 1) } else { counter(heading).display(it.numbering) }

          #text(
            size: 1.25em,
            style: "italic",
            weight: "medium",
            fill: accent-color,
            font: main-fonts,
          )[Capítulo #word-str]
          #v(0.35em)

          // Título del capítulo (h1)
          #text(
            size: 2.3em,
            weight: "bold",
            fill: luma(20),
            font: if is-dual-font { title-fonts } else { main-fonts },
          )[#it.body]

          #v(0.6em)
          #rect(width: 70pt, height: 2.5pt, fill: accent-color)
        ]
      ]
    }
  }

  body
}
