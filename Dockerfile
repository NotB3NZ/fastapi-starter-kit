FROM python:3.12.5-slim-bookworm

ENV PYTHONUNBUFFERED=1 \
  TZ="Asia/Dhaka" \
  UV_VERSION=0.4.3

# System deps:
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates tzdata && \
    ln -fs /usr/share/zoneinfo/Asia/Dhaka /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata

# Download the latest installer
ADD https://astral.sh/uv/$UV_VERSION/install.sh /uv-installer.sh
# Run the installer then remove it
RUN sh /uv-installer.sh && rm /uv-installer.sh
# Ensure the installed binary is on the `PATH`
ENV PATH="/root/.cargo/bin/:$PATH"

# Copy only requirements to cache them in docker layer
WORKDIR /code
# Copy the lockfile and `pyproject.toml` into the image
ADD uv.lock /code/uv.lock
ADD pyproject.toml /code/pyproject.toml
# Install dependencies
RUN uv sync --frozen --no-install-project
# Copy the project into the image
ADD . /code
# Sync the project
RUN uv sync --frozen
