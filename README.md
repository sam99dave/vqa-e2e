# vqa-e2e
End to end visual question and answering application

## Docker Commands
Building docker image
`docker build -t vqa-e2e .`

Running docker
`docker run -p 8501:8501 -p 8000:8000 vqa-e2e`

Running docker interactive, **//** is important to turn off GitBash's automatic path conversion
`docker run -it --rm vqa-e2e //bin/bash`

Streamlit App
>> localhost:8501

FastAPI
>> localhost:8000/docs
