package main

import (
	"fmt"
	"slices"
	"maps"
)

func main() {
	// s := []string{"a", "b", "c"}
	s := make([]string, 3)
	s[0] = "a"
	s[1] = "b"
	s[2] = "c"
	a := make([]string, 3)
	copy(a, s)

	b := map[string]int{"foo" : 1, "bar" : 2}
	c := map[string]int{"foo" : 1, "bar" : 2}

	if slices.Equal(a, s) {
		fmt.Println("a == s!")
	}

	if maps.Equal(c, b){
		fmt.Println("c == b!")
	}

	fmt.Println(a, s)
	fmt.Println(b, c)
}