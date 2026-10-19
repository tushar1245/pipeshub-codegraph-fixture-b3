package main

import (
	"log"
	"net/http"
	"os"

	"github.com/acme/shop/gateway/internal/build"
	httpapi "github.com/acme/shop/gateway/internal/http"
	"github.com/acme/shop/gateway/internal/store"
)

func main() {
	addr := envOr("GATEWAY_ADDR", ":8080")
	log.Println(build.Current().String())
	srv := httpapi.NewServer(store.NewMemoryStore())
	log.Fatal(http.ListenAndServe(addr, srv))
}

func envOr(key, fallback string) string {
	if v := os.Getenv(key); v != "" {
		return v
	}
	return fallback
}
