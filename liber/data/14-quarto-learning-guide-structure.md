# Best Practices for Organizing a Quarto Learning Guide

Creating a "Learning Guide" (such as an educational course, textbook, or study guide) using Quarto requires a thoughtful project structure to keep content manageable, logical, and easy to maintain. By leveraging Quarto's "book" project type, you can systematically map a curriculum's syllabus to your file structure and configuration.

## 1. Project Directory Structure

A clean directory structure is essential for an educational guide, which often includes lectures, readings, assignments, and datasets. 

Here is a recommended project structure:

```text
my-learning-guide/
├── _quarto.yml             # Main project configuration file
├── index.qmd               # Course homepage / Syllabus / Preface
├── references.qmd          # Global bibliography page
├── assets/                 # Global assets (images, custom CSS)
│   ├── css/
│   │   └── custom.css
│   └── images/
│       └── logo.png
├── data/                   # Datasets used across the course
│   └── course_dataset.csv
├── module-01-intro/        # Content separated by Week or Module
│   ├── index.qmd           # Main chapter for the module
│   ├── _lesson-1.qmd       # Sub-sections (prefixed with _ to hide from standalone render)
│   ├── _lesson-2.qmd
│   └── images/             # Module-specific images
├── module-02-methods/
│   ├── index.qmd
│   └── _lesson-1.qmd
└── appendices/             # Extra resources (e.g., glossaries, setup guides)
    ├── setup-guide.qmd
    └── glossary.qmd
```

### Key Directory Principles:
- **Modular Folders:** Grouping content by week, module, or topic (e.g., `module-01-intro/`) keeps related assets, sub-pages, and code together.
- **Underscore Prefix (`_`):** Any `.qmd` or `.md` file prefixed with an underscore is ignored by Quarto during the global site render. This is crucial for managing large files using the "include" method (discussed below).

## 2. Configuring `_quarto.yml` for a Syllabus

The `_quarto.yml` file is the backbone of your learning guide. Using the `book` type, you can use `parts`, `chapters`, and `appendices` to map exactly to your syllabus structure. 

```yaml
project:
  type: book

book:
  title: "Data Science 101: A Learning Guide"
  author: "Instructor Name"
  date: "Fall 2026"
  
  chapters:
    - index.qmd                  # Acts as the landing page / Syllabus
    
    - part: "Module 1: Introduction and Setup"
      chapters: 
        - module-01-intro/index.qmd
        
    - part: "Module 2: Core Methods"
      chapters:
        - module-02-methods/index.qmd
        - module-02-methods/advanced-methods.qmd
        
    - references.qmd             # Bibliography
        
  appendices:
    - appendices/setup-guide.qmd # Becomes Appendix A
    - appendices/glossary.qmd    # Becomes Appendix B

format:
  html:
    theme: cosmo
    toc: true
    number-sections: true
  pdf:
    documentclass: scrreprt
    keep-tex: true

execute:
  freeze: auto                   # Prevents re-running unchanged code blocks
```

### Key Configuration Details:
- **`part`**: Use this to define high-level divisions like "Weeks", "Modules", or "Terms". The `chapters` array nested under a part dictates the pages belonging to that section.
- **`appendices`**: Quarto automatically formats these files differently (usually numbering them as A, B, C instead of 1, 2, 3). This is ideal for software installation guides, mathematical notation sheets, or glossaries.
- **`index.qmd`**: Every Quarto book requires an `index.qmd` at the root. In an educational context, this is typically your Preface or the main Course Syllabus.

## 3. Managing Large Files and Course Modules

Educational modules can become massive if you try to put a whole week's worth of lectures, readings, and exercises into a single `.qmd` file. Quarto supports the `{{< include >}}` shortcode to keep files modular.

### Splitting by Lessons
Instead of writing a 2,000-line document for Module 1, split it up:

1. Create partial files with an underscore prefix (so they aren't rendered as standalone chapters):
   - `module-01-intro/_lesson-1-theory.qmd`
   - `module-01-intro/_lesson-2-practice.qmd`

2. In your main `module-01-intro/index.qmd` file, use the include shortcode to stitch them together:

```markdown
# Module 1: Introduction to the Course

Welcome to the first module. Here we will cover the theory and practice of our subject.

{{< include _lesson-1-theory.qmd >}}

{{< include _lesson-2-practice.qmd >}}
```

**Benefits of the Include approach:**
- **Cross-referencing:** Since Quarto stitches them together *before* rendering, internal links, citations, and figure references (`@fig-example`) work seamlessly across the included files.
- **Collaboration:** Multiple teaching assistants or co-authors can work on different lessons simultaneously without triggering merge conflicts in a massive master file.

## 4. Performance Optimization for Educational Content

Courses with heavy computational code (e.g., Python, R, or Julia blocks) can take a long time to render. 
- Always use **`freeze: auto`** (or `freeze: true`) in your `execute` options. 
- This ensures Quarto only re-executes code in documents that have changed, saving substantial rendering time as the course grows over the semester.

## Summary
By mapping your syllabus directly to the `_quarto.yml` via `parts` and `chapters`, dividing weeks/modules into subdirectories, and utilizing the `{{< include >}}` shortcode for long lessons, you create a robust, scalable, and highly maintainable Quarto Learning Guide.
