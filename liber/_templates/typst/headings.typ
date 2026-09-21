// =============================================================================
// headings.typ  —  Estilos de secciones (Nivel 2, 3 y 4) estilo quimica_tayac
// =============================================================================
//
// PROPÓSITO:
//   Aplica la jerarquía tipográfica clásica de quimica_tayac a las secciones:
//     • Nivel 2: Smallcaps con espaciado entre letras (tracking: 0.08em),
//       peso bold y margen vertical generoso.
//     • Nivel 3: Itálica refinada con espaciado limpio.
//     • Nivel 4: Párrafo titulado en línea (bold italic).
//     • Desactivación de partición de palabras con guión en encabezados.
// =============================================================================

#let apply-section-styles(main-fonts, title-fonts, is-dual-font, body) = {

  // Desactivar división de palabras con guión y justificación en encabezados
  show heading: set text(hyphenate: false)
  show heading: set par(justify: false)

  // ── Nivel 2: Sección ──
  show heading.where(level: 2): it => {
    v(2.2em)
    block(breakable: false, width: 100%)[
      #set text(font: if is-dual-font { title-fonts } else { main-fonts }, size: 1.18em)
      #if it.numbering != none {
        text(weight: "bold", fill: rgb("#a06050"))[#counter(heading).display(it.numbering)#h(0.7em)]
      }
      #text(weight: "bold", tracking: 0.04em, it.body)
    ]
    v(0.85em)
  }

  // ── Nivel 3: Subsección ──
  show heading.where(level: 3): it => {
    v(1.3em)
    block(breakable: false, width: 100%)[
      #set text(font: if is-dual-font { title-fonts } else { main-fonts }, size: 1.02em)
      #if it.numbering != none {
        text(weight: "medium", fill: rgb("#a06050"))[#counter(heading).display(it.numbering)#h(0.5em)]
      }
      #text(style: "italic", weight: "medium", it.body)
    ]
    v(0.5em)
  }

  // ── Nivel 4: Párrafo con título ──
  show heading.where(level: 4): it => {
    v(0.9em)
    text(font: main-fonts, style: "italic", weight: "bold", it.body)
    h(0.5em)
  }

  body
}
