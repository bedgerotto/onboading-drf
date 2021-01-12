# set base image (host OS)
FROM python:3.9

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# set the working directory in the container
WORKDIR /code

# command to run on container start
CMD [ "bash" ]
