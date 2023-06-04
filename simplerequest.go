package main

import (
	"log"
	"net/http"
	"os"
)

func main() {
	var r *http.Response
	var err error

	r, err = http.Get("http://www.example.com/index.html")

	if err != nil {
		panic(err)
	}

	if r.StatusCode == 200 {
		var webPageContent []byte
		var bodyLength int = 1270

		webPageContent = make([]byte, bodyLength)

		var out *os.File
		out, err = os.OpenFile("index.html", os.O_CREATE|os.O_WRONLY, 0664)

		if err != nil {
			panic(err)
		}

		out.Write(webPageContent)
		out.Close()
	} else {
		log.Fatal("Failed", r.Status)
	}
}
