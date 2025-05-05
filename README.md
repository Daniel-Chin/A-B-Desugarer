# A=B Desugarer
A syntactic preprocessor that transforms extended A=B source code into its canonical form. For Artless's puzzle game "[A=B](https://store.steampowered.com/app/1720850/AB/)". 

## ⚠️ Spoiler alert!
The mechanics of this preprocessor may hint some solution styles. I recommend learning and using this preprocessor only after level "4-14 Center 2".  

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

## Usage
Start the python script "main.py". Paste your source code in the extended A=B language. Press Ctrl+D to trigger EoF.  

e.g. on Wayland Linux:  
```fish
python main.py | wl-copy
```

e.g. on Windows:  
```cmd
python main.py | clip
```
