package httpapi

import (
	"net/http"
	"net/http/httptest"
	"testing"

	"github.com/acme/shop/gateway/internal/store"
)

func TestGetReturnsStoredItem(t *testing.T) {
	s := store.NewMemoryStore()
	if err := s.Put("sku-1", "widget"); err != nil {
		t.Fatal(err)
	}
	srv := NewServer(s)
	rec := httptest.NewRecorder()
	srv.ServeHTTP(rec, httptest.NewRequest(http.MethodGet, "/items/sku-1", nil))
	if rec.Code != http.StatusOK {
		t.Fatalf("status = %d, want 200", rec.Code)
	}
}

func TestMissingItemIs404(t *testing.T) {
	srv := NewServer(store.NewMemoryStore())
	rec := httptest.NewRecorder()
	srv.ServeHTTP(rec, httptest.NewRequest(http.MethodGet, "/items/nope", nil))
	if rec.Code != http.StatusNotFound {
		t.Fatalf("status = %d, want 404", rec.Code)
	}
}
