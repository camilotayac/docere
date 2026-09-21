// =============================================================================
// elements.typ  —  Elementos del documento: TOC clásico, captions y notas al pie
// =============================================================================
//
// PROPÓSITO:
//   Aplica los estilos de elementos editoriales clásicos de quimica_tayac:
//     • Tabla de contenidos (TOC) con estilo académico: rótulo de capítulo
//       en itálica ("Capítulo uno"), línea de puntos directriz (#repeat[ . ])
//       y enlaces activos a cada sección y página.
//     • Captions de figuras y tablas con suplemento y número en negrita.
//     • Separador sutil de notas al pie.
// =============================================================================

#let apply-elements(main-fonts, title-fonts, is-dual-font, body) = {

  // ── Captions de figuras y tablas ──
  show figure.caption: it => {
    set text(font: if is-dual-font { title-fonts } else { main-fonts }, size: 0.88em)
    text(weight: "bold", tracking: 0.03em)[#it.supplement #it.counter.display()]
    [#it.separator ]
    it.body
  }

  // ── Notas al pie ──
  set footnote.entry(
    separator: line(length: 30%, stroke: 0.4pt + luma(180)),
    indent: 0em,
  )
  show footnote.entry: set text(font: main-fonts, size: 8.5pt)

  // ── Tabla de contenidos clásica con hiperenlaces y puntos ──
  show outline.entry.where(level: 1): it => {
    v(1.2em)
    block(width: 100%, breakable: false)[
      #if it.element != none and it.element.numbering != none {
        let ch-num = counter(heading).at(it.element.location()).first()
        let num-words = (
          "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez",
          "once", "doce", "trece", "catorce", "quince", "dieciséis", "diecisiete", "dieciocho", "diecinueve", "veinte"
        )
        let word-str = if ch-num > 0 and ch-num <= num-words.len() { num-words.at(ch-num - 1) } else { str(ch-num) }
        text(size: 0.88em, style: "italic", fill: rgb("#a06050"))[Capítulo #word-str]
        linebreak()
      }
      #set text(size: 1.05em, weight: "bold", font: main-fonts)
      #if it.element != none {
        link(it.element.location())[
          #it.element.body
          #box(width: 1fr, inset: (x: 0.4em), text(fill: luma(170))[#repeat[ . ]])
          #it.element.location().page()
        ]
      } else {
        it.body
      }
    ]
    v(0.3em)
  }

  show outline.entry.where(level: 2): it => {
    block(width: 100%, inset: (left: 1.2em, bottom: 0.2em))[
      #set text(size: 0.92em, font: main-fonts)
      #if it.element != none {
        link(it.element.location())[
          #if it.element.numbering != none {
            let h-nums = counter(heading).at(it.element.location())
            let sec-idx = if h-nums.len() > 1 { h-nums.at(1) } else { h-nums.first() }
            text(weight: "bold", fill: rgb("#a06050"))[#sec-idx.]
            h(0.4em)
          }
          #it.element.body
          #box(width: 1fr, inset: (x: 0.4em), text(fill: luma(170))[#repeat[ . ]])
          #it.element.location().page()
        ]
      } else {
        it.body
      }
    ]
  }

  body
}
