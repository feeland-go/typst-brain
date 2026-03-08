# Speaker Notes

Touying supported speaker notes that can be displayed on a second screen (e.g., using Pympress).

```typst
== Slide with Note
Slide content here.

#speaker-note[
  + This is a speaker note.
  + You won't see it unless you use `config-common(show-notes-on-second-screen: right)`
]
```
