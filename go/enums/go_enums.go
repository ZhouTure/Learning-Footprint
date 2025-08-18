package main

import "fmt"

// ----------------枚举标准写法----------------------

type ServerState int

const (
	StateIdle ServerState = iota // 0
	ServerConnected // 1
	StateError // 2
	StateRetrying // 3
)

var stateName = map[ServerState]string{
	StateIdle: "idle",
	ServerConnected: "connected",
	StateError: "error",
	StateRetrying: "retrying",
}

func (ss ServerState) String() string {
	return stateName[ss]
}

// -------------------------------

func main() {
	ns := transition(StateIdle)
	fmt.Println(ns)
}

func transition(s ServerState) ServerState  {
	switch s {
	case StateIdle:
		return ServerConnected
	case ServerConnected, StateRetrying:
		return StateIdle
	case StateError:
		return StateError
	default:
		panic(fmt.Errorf("unknown state: %s", s))
	}
}