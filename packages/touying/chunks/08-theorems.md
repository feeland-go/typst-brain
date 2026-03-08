# Theorems and Proofs

Touying works well with theorem environments. You might need to freeze theorem counters for correct animations.

```typst
#show: university-theme.with(
  config-common(frozen-counters: (theorem-counter,)),
)

== Theorems
#definition[
  A natural number is called a _prime number_...
]

#theorem(title: "Euclid")[
  There are infinitely many primes.
]

#proof[
  Suppose to the contrary...
]
```
