# 🐕 Verba X Unstructured (demo showcase)

Welcome to Verba: The Golden RAGtriever, an open-source initiative designed to offer a streamlined, user-friendly interface for Retrieval-Augmented Generation (RAG) applications. In this repo, you'll find a step-by-step guide for importing PDFs into Verba by using [Unstructured.io](https://unstructured.io/).

> If you want to learn more about Verba, you can find further details on our [Verba Repo](https://github.com/weaviate/Verba).

# ✨ Quickstart

Here is a quickstart for running this demo workflow. These two API keys are required for running this demo: `OpenAI` and `Unstructured`. 
Please note that using this project will generate costs on your provided API key.

1. **Initialize a new Python Environment**
- ```python3 -m virtualenv venv```

2. **Add Unstructured and OpenAI API key to a `.env` file**
- ```OPENAI_API_KEY=YOUR_KEY```
- ```UNSTRUCTURED_API_KEY=YOUR_KEY```

3. **Source the Python Environment**
- ```source venv/bin/activate```
- ```source .env```

4. **Install requirements**
- ```pip install -r requirements.txt```

5. **(OPTIONAL) Convert PDFs into Text files**
- ```python pdf_to_txt.py```

6. **Import data to Verba**
- ```verba import --path ./data```

7. **Start Verba**
- ```verba start```

## 📦 Dataset

This Repo contains PDFs about taste, smell and their combination. The data folder already contains the converted .txt files, so it's not required to run conversion script.

- Taste and Smell (https://www.researchgate.net/publication/293334369_Taste_and_Smell)
- Combining Tastes (https://www.diva-portal.org/smash/get/diva2:1605983/FULLTEXT01.pdf)

## 💰 Large Language Model (LLM) Costs

Verba exclusively utilizes OpenAI models. Be advised that the usage costs for these models will be billed to the API access key you provide. Primarily, costs are incurred during data embedding and answer generation processes. The default vectorization engine for Verba is `Ada v2`.

## 💖 Open Source Contribution

Your contributions are always welcome! Feel free to contribute ideas, feedback, or create issues and bug reports if you find any! Visit our [Weaviate Community Forum](https://forum.weaviate.io/) if you need any help!