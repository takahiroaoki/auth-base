FROM amazonlinux:2.0.20230504.1

# install basic tools
RUN yum -y update && yum install -y \
    systemd \
    shadow-utils \
    tar \
    unzip \
    sudo

# install python
RUN yum install -y python3-3.7.16

# install poetry
RUN pip3 install poetry

# add user
## shadow-utils contains "useradd"
ARG USER_NAME=dev-user
RUN useradd -m $USER_NAME && echo "${USER_NAME} ALL=NOPASSWD: ALL" >> /etc/sudoers
USER $USER_NAME

# install libraries
WORKDIR /app
COPY ./app/pyproject.toml* ./app/poetry.lock* /app/
RUN poetry install

ENTRYPOINT ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--reload"]