FROM python:3.10.5-alpine3.16

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 80

CMD ["python","./Practica_2_SDN.py" ]
