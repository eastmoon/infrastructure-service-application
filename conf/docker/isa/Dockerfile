# Step : base
FROM python:slim

## Update python package manager
RUN pip install --upgrade pip

# Step : Install docker-cli
RUN apt update -y && apt install -y \
    apt-transport-https \
    ca-certificates \
    software-properties-common \
    curl \
    gnupg
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
RUN add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable"
RUN apt update -y && apt install -y \
    docker-ce-cli \
    docker-compose-plugin

# Step : Python FastAPI
## Install FastAPI
RUN pip install \
    fastapi \
    uvicorn[standard]

# Step : Command line interface
## Install python libraries
RUN pip install \
    pyyaml \
    requests

## Install CLI & API
ADD ./cli /usr/local/isa/cli
ADD ./api /usr/local/isa/api
RUN cat <<EOF > /bin/isa
CLI_FILE=\${BASH_SOURCE##*/}
export PYTHON_CLI_NAME=\${CLI_FILE%.*}
cd /usr/local/isa/cli
python main.py \${@}
EOF
RUN chmod +x /bin/isa

# Step : Install contents and setting container environment
## Copy contents
ADD ./modules /usr/local/modules
ADD ./configs /usr/local/configs
ADD ./docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +rx /docker-entrypoint.sh

## Setting container startup
WORKDIR /usr/local/configs
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["apiserver"]
