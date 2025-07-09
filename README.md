# Calculus Romanus

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

a. Equals -- aequus etc
b. not Equals -- non aequus
c. Greater than -- maior quam
d. Less than -- minor quam

## Examples

### Tax Calculation

```
Augustus est X
Tributum est V
Taxatio est Augustus multiplicat Tributum
Scribo Taxatio
```
