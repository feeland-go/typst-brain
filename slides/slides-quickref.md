---
typst_min_version: "0.13.0"
typst_max_version: "0.14.x"
updated_at: "2026-03-07"
token_count: 0
see_also: [packages/touying.md, packages/polylux.md]
---

# Slides Quick Reference

## Option 1: Touying (Recommended — full-featured)
```typst
#import "@preview/touying:0.6.1": *
#import themes.university: *

#show: university-theme.with(
  aspect-ratio: "16-9",
  config-info(title: [Title], author: [Author], date: datetime.today(), institution: [Inst]),
)
#title-slide()

= Section Title
== Slide Title
Content here. #pause More after pause.
```
Themes: simple, university, metropolis, dewdrop, aqua.

## Option 2: Polylux (Minimalist)
```typst
#import "@preview/polylux:0.4.0": *
#set page(paper: "presentation-16-9")
#set text(size: 25pt)

#slide[= Title Slide
Author — Date]

#slide[== Slide 1
Content. #uncover(2)[Appears later.]]
```

## Option 3: Native Typst (Emergency Fallback)
```typst
#set page(paper: "presentation-16-9", margin: 2cm)
#set text(size: 20pt)

// Slide 1
#align(horizon + center)[= Title
_Subtitle_]
#pagebreak()

// Slide 2
= Heading
Content
```
