package store

import (
	"sync"

	"github.com/pkg/errors"
)

type Store interface {
	Get(id string) (string, error)
	Put(id string, value string) error
}

type MemoryStore struct {
	mu    sync.RWMutex
	items map[string]string
}

func NewMemoryStore() *MemoryStore {
	return &MemoryStore{items: make(map[string]string)}
}

func (s *MemoryStore) Get(id string) (string, error) {
	s.mu.RLock()
	defer s.mu.RUnlock()
	v, ok := s.items[id]
	if !ok {
		return "", errors.New("not found: " + id)
	}
	return v, nil
}

func (s *MemoryStore) Put(id string, value string) error {
	if id == "" {
		return errors.New("empty id")
	}
	s.mu.Lock()
	defer s.mu.Unlock()
	s.items[id] = value
	return nil
}
