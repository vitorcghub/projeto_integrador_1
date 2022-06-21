# Start from the official Python base image.
FROM python:3.9 as base

# Environment variables to configure Flask
ENV API_DIR="/app"

# Work directory inside container
WORKDIR ${API_DIR}

# Copy the file with the requirements to the /code directory.
COPY ./requirements.txt ${API_DIR}/requirements.txt

# Install requirements
RUN pip install --no-cache-dir --upgrade -r ${API_DIR}/requirements.txt

############START NEW IMAGE: PRODUCTION ###################
FROM base as prod
COPY ./app ${API_DIR}
