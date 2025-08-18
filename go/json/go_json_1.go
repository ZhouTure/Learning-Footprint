package main

import (
	"encoding/json"
	"fmt"
)

type response1 struct {
	Page   int
	Fruits []string
}

func main() {

	var data_1 []string
	slcD := []string{"apple", "peach", "pear"}
	slcB, _ := json.Marshal(slcD)
	fmt.Println(string(slcB))
	err := json.Unmarshal(slcB, &data_1)
	if err != nil{
		panic(err)
	}
	fmt.Println("slices_after:", data_1[2])

	var data_2 map[string]interface{}
	mapD := map[string]int{"apple": 5, "lettuce": 7}
	mapB, _ := json.Marshal(mapD)
	fmt.Println(string(mapB))
	err = json.Unmarshal(mapB, &data_2)
	if err != nil{
		panic(err)
	}
	fmt.Println("map_after:", data_2["apple"])

	res1D := &response1{
		Page:   1,
		Fruits: []string{"apple", "peach", "pear"}}
	res1B, _ := json.Marshal(res1D)
	fmt.Println(string(res1B))

	var data map[string]interface{}
	err = json.Unmarshal(res1B, &data)
	if err != nil{
		panic(err)
	}
	fmt.Println("UnMarshal:",data["Page"])
}
