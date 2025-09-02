default:
    just --list

backend-dev:
    uv run backend/main.py

frontend-dev:
    bun run dev

[parallel]
dev: frontend-dev backend-dev
