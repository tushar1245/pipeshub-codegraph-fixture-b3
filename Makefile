dev:
	docker compose up --build

test:
	cd backend && pytest -q
	cd frontend && npm test
