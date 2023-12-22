FROM python:3.10

# # Configure Poetry
# ENV POETRY_VERSION=1.7.1
# ENV POETRY_HOME=/opt/poetry
# ENV POETRY_VENV=/opt/poetry-venv
# ENV POETRY_CACHE_DIR=/opt/.cache

# # Install poetry separated from system interpreter
# RUN python3 -m venv $POETRY_VENV \
#     && $POETRY_VENV/bin/pip install -U pip setuptools \
#     && $POETRY_VENV/bin/pip install poetry==${POETRY_VERSION}

# # Add `poetry` to PATH
# ENV PATH="${PATH}:${POETRY_VENV}/bin"
# ENV PATH="${PATH}:/root/.local/bin"

WORKDIR /app

# Install dependencies
COPY poetry.lock pyproject.toml ./

# RUN poetry install
RUN pip install poetry && poetry config virtualenvs.create false && poetry install

# Run your app
COPY vqa_e2e/ .

RUN ls -al

EXPOSE 8501 8000

# CMD [ "streamlit", "run", "client.py", "--server.port=8501", "--server.address=0.0.0.0", "&", "uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"  ]
# CMD [ "streamlit", "run", "client.py", "--server.port=8501", "--server.address=0.0.0.0" ]
# CMD [ "uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000" ]
# CMD ["streamlit", "run", "client.py", "&", "uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
CMD ["./start_services.sh"]