###############################################################
# Dockerfile for creating Image with Paython and my-script.py #
###############################################################
FROM python:3
WORKDIR /app
VOLUME /app
COPY my-app.py .
CMD exec /bin/bash -c "python ./my-app.py; trap : TERM INT; sleep infinity & wait"