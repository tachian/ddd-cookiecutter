# {{cookiecutter.project_name}}

## {{cookiecutter.project_description}}

## RoadMap to UP:

 + Install {{cookiecutter.database}} in your local machine or use a docker image
    + In {{cookiecutter.database}} execute:
        + `Create databases "{{cookiecutter.project_slug}}";`
        + `Create databases "{{cookiecutter.project_slug}}_test";`
        {% if cookiecutter.database|lower == 'postgres'-%}
        + `CREATE EXTENSION IF NOT EXISTS "uuid-ossp";`
        {% endif %}

 + Dependencies
   `sudo apt install libcurl4-openssl-dev libssl-dev`

 + Verify if SSH is configured:
    + `your local machine`
    + `your BitBucket count`

 + Clone repository
    + `git clone {{cookiecuttter.project_repository}}`

 + Create and activate "virtualenv"

 + Install "requirements":
    + `(pip install -r {{cookiecuttter.project_source}}/requirements-dev.txt)`

 + Set environment variable:
    + DEPLOY_ENV=<environment where App will run>
    + LOGS_LEVEL=<Level of logs - Used on production environment>
    + DATABASE_URI={{cookiecutter.database}}://<user>:<password>@localhost:5432/<database>
    + DATABASE_URI_TEST={{cookiecutter.database}}://<user>:<password>@localhost:5432/<database>_test

 + Execute (inside {{cookiecuttter.project_source}} dir)
    + `flask db migrate` To generate database revision files
    + `flask db upgrade` To apply revision files

 + Start server (inside {{cookiecuttter.project_source}} dir)
    + `flask run`

 + HEALTH endpoints
    + /api/healthz: If API is working, must show {"service": "{{cookiecutter.health_message}}", "version": "9.9.9"}
    + /api/docs/swagger: IF API is working, must show SWAGGER page

## Commands
 + Reset Database (inside {{cookiecuttter.project_source}} dir)
	+ `flask drop-create-tables`

## Generate the Docker image

Inside {{cookiecutter.project_source}} execute `docker build . -t {{cookiecutter.project_slug}}:<tage>`

A merge to dev or qa branchs will also build an image automatically on Jenkins and push it to AWS ECR

### Managing the image tag

The tag must be changed manually on .env.yaml file before opening a PR to dev or qa branches.

The version should be managed using the [SEMVER](https://semver.org/) scheme

## Lendico standards applied

* [Jenkins](https://lendicobr.atlassian.net/wiki/spaces/TI/pages/119439575/Padr+es+de+jobs+no+Jenkins)
* [Docker](https://lendicobr.atlassian.net/wiki/spaces/TI/pages/35848362/Padr+es+para+containers+Docker)
