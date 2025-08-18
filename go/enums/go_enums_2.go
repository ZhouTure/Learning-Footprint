package main

import "fmt"

type Fruit int

const (
	apple Fruit = iota
	banana
	orange
	bamboo
)

var fruitName = map[Fruit]string{
	apple:  "Delicious",
	banana: "Bad",
	orange: "Juicy",
	bamboo: "unknown",
}

func (fruit Fruit) String() string {
	return fruitName[fruit]
}

func main() {

	fruit := transition1(apple)
	fmt.Println(fruit)

	fruit = transition1(bamboo)
	fmt.Println(fruit)
}

func transition1(fruit Fruit) Fruit {
	switch fruit {
	case apple:
		return apple
	case banana:
		return banana
	case orange:
		return orange
	default:
		panic(fmt.Errorf("unknown fruit: %s", fruit))
		// fmt.Println("Unknown fruit: %s", fruit)
	}
}
