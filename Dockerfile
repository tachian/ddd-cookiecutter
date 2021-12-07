FROM 178164760726.dkr.ecr.us-east-1.amazonaws.com/lendico.python3.9-base:v0.1.19 as base

# LABELS
LABEL maintainer="Lendico <contato@lendico.com.br>"
LABEL slack="squad-titan"
LABEL application="cdc-manager"
LABEL repository="bitbucket.org:lendicobrasil/cdc-manager.git"

# Copy project main folder
COPY main main

# Testing stage
FROM base AS testing

# Install testing packages (customize according to this application)
# Note: Do not put any lib here except for testing.
#       These libs will only be installed in the test container
RUN pip install coverage freezegun mock pytest pytest-cov pytest-mock requests-mock moto[sqs,sns] --no-cache-dir

# Run tests
COPY tests tests
ENV LENDICO_CDCMANAGER_DEPLOY_ENV='Testing'
RUN coverage run -m pytest -vvs --junitxml=/report.xml \
    --skip-startfinish\
    --ignore=tests/integration \
    --ignore=tests/test_migrations.py \
    --ignore=tests/unit/application_layer/adapters/test_grafana_sevice.py \
    --ignore-glob=*_repository.py
RUN coverage xml -o /coverage.xml

# Final stage
FROM base AS final

RUN mkdir -p main

## insert custom codes from application here

EXPOSE 5000
ENTRYPOINT ["./entrypoint.sh"]
