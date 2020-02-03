# Source Code Tokenizer by Using PyAntlr

Tokenize Multi Language Code

## Usage

1. Get antlr4-python3-runtime and this repository

```sh
pip3 install antlr4-python3-runtime
git clone https://github.com/Ikuyadeu/CodeTokenizer.git
```


2. Make python code that call tokenizer

```py
from tokenizer import TokeNizer

TN = TokeNizer("Python")

code = "if a.isEmpty():"
print(TN.getPureTokens(code))
```

## Supported Languages

* Python(Python)
* Java(Java)
* JavaScript/TypeScript(JavaScript)
* C/C++(CPP)
* Ruby(Ruby)
* Go(Go)
* R(R)
* PHP(PHP)
* Dart(Dart)


## Thanks

This code is made by using antlr and [Anoyomouse/Antlr4-Grammar-JavaScript-Py](https://github.com/Anoyomouse/Antlr4-Grammar-JavaScript-Py)
