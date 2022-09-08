setup: ## Install dependencies
	python3 -m venv venv
	./venv/bin/python -m pip install --upgrade pip
	./venv/bin/python -m pip install -r requirements.txt

run_sd:
	conda activate stable-diffusion-main/ldm
	python activate stable-diffusion-main/scripts/txt2img.py --prompt "a photograph of an astronaut riding a horse" --plms
	conda deactivate


run: ## Run the app with no reload
	./venv/bin/wave run --no-reload src.app

dev: ## Run the app with active reload
	H2O_WAVE_NO_LOG=True ./venv/bin/wave run src.app

help: ## List all make tasks
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
