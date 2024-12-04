# Define the Streamlit application path
APP_PATH = ./src/app.py

# setup:
# 	curl -o games_may2024_cleaned.csv "https://www.googleapis.com/drive/v3/files/1862luNeJSBquwux74i80Sex4oZCAdX9x?alt=media&key=$VIKI_API_KEY"

# Action to run the Streamlit app, depends on activate
run:
	@echo "Running Streamlit"
	 streamlit run $(APP_PATH)

# Clean action (optional)
clean:
	@echo "Deactivating Conda environment..."
	conda deactivate
