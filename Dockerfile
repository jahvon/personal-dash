FROM ubuntu:16.04 as base

# Install all Ubuntu dependencies
RUN apt-get update -y && \
  apt-get install -y python3-pip python3-dev postgresql \
  libpq-dev libffi-dev jq

# Set locale settings
ENV LC_ALL=C.UTF-8 \
    LANG=C.UTF-8

# Set environment variables
ENV FLASK_APP=manage.py \
    FLASK_ENV=development \
    APP_SETTINGS=config.DevelopmentConfig \
    SECRET_KEY=secretssecretsarenofun1 \
    DATABASE_URL=postgresql://jahvon:jahvon@db/personaldash

# Copy app to working directory
COPY . /app
WORKDIR /app

# Install Python dependencies from requirements.txt
RUN pip3 install -r requirements.txt

FROM base as development
EXPOSE 5000
CMD ["bash"]