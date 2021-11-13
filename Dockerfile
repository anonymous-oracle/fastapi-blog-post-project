FROM python:3.9.7

WORKDIR /usr/src/app

COPY requirements.txt ./

COPY alembic.sh alembic.sh

COPY app.sh app.sh

COPY container_commands.sh container_commands.sh

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt -U

COPY . .
EXPOSE 8000

CMD [ "bash", "container_commands.sh" ]