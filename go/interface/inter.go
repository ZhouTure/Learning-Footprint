package main

import "fmt"

type inter interface{
	S() float64
	L() float64
}

type Rect struct {
	len, width float64
}

func (r Rect) S() float64 {
	return r.len*r.width
}

func (r Rect) L() float64 {
	return  (r.len + r.width) * 2
}

func main() {
	fmt.Println("hello, this's a interface modle")
	R := Rect{2, 4}

	fmt.Println("Rect area is ", R.S())
	fmt.Println("Rect len is ",R.L())
}