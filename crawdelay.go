package main

import (
	"fmt"
	"net/http"
	"time"
)

func main() {
	var lastRequestTime time.Time
	maximumNumberOfRequests := 5
	pageDelay := 5 * time.Second

	for i := 0; i < maximumNumberOfRequests; i++ {
		elapsedTime := time.Now().Sub(lastRequestTime)
		fmt.Printf("Elapsed Time: %.2f(s)\n", elapsedTime.Seconds())

		if elapsedTime < pageDelay {
			var timeDiff time.Duration = pageDelay - elapsedTime
			fmt.Printf("Sleeping for %.2f(s)\n", timeDiff.Seconds())
			time.Sleep(pageDelay - elapsedTime)
		}

		println("GET example.com/index.html")
		_, err :=
			http.Get("http://www.example.com/index.html")
		if err != nil {
			panic(err)
		}
		lastRequestTime = time.Now()
	}
}
