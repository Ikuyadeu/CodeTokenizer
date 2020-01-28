package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"go/scanner"
	"go/token"
	"os"
)

type Position struct {
	Line   int
	Column int
}

type Token struct {
	Position Position
	Category string
	Str      string
}

type Human struct {
	Name string
	Age  int
}

func main() {
	// Initialize the scanner.
	var s scanner.Scanner

	stdin := bufio.NewScanner(os.Stdin)
	stdin.Scan()

	var tokens []Token
	text := stdin.Text()
	fset := token.NewFileSet()                       // positions are relative to fset
	file := fset.AddFile("", fset.Base(), len(text)) // register input "file"
	s.Init(file, []byte(text), nil /* no error handler */, scanner.ScanComments)

	// Repeated calls to Scan yield the token sequence found in the input.
	for {
		pos, tok, lit := s.Scan()
		if tok == token.EOF {
			break
		}
		position := fset.Position(pos)
		tokenPosition := Position{
			Line:   position.Line,
			Column: position.Column}

		str := lit
		category := tok.String()
		if str == "" {
			str = category
		}
		currentToken := Token{
			Position: tokenPosition,
			Category: category,
			Str:      str,
		}

		tokens = append(tokens, currentToken)
	}
	a, _ := json.Marshal(tokens)
	string := string(a)
	fmt.Println(string)

}
