// =============================================================================
// icons.typ  —  Iconos vectoriales educativos nativos para Typst
// =============================================================================
//
// PROPÓSITO:
//   Iconos vectoriales dibujados puramente con primitivas geométricas de Typst
//   (circle, rect, polygon, line, ellipse). No dependen de ninguna fuente
//   externa ni de FontAwesome, garantizando 100% de portabilidad y renderizado
//   nítido a cualquier resolución.
//
// ICONOS DISPONIBLES:
//   • icon-book()        → Libro abierto (conocimiento / lectura)
//   • icon-mortarboard() → Birrete académico (educación / graduación)
//   • icon-science()     → Modelo atómico con orbitales (ciencias / física / química)
//   • icon-compass()     → Compás de dibujo técnico y geometría
//   • icon-leaf()        → Hoja botánica (ciencias naturales / biología)
//   • icon-flask()       → Matraz Erlenmeyer de laboratorio (experimentación)
// =============================================================================

/// Libro abierto con páginas y lomo central
#let icon-book(size: 20pt, stroke-color: luma(180), fill-color: none) = {
  box(width: size, height: size * 0.75)[
    // Página izquierda
    #place(top + left, polygon(
      fill: if fill-color != none { fill-color } else { stroke-color.lighten(85%) },
      stroke: 0.5pt + stroke-color,
      (4%, 22%), (48%, 10%), (48%, 86%), (4%, 98%),
    ))
    // Página derecha
    #place(top + left, polygon(
      fill: if fill-color != none { fill-color } else { stroke-color.lighten(85%) },
      stroke: 0.5pt + stroke-color,
      (52%, 10%), (96%, 22%), (96%, 98%), (52%, 86%),
    ))
    // Lomo central
    #place(top + left, line(start: (50%, 10%), end: (50%, 88%), stroke: 0.75pt + stroke-color))
  ]
}

/// Birrete académico de graduación con borla
#let icon-mortarboard(size: 20pt, stroke-color: luma(180), fill-color: none) = {
  box(width: size, height: size * 0.75)[
    // Cubierta en rombo
    #place(top + left, polygon(
      fill: if fill-color != none { fill-color } else { stroke-color.lighten(85%) },
      stroke: 0.5pt + stroke-color,
      (50%, 5%), (95%, 38%), (50%, 72%), (5%, 38%),
    ))
    // Base del casquete
    #place(top + left, polygon(
      fill: if fill-color != none { fill-color } else { stroke-color.lighten(75%) },
      stroke: 0.5pt + stroke-color,
      (26%, 50%), (26%, 80%), (74%, 80%), (74%, 50%),
    ))
    // Hilo de la borla y borla
    #place(top + left, line(start: (50%, 38%), end: (92%, 60%), stroke: 0.5pt + stroke-color))
    #place(top + left, circle(radius: 1.5pt, fill: stroke-color), dx: 92% - 1.5pt, dy: 60% - 1.5pt)
  ]
}

/// Átomo con núcleo y tres anillos orbitales de probabilidad
#let icon-science(size: 20pt, stroke-color: luma(180)) = {
  box(width: size, height: size)[
    #place(center + horizon, circle(radius: size * 0.11, fill: stroke-color))
    #place(center + horizon, rotate(30deg, ellipse(width: size * 0.88, height: size * 0.32, stroke: 0.45pt + stroke-color)))
    #place(center + horizon, rotate(-30deg, ellipse(width: size * 0.88, height: size * 0.32, stroke: 0.45pt + stroke-color)))
    #place(center + horizon, rotate(90deg, ellipse(width: size * 0.88, height: size * 0.32, stroke: 0.45pt + stroke-color)))
  ]
}

/// Compás de dibujo técnico y matemáticas
#let icon-compass(size: 20pt, stroke-color: luma(180)) = {
  box(width: size, height: size)[
    #place(top + left, circle(radius: 1.6pt, fill: stroke-color), dx: 50% - 1.6pt, dy: 5% - 1.6pt)
    #place(top + left, line(start: (50%, 5%), end: (20%, 95%), stroke: 0.55pt + stroke-color))
    #place(top + left, line(start: (50%, 5%), end: (80%, 95%), stroke: 0.55pt + stroke-color))
    #place(top + left, line(start: (32%, 55%), end: (68%, 55%), stroke: 0.45pt + stroke-color))
  ]
}

/// Hoja botánica de biología y ciencias de la naturaleza
#let icon-leaf(size: 20pt, stroke-color: luma(180), fill-color: none) = {
  box(width: size, height: size)[
    #place(top + left, polygon(
      fill: if fill-color != none { fill-color } else { stroke-color.lighten(88%) },
      stroke: 0.5pt + stroke-color,
      (50%, 5%), (85%, 35%), (75%, 75%), (50%, 95%), (25%, 75%), (15%, 35%),
    ))
    #place(top + left, line(start: (50%, 5%), end: (50%, 95%), stroke: 0.5pt + stroke-color))
    #place(top + left, line(start: (50%, 38%), end: (72%, 28%), stroke: 0.35pt + stroke-color))
    #place(top + left, line(start: (50%, 55%), end: (28%, 45%), stroke: 0.35pt + stroke-color))
    #place(top + left, line(start: (50%, 70%), end: (68%, 62%), stroke: 0.35pt + stroke-color))
  ]
}

/// Matraz Erlenmeyer de química y laboratorio
#let icon-flask(size: 20pt, stroke-color: luma(180), fill-color: none) = {
  box(width: size, height: size)[
    // Cuello del matraz
    #place(top + left, rect(width: size * 0.26, height: size * 0.34, stroke: 0.5pt + stroke-color, radius: 0.5pt), dx: size * 0.37, dy: 2pt)
    // Cuerpo cónico
    #place(top + left, polygon(
      fill: if fill-color != none { fill-color } else { stroke-color.lighten(88%) },
      stroke: 0.5pt + stroke-color,
      (37%, 34%), (63%, 34%), (90%, 92%), (10%, 92%),
    ))
    // Menisco de líquido
    #place(top + left, line(start: (22%, 70%), end: (78%, 70%), stroke: 0.4pt + stroke-color))
  ]
}
