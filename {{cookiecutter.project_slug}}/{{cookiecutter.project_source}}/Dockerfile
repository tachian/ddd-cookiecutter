FROM 178164760726.dkr.ecr.us-east-1.amazonaws.com/lendico.python3.9-base:v0.1.34 as base

# LABELS
LABEL maintainer="{{cookiecutter.project_mantainer}}"
LABEL slack="squad-titan"
LABEL application="{{cookiecutter.project_slug}}"
LABEL repository="{{cookiecutter.project_repository}}"

# Copy project main folder
COPY {{cookiecutter.project_main_folder}} {{cookiecutter.project_main_folder}}

# Testing stage
FROM base AS testing

# Install testing packages (customize according to this application)
# Note: Do not put any lib here except for testing.
#       These libs will only be installed in the test container
RUN pip install coverage freezegun mock pytest pytest-cov pytest-mock requests-mock mixer --no-cache-dir

# Run tests
COPY tests tests
RUN coverage run -m pytest -vvs --junitxml=/report.xml
RUN coverage xml -o /coverage.xml -i

# Final stage
FROM base AS final

RUN mkdir -p {{cookiecutter.project_main_folder}}

## insert custom codes from application here

EXPOSE 5000
ENTRYPOINT ["./entrypoint.sh"]
