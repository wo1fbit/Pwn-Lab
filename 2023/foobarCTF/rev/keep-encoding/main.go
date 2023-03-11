package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	var input string
	fmt.Scanf("%s", &input)
	splitted := strings.Split(input, "|")
	f1(splitted)
	fmt.Print(os.Getenv("FLAG"))
}
