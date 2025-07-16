# Calculus Romanus

## Interactive Demo

[Calculus Romanus](https://max1vol.github.io/calculus-romanus/)

## Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1W_tQP46Nd50Zv0cDFZQMZe9bMmbhkfdH?usp=sharing)

## Rules

1. All numbers written using Roman numerals
2. All variables should be names of Roman Emperors (fixed list of 10 names)
3. the "print" command is called "Scribo"

4. No arithmetic symbols, only Roman words, no division (not invented yet):

```
I addit II  # 1 + 2
V minuit II # 5-2
III multiplicat IV  # 3*4
```

5. error handling: no negative numbers or zero (Romans didn't invent that), so whole program crashes if encountered (fun part)

6. functions

Function definitions: functio, finio; reddo -- return:

```
functio Summa(a, b)
  reddo a addit b
finio
```

Function calls

```
Scribo Summa(V, III)
```

7. Conditions: if == si, else -- aliter

```
si Augustus maior quam X ergo
    Scribo "Augustus est dives"
aliter
    Scribo "Augustus non est dives"
```

8. Comparisons

| English      | Calculus Romanus |
| ------------ | ---------------- |
| Equals       | aequus           |
| Not Equals   | non aequus       |
| Greater than | maior quam       |
| Less than    | minor quam       |

9. Quircks

a. No operator prescedence, no brackets
b. 0 (zero) and negative numbers are not invented yet, so the program crashes if encounters those!

## Examples

### Tax Calculation

```
Augustus est X
Tributum est V
Taxatio est Augustus multiplicat Tributum
Scribo Taxatio
```
