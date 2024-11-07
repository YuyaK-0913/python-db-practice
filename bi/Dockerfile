FROM python:3.10.6-slim

COPY requirements.txt requirements.txt

RUN apt-get -y update && \
    apt-get -y install \
    apt-utils \
    gcc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --no-cache-dir -r requirements.txt

COPY src /src

WORKDIR /src

CMD ["/bin/bash", "-c", "while true; do sleep 1; done"]
# CMD [ "streamlit", "run", "src/main.py" ]