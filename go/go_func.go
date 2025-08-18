package main

import "fmt"

func plus(a int, b int) int {
	return  a + b	
}

func plusplus(a, b, c int) int {
	return a + b + c
}

func main() {

	plusplusplus := func (a, b, c, d int) int {
		return a + b + c + d
	}
	res := plus(1, 2)
	fmt.Println("1 + 2 =", res)

	res = plusplus(1, 2, 3)
	fmt.Println("1 + 2 + 3 =", res)

	res = plusplusplus(1, 2, 3, 4)
	fmt.Println("1 + 2 + 3 + 4 =",res)
}