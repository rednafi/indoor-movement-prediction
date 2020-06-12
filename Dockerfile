FROM python:3.8.3

WORKDIR /app

COPY ./requirements.txt /app/

RUN pip install -r requirements.txt

COPY ./ /app


EXPOSE 8888

CMD ["sh", "-c", "jupyter notebook --ip=0.0.0.0 --allow-root"]
