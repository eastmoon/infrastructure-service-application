# Step : base
FROM python:slim

# Update linux package manager
RUN apt-get update -y

# Update python package manager
RUN pip install --upgrade pip

# Install yaml parser tools
RUN pip install pyyaml

# Install python requirement
RUN pip install \
    pyyaml

# Step : Python FastAPI
# Install FastAPI
RUN pip install \
    fastapi \
    uvicorn[standard]

# Install API server
ADD ./api/docker-entrypoint.sh /docker-entrypoint.sh
ADD ./api/server /usr/local/fastapi
RUN chmod +rx /docker-entrypoint.sh

# Step : Command line interface
# Install CLI
ADD ./cli /usr/local/isa

RUN cat <<EOF > /bin/isa
CLI_FILE=\${BASH_SOURCE##*/}
export PYTHON_CLI_NAME=\${CLI_FILE%.*}
cd /usr/local/isa
python main.py \${@}
EOF
RUN chmod +x /bin/isa

# Setting
WORKDIR /app
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["apiserver"]
