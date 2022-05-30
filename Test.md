### Definitionen 
```ad-definition
title: Definition Komplexitätsklasse TIME
 
Sei $t: \mathbb{N} \rightarrow \mathbb{N}$. Die Komplexitätsklasse **TIME** besteht aus allen __Sprachen__ A, für die es eine Mehrband-[Turingmaschine](((MUEDE77ga))) gibt, die A [entscheidet](((3JG-Oo8mQ))) und in [Zeit](((yHuuAgvpM)))$ O(s$) arbeitet.
```
```ad-definition
title: Definition Komplexitätsklasse SPACE
 
Sei $t: \mathbb{N} \rightarrow \mathbb{N}$. Die Komplexitätsklasse **SPACE** besteht aus allen __Sprachen__ A, für die es eine Mehrband-[Turingmaschine](((MUEDE77ga))) gibt, die A [entscheidet](((3JG-Oo8mQ))) und in [Platz](((AzAPjA98H)))$ O(s$) arbeitet.
```
```ad-definition
title: Definition Komplexitätsklasse P
 
$P = \bigcup_{k\in \mathbb{N}}\text{TIME}(n^k)=\text{TIME}(n^{O(1)})$ mit [TIME](((vb5kXY6cz)))

Die Komplexitätsklasse ist die Klasse der __effizient lösbaren__ Probleme. 
```
```ad-definition
title: Definition Komplexitätsklasse NTIME

Sei $t: \mathbb{N} \rightarrow \mathbb{N}$. Die Komplexitätsklasse **TIME** besteht aus allen __Sprachen__ A, für die es eine Mehrband-[NTM](((MUEDE77ga))) gibt, die A [entscheidet](((3JG-Oo8mQ))) und in [Zeit](((yHuuAgvpM)))$ O(s$) arbeitet.
```
```ad-definition
title: Definition Komplexitätsklasse NSPACE

Sei $t: \mathbb{N} \rightarrow \mathbb{N}$. Die Komplexitätsklasse **TIME** besteht aus allen __Sprachen__ A, für die es eine Mehrband-[NTM](((MUEDE77ga))) gibt, die A [entscheidet](((3JG-Oo8mQ))) und in [Platz](((AzAPjA98H)))$ O(s$) arbeitet.
```
```ad-definition
title: Definition Komplexitätsklasse NP

$NP = \bigcup_{k\in \mathbb{N}}\text{NTIME}(n^k)=\text{NTIME}(n^{O(1)})$ mit [NTIME](((aECM1ttL4)))

Die Komplexitätsklasse ist die Klasse der __effizient überprüfbaren__ Probleme. 

Siehe auch [[NP-Problem]].
```
```ad-definition
title: Definition Komplexitätsklasse EXP
 
$\text{EXP} = \text{TIME}(2^{n^{O(1)}})$
```
```ad-definition
title: Definition Komplexitätsklasse PSPACE
 
$\text{PSPACE} = \text{SPACE}(n^{O(1)})$
```
```ad-definition
title: Definition Komplexitätsklasse NL
 
$\text{NL} = \text{NSPACE}(log(n))$
```
```ad-definition
title: Definition Komplexitätsklasse L
 
$\text{L} = \text{SPACE}(log(n))$
```
```ad-definition
title: Definition Raumkonstruierbarkeit
 Sei $f: \mathbb{N} \rightarrow \mathbb{N}$ eine Funktion. Wir nennen $f$ **raumkonstruierbar**, fall es eine [deterministische Einband-Turingmaschine](((MUEDE77ga))) gibt, die bei Eingabe eines Wortes $x$ einen Speicherbedarf von __genau__ $f(|x|)$ hat. 
```
### Zusammenhänge untereinander 
- Zusammenhang [SPACE](((Au0v8kV8D)))-[NSPACE](((cWT4RCXVz))), [TIME](((vb5kXY6cz)))-[NTIME](((aECM1ttL4))): 
$\text{SPACE}(s(n)) \subseteq \text{NSPACE}(s(n))$ und $\text{TIME}(t(n)) \subseteq \text{NTIME}(t(n))$
- Zusammenhang [NTIME](((aECM1ttL4))) in [TIME](((vb5kXY6cz))): 
Sei $t(n) \geq n$ eine Funktion. Dann gilt $\text{NTIME}(t(n)) \subseteq \text{TIME}(2^{O(t(n))})$
- Zusammenhang [NTIME](((aECM1ttL4))), [TIME](((vb5kXY6cz))) und [SPACE](((Au0v8kV8D)))
Sei $t(n) \geq n$ eine Funktion. Dann gilt: $\text{TIME}(t(n)) \subseteq \text{NTIME}(t(n)) \subseteq \text{SPACE}(t(n))$
- Zusammenhang [SPACE](((Au0v8kV8D))) in [TIME](((vb5kXY6cz)))
Sei $s(n) \geq log(n)$ eine Funktion. Dann gilt $\text{SPACE}(s(n)) \subseteq \text{TIME}(2^{O(s(n))})$
- Zusammenhang [NSPACE](((cWT4RCXVz))) und [TIME](((vb5kXY6cz)))
Sei $s(n) \geq log(n)$ [raumkonstruierbar](((7zTwvPY7U))). Dann gilt: $\text{NSPACE}(s(n)) \subseteq \text{TIME}(2^{O(s(n))})$
- Zusammenhang [NSPACE](((cWT4RCXVz))) [SPACE](((Au0v8kV8D))) (**Satz von Savitch**)
Sei $s(n)\geq log(n)$ [raumkonstruierbar](((7zTwvPY7U))). Dann gilt: $\text{NSPACE}(s(n))\subseteq \text{SPACE}((s(n))^2)$
```ad-satz
title:Platzhierarchiesatz
 Sei $s_1 \in o(s_2)$ und $s_2$ [raumkonstruierbar](((7zTwvPY7U))). Dann gilt: $\text{SPACE}(s_1) \subsetneq \text{SPACE}(s_2)$
```
```ad-satz
title:Zeithierarchiesatz
 Sei $t_1(n) \in o(\frac{t_2(n)}{log(t_2(n))})$, $t_2$ "zeitkonstruierbar". Dann ist $\text{TIME}(t_1) \subsetneq \text{TIME}(t_2)$
```
### Zusammenhang zu [[Turingmaschine]]n
- Zusammenhang [(N)-TIME](((aECM1ttL4))) und [1-Band TM](((MUEDE77ga)))
Sei $t(n) \geq n$ eine Funktion. Jede Mehrband Turingmaschine M, die [in Zeit t](((8XuGd8md6))) arbeitet, kann von einer 1-Band Turingmaschine M' simuliert werden, die in Zeit $O(t^2)$ arbeitet
- Zusammenhang [(N)-TIME](((aECM1ttL4))) und [2-Band TM](((MUEDE77ga)))
Sei $t(n) \geq n$ eine Funktion. Jede Mehrband Turingmaschine M, die [in Zeit t](((8XuGd8md6))) arbeitet, kann von einer 2-Band Turingmaschine M' simuliert werden, die in Zeit $O(log(t) \cdot t)$ arbeitet
