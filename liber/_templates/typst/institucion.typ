// =============================================================================
// institucion.typ  —  Datos del Proyecto, Institución Educativa y Equipo Docente
// =============================================================================
//
// INSTRUCCIONES PARA FUTURAS ACTUALIZACIONES:
//   A medida que el libro se aplique en diferentes colegios a lo largo del tiempo,
//   puedes modificar la institución activa o añadir nuevas filas en la lista
//   `historico-colaboradores`.
// =============================================================================

#let datos-proyecto = (
  // ── Autoría, Ejecución y Análisis del Proyecto ──
  autor: "Camilo Tayac",
  rol-autor: "Creador, Ejecutor del Proyecto y Analizador Pedagógico-Curricular",
  titulo: "Natura Docens",
  subtitulo: "Guía Didáctica y Plan de Área de Ciencias Naturales (Grados 6° a 11°)",
  coleccion: "Biblioteca de Camilo Tayac de Ciencias Naturales",

  // ── Institución Educativa Vigente ──
  institucion-vigente: (
    nombre: "Institución Educativa Mariscal Sucre",
    rector: "Rectoría Institucional",
    coordinacion: "Coordinación Académica",
    municipio-pais: "Colombia",
    vigencia: "2025 - 2026",
  ),

  // ── Registro Histórico de Colegios, Rectores y Docentes que han Apoyado ──
  // Agrega nuevas entradas a esta lista a medida que el proyecto crezca:
  historico-colaboradores: (
    (
      periodo: "2025 - 2026",
      colegio: "Institución Educativa Mariscal Sucre",
      directivos: "Rectoría Institucional\nCoordinación Académica",
      docentes: "Docentes de Ciencias Naturales\n(Biología, Física y Química)",
      observaciones: "Validación inicial de secuencias didácticas y pruebas Saber 11°.",
    ),
    // Ejemplo para agregar un nuevo colegio en el futuro:
    // (
    //   periodo: "2026 - 2027",
    //   colegio: "Colegio Municipal San Juan",
    //   directivos: "Lic. Nombre Rector (Rector)\nLic. Nombre Coord (Coord. Académica)",
    //   docentes: "Prof. Nombre 1 (Física)\nProf. Nombre 2 (Química)\nProf. Nombre 3 (Biología)",
    //   observaciones: "Implementación en Educación Media (10° y 11°).",
    // ),
  ),

  // ── Marco Legal y Distribución Educativa ──
  legal: (
    derechos: "Todos los derechos del modelo pedagógico y diseño curricular reservados.",
    licencia: "Licencia Creative Commons Atribución-NoComercial 4.0 Internacional (CC BY-NC 4.0).",
    permisos: "Se autoriza su uso, lectura, distribución e impresión con fines pedagógicos y sin fines de lucro comercial.",
  ),
)
