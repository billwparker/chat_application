
# Create conda environment, we'll call it chat
conda create -n chat python=3.11

# Install dependencies
pip install openai
pip install streamlit

# Download Ollama
(Ollama only works on Mac for Linux right now. For Windows you could use LMStudio)
https://ollama.com/

# Choose and run local model using Ollama

## This command will download the mistral model for ollama to use
ollama pull mistral

## This command will run mistral at http://localhost:11434/v1
ollama run mistral

# Streamlit app
Build Streamlit python file. We'll call it app.py.

## This command will run Streamlit app
streamlit run app.py
