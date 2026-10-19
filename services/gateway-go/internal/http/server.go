package httpapi

import (
	"encoding/json"
	"net/http"

	"github.com/acme/shop/gateway/internal/store"
)

type Server struct {
	store  store.Store
	router *http.ServeMux
}

func NewServer(s store.Store) *Server {
	srv := &Server{store: s, router: http.NewServeMux()}
	srv.routes()
	return srv
}

func (s *Server) routes() {
	s.router.Handle("/items/", Chain(http.HandlerFunc(s.handleGet), Logging, RequireJSON))
	s.router.HandleFunc("/healthz", s.handleHealth)
}

func (s *Server) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	s.router.ServeHTTP(w, r)
}

func (s *Server) handleGet(w http.ResponseWriter, r *http.Request) {
	id := r.URL.Path[len("/items/"):]
	value, err := s.store.Get(id)
	if err != nil {
		writeError(w, http.StatusNotFound, err)
		return
	}
	writeJSON(w, http.StatusOK, map[string]string{"id": id, "value": value})
}

func (s *Server) handleHealth(w http.ResponseWriter, r *http.Request) {
	writeJSON(w, http.StatusOK, map[string]string{"status": "ok"})
}

func writeJSON(w http.ResponseWriter, status int, body any) {
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(status)
	_ = json.NewEncoder(w).Encode(body)
}

func writeError(w http.ResponseWriter, status int, err error) {
	writeJSON(w, status, map[string]string{"error": err.Error()})
}
