# ShopGenius AI

A multi-agent system to deliver hyper-personalized product recommendations in e-commerce using GenAI and SQLite.

## Features
- Multi-agent architecture: Customer, Product, Recommender, Feedback, DB
- Uses SQLite for persistent long-term memory
- Embedding-based recommendation architecture (pluggable with Ollama)

## Structure
- agents/: All intelligent components
- data/: Preloaded SQLite DB (schema must be created)
- utils/: Data preprocessing utilities

## Getting Started
1. Make sure Python and required packages are installed.
2. Place your ecomm_dataset.sqlite file in the `data/` folder.
3. Run the system using:
```bash
python main.py
```

## Demo
Run `demo.py` to simulate interactions.

---
This project is built for the Hack the Future: Gen AI Sprint.
