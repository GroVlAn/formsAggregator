FROM python:3.11.5-alpine

RUN cd ..

WORKDIR /app

COPY . .

RUN python3 -m venv .venv
RUN . ./venv/bin/activate
RUN pip install -r requirements.txt

CMD ["python3", "main.py", "run", "--prod"]

EXPOSE 4040