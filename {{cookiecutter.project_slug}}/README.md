# {{cookiecutter.project_name}}

## {{cookiecutter.project_description}}

## RoadMap to UP:

{%- if cookiecutter.database|lower != 'nosql' -%}
 + Install {{cookiecutter.database}} in your local machine or use a docker image
    + In {{cookiecutter.database}} execute:
        + `Create databases "{{cookiecutter.project_slug}}";`
        + `Create databases "{{cookiecutter.project_slug}}_test";`
        {%- if cookiecutter.database|lower == 'postgres' -%}
        + `CREATE EXTENSION IF NOT EXISTS "uuid-ossp";`
        {%- endif %}
{%- endif %}

 + Dependencies
   `sudo apt install libcurl4-openssl-dev libssl-dev`

 + Verify if SSH is configured:
    + `your local machine`
    + `your BitBucket count`

 + Clone repository
    + `git clone {{cookiecutter.project_repository}}`

 + Create and activate "virtualenv"

 + Install "requirements":
    + `(pip install -r {{cookiecutter.project_source}}/requirements-dev.txt)`

 + Set environment variable:
    + DEPLOY_ENV=<environment where App will run>
    + LOGS_LEVEL=<Level of logs - Used on production environment>
    {%- if cookiecutter.database|lower != 'nosql' -%}
    + DATABASE_URI={{cookiecutter.database}}://<user>:<password>@localhost:5432/<database>
    + DATABASE_URI_TEST={{cookiecutter.database}}://<user>:<password>@localhost:5432/<database>_test
    {%- endif %}

 {%- if cookiecutter.database|lower != 'nosql' -%}
 + Execute (inside {{cookiecutter.project_source}} dir)
    + `flask db migrate` To generate database revision files
    + `flask db upgrade` To apply revision files
 {%- endif %}

 + Start server (inside {{cookiecutter.project_source}} dir)
    + `flask run`

 + HEALTH endpoints
    + /api/healthz: If API is working, must show {"service": "{{cookiecutter.health_message}}", "version": "9.9.9"}
    + /api/docs/swagger: IF API is working, must show SWAGGER page

## Commands
 + Reset Database (inside {{cookiecutter.project_source}} dir)
	+ `flask drop-create-tables`

## Generate the Docker image

Inside {{cookiecutter.project_source}} execute `docker build . -t {{cookiecutter.project_slug}}:<tag>`

A merge to dev or qa branchs will also build an image automatically on Jenkins and push it to AWS ECR

### Managing the image tag

The tag must be changed manually on .env.yaml file before opening a PR to dev or qa branches.

The version should be managed using the [SEMVER](https://semver.org/) scheme
