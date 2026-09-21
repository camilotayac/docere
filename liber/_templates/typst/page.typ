// =============================================================================
// page.typ  —  Configuración de página y encabezados estilo libro académico
// =============================================================================
//
// PROPÓSITO:
//   Establece la maquetación de página estándar (A4 con márgenes completos de
//   2 cm horizontal × 2.5 cm vertical), garantizando máximo espacio para tablas
//   y contenido didáctico (sin marginalia).
//
// ENCABEZADOS:
//   • Recto (página impar): Título del capítulo en smallcaps ─── Folio
//   • Verso (página par):   Folio ─── Título del capítulo en smallcaps
//   • Suprimido automáticamente en páginas de apertura de capítulo y partes.
// =============================================================================

#set page(
  paper: $if(papersize)$"$papersize$"$else$"a4"$endif$,
$if(margin)$
  margin: ($for(margin/pairs)$$margin.key$: $margin.value$,$endfor$),
$else$
  margin: (x: 2cm, top: 2.5cm, bottom: 2.5cm),
$endif$
  header: context {
    // Verificar si la página actual contiene una apertura de capítulo (nivel 1)
    let is-chapter-page = query(selector(heading.where(level: 1))).any(
      h => h.location().page() == here().page()
    )

    // No mostrar encabezado en página 1 ni en páginas de apertura de capítulo
    if not is-chapter-page and counter(page).get().first() > 1 {
      let chapters = query(selector(heading.where(level: 1)).before(here()))
      if chapters.len() > 0 {
        let title-text = chapters.last().body
        let is-odd = calc.odd(here().page())
        [
          #set text(size: 8.5pt, fill: luma(110))
          #if is-odd [
            #text(tracking: 0.1em, smallcaps(title-text))
            #h(1fr)
            #text(weight: "bold", fill: rgb("#a06050"), counter(page).display())
          ] else [
            #text(weight: "bold", fill: rgb("#a06050"), counter(page).display())
            #h(1fr)
            #text(tracking: 0.1em, smallcaps(title-text))
          ]
          #v(0.3em)
          #line(length: 100%, stroke: 0.35pt + luma(210))
        ]
      }
    }
  },
  footer: none,
)
