package main

import (
	"fmt"
	"math"
)

type geomoetry interface {
	area() float64
	perim() float64
}

type rect struct {
	width, height float64
}

type circle struct {
	radius float64
}

func (r rect) area() float64 {
	return r.height * r.width
}

func (r rect) perim() float64 {
	return 2*r.height + 2*r.width
}

func (c circle) area() float64 {
	return c.radius * c.radius * math.Pi
}

func (c circle) perim() float64 {
	return c.radius * 2 * math.Pi
}

func measure(g geomoetry) {
	fmt.Println(g)
	fmt.Println(g.area())
	fmt.Println(g.perim())
}


// 断言写法， ok是bool值 ok == true c为circle ok==false c为 0
func detectCircle(g geomoetry) {
	if c, ok := g.(circle); ok {
		fmt.Println("circle with radius", c.radius)
	} else {
		fmt.Println("That's not a circle")
	}
}

func main() {

	r := rect{width: 4, height: 4}
	c := circle{radius: 5}

	measure(r)
	measure(c)

	detectCircle(r)
	detectCircle(c)

}
