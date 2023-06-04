package main

import (
	"io/ioutil"

	"github.com/gregjones/httpcache"
	"github.com/gregjones/httpcache/diskcache"
)

func main() {
	diskcache.New("./cache")
	storage := diskcache.New("./cache")
	cache := httpcache.NewTransport(storage)

	cache.MarkCachedResponses = true
	cachedClient := cache.Client()
	println("Caching:http://www.example.com/index.html")
	resp, err := cachedClient.Get("http://www.example.com/index.html")
	if err != nil {
		panic(err)
	}

	ioutil.ReadAll(resp.Body)
	resp.Body.Close()
	println("Requesting:http://www.example.com/index.html")
	resp, err = cachedClient.Get("http://www.ecample.com/index.html")
	if err != nil {
		panic(err)
	}

	_, ok := resp.Header["X-From-Cache"]
	if ok {
		println("Result was pulled from the cache!")
	}
}
