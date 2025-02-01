FROM python:3.11-alpine
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY . /app
RUN pip install --root-user-action=ignore --no-cache-dir -r requirements.txt
RUN pip install -e .
ARG REST_PORT
ARG GRPT_PORT
ARG AMQP_PORT
ARG MONGO_PORT
ARG EUREKA_PORT
ENV R_PORT=${REST_PORT}
ENV G_PORT=${GRPT_PORT}
ENV A_PORT=${AMQP_PORT}
ENV M_PORT=${MONGO_PORT}
ENV E_PORT=${EUREKA_PORT}
EXPOSE ${G_PORT} ${R_PORT} ${A_PORT}/tcp ${M_PORT} ${E_PORT}
#This line is needed to display print messages

WORKDIR /app/src/amqp_adapter_one
RUN ls -a
#CMD ["sh","./wrapper_script.sh"]
CMD ["python", "./main.py", "--mode=prod"]