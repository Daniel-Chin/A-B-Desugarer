# A=B Desugarer
## It unrolls the wildcard '?'
Any line containing any '?' is duplicated to three lines. Each line replaces all '?' to 'a', 'b', and 'c' respectively.  

e.g.  
```
?|=|?
```
is unrolled to  
```
a|=|a
b|=|b
c|=|c
```

## Escape char: '\'
- `\?` is replaced with `?`.  
- `\\` is replaced with `\`.  
- Other `\`-prefixed strings are invalid.
