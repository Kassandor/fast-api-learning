.DEFAULT_GOAL := help

PORT = 8000
HOST = localhost

run: ## Run app
	uvicorn main:app -h ${HOST} -p ${PORT}

help: ## Help message
	@echo "Usage: make [command]"
	@echo ""
	@echo "Commands:"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "%-10s %s\n", $$1, $$2}' $(MAKEFILE_LIST)
