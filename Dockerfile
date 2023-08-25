FROM python

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

