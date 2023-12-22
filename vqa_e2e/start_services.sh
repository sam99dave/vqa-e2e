#!/bin/bash

# Start Streamlit
streamlit run client.py --server.address=0.0.0.0 --server.port 8501 &

# Start Uvicorn (FastAPI)
uvicorn server:app --host 0.0.0.0 --port 8000
