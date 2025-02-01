FROM python:3.10-alpine
WORKDIR /app
COPY . /app
RUN pip install --root-user-action=ignore -r requirements.txt
RUN pip install -e .
ARG REST_PORT
ARG GRPT_PORT
ENV R_PORT=${REST_PORT}
ENV G_PORT=${GRPT_PORT}
EXPOSE ${G_PORT} ${R_PORT}
#This line is needed to display print messages
ENV PYTHONUNBUFFERED=1
CMD ["sh","./wrapper_script.sh"]