FROM python:3.9.16-slim-bullseye

COPY pip-requirements.txt pip-requirements.txt

RUN pip install -r pip-requirements.txt
