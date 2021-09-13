FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

WORKDIR /api

COPY ./api/requirements.txt .

RUN pip install -r requirements.txt

# copy project
COPY . .

EXPOSE 8000

CMD ["uvicorn", "api.api:app", "--host", "0.0.0.0", "--port", "8000"]

#COPY ./api /api

# ENV INSTALL_PATH /api-credijusto

# RUN mkdir -p $INSTALL_PATH

# COPY ./api $INSTALL_PATH

# WORKDIR $INSTALL_PATH

# COPY requirements.txt requirements.txt

# RUN pip install --no-cache-dir -r requirements.txt

#WORKDIR /api

#EXPOSE 8081

#CMD ["uvicorn", "api:app", "--host", "127.0.0.1", "--port", "8081", "--reload"]

