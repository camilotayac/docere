# Quarto Pedagogical Design for Learning Guides

This report details how to structure a Quarto (`.qmd`) file to serve as an effective chapter or lesson for a Learning Guide, utilizing document-level design elements, callouts, tabsets, and margin content.

## 1. YAML Frontmatter
The YAML frontmatter sets up the fundamental document options for an educational context. It should enable a table of contents (TOC), number sections for easy reference, and set up options to display code effectively.

```yaml
---
title: "Lesson Title"
subtitle: "A short description of the lesson"
author: "Author Name"
date: last-modified
format:
  html:
    toc: true
    toc-depth: 3
    toc-expand: true
    number-sections: true
    code-fold: show
    code-tools: true
    theme: cosmo
---
```

## 2. Learning Objectives & Prerequisites
Start the lesson with clearly defined Learning Objectives and Prerequisites. These can be elegantly framed using Quarto's standard callouts so they stand out from the main text. 

```markdown
:::{.callout-important}
## Learning Objectives
By the end of this lesson, you will be able to:
- Structure a Quarto document for educational purposes.
- Utilize Quarto callouts, tabsets, and margin notes effectively.
:::

:::{.callout-note}
## Prerequisites
Before starting this lesson, you should be familiar with basic Markdown syntax.
:::
```

## 3. Pedagogical Callouts
Quarto includes five standard callouts (`note`, `tip`, `important`, `caution`, `warning`) that are ideal for scaffolding a learner's experience.

- **Note**: General context or "did you know?" info.
- **Tip**: Best practices or efficiency tips.
- **Warning**: Common pitfalls.
- **Caution**: Critical issues that might break code.

*Example:*
```markdown
:::{.callout-warning}
## Common Pitfall
Do not nest complex elements like margin content inside tabsets, as it can cause rendering issues.
:::
```

You can also use collapsible callouts for supplemental details that shouldn't disrupt the reading flow:
```markdown
:::{.callout-tip collapse="true"}
## Expand to see advanced syntax
Here is the advanced syntax for custom CSS styling...
:::
```

## 4. Tabsets for Exercises & Solutions
Tabsets (`.panel-tabset`) are an excellent way to present exercises and their solutions without revealing the answer immediately, or to show code in multiple languages.

```markdown
::: {.panel-tabset}
## Exercise
Write a function in Python that prints "Hello, Quarto!".

## Solution
```python
def greet():
    print("Hello, Quarto!")

greet()
```
:::
```

## 5. Margin Content for Side-Notes
Margin content prevents the main text from becoming cluttered. Use margins for glossaries, side-notes, fun facts, or small reference figures. 

For standard text, wrap it in a `column-margin` div:
```markdown
::: {.column-margin}
**Vocabulary:** *Frontmatter* refers to the YAML block at the top of a document that configures its global settings.
:::
```

Or for simple footnote-like asides without numbers:
```markdown
[This is a small side-note placed in the margin.]{.aside}
```

## 6. Concrete Template

Below is a complete `.qmd` template combining all these elements.

```markdown
---
title: "Chapter X: Introduction to Document Design"
subtitle: "Structuring Pedagogical Content in Quarto"
author: "Instructional Designer"
date: last-modified
format:
  html:
    toc: true
    toc-location: left
    number-sections: true
    theme: flatly
---

:::{.callout-important}
## Learning Objectives
In this chapter, you will learn how to:
- Configure YAML for lessons.
- Use Callouts, Tabsets, and Margin notes.
:::

## Introduction

Welcome to the lesson. Pedagogical design is crucial for keeping learners engaged.[This is an inline aside providing extra context.]{.aside} 

## Main Concept

Quarto provides several tools to structure your content effectively. 

::: {.column-margin}
**Did you know?** 
Quarto supports multiple output formats including HTML, PDF, and MS Word from the same `.qmd` source!
:::

### Best Practices

:::{.callout-tip}
## Pro Tip
Always validate your YAML syntax.
:::

## Practice

::: {.panel-tabset}
## Question
How do you create a collapsible note in Quarto?

## Hint
Look at the `collapse` attribute in callouts.

## Solution
Use `collapse="true"` inside the callout curly braces: `:::{.callout-note collapse="true"}`
:::

## Summary

You have successfully learned how to structure a Quarto lesson!
```
