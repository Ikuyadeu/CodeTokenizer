# Source Code Tokenizer by Using PyAntlr

Tokenize Multi Language Code

## Usage

1. Get antlr4-python3-runtime and this repository

```sh
pip install antlr4-python3-runtime
git clone https://github.com/Ikuyadeu/CodeTokenizer.git
```


2. Make python code that call this

```py
from tokenizer import TokeNizer

TN = TokeNizer("Python")

code = "if a.isEmpty():"
print(TN.getPureTokens(code))
```

## Supported Languages

* Python
* Java
* JavaScript
* C++


## Thanks

This code is made by using antlr and [Anoyomouse/Antlr4-Grammar-JavaScript-Py](https://github.com/Anoyomouse/Antlr4-Grammar-JavaScript-Py)
