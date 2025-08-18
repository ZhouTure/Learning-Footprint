package main

import "fmt"


func main() {
	vals := func (a, b int) (int, int){
		return a + b, a * b 
	}
	a, b := vals(1, 2)

	fmt.Println(a, b)
}