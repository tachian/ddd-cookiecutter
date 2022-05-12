# CDC Manager

## Credito Direto ao Consumidor

## RoadMap to UP:

 + Install Postgresql in your local machine
    + In Postgres execute:
        + `Create databases "Lendico";`
        + `Create databases "Lendico_test";`
        + `CREATE EXTENSION IF NOT EXISTS "uuid-ossp";`

 + Dependencies
   `sudo apt install libcurl4-openssl-dev libssl-dev`

 + Verify if SSH is configured:
    + `your local machine`
    + `your BitBucket count`

 + Clone repository
    + `git clone git@bitbucket.org:lendicobrasil/cdc-manager.git`

 + Create and activate "virtualenv"

 + Install "requirements":
    + `(pip install -r requirements-dev.txt)`

 + Set environment variable:
    + DATABASE_URI=postgresql://<user>:<password>@localhost:5432/<database>
    + BASE_URL_FRONT= <url for lendico page>
    + BASE_URL_FRONT_BACKOFFICE= <url for lendico backoffice page>
    + JWT_EXP_DELTA_SECONDS_ECOMMERCE= <Time in seconds for ecommerce communication expiration>
    + JWT_EXP_DELTA_SECONDS_RECOVERY_PASSWORD= <Time in seconds for link to recovery password expiration>
    + JWT_EXP_DELTA_SECS_NUVEMSHOP_PAYMENT = <Time in seconds for token generate to Nuvemshop payemnt. Default 10>
    + IDWALL_TOKEN= <App token from IdWall communication>
    + IDWALL_SECRET_TOKEN_WEBHOOK= <Secret-Token token from idWall webhook>
    + IDWALL_MATRIZ_RG= <Matriz param for analysis biometry>
    + IDWALL_MATRIZ_CNH= <Matriz param for analysis biometry>
    + IDWALL_URI= <uri for IdWall api>
    + LENDICO_CONTRACT_API_URL= <url for contract-manager>
    + LENDICO_CONTRACT_API_KEY= <key for contract-manager>
    + LENDICO_CONTRACT_API_TIMEOUT= <timeout for contract-manager service>
    + LENDICO_CONTRACT_PARTNER= <Web Service Strategy used on contract-manager>
    + CREDIT_ANALYSIS_ENGINE_URI= <url for credit-engine>
    + LENDICO_COMMUNICATION_API_URL=<url for lendico-communication service>
    + LENDICO_COMMUNICATION_API_KEY=<API Key lendico-communication service>
    + LENDICO_COMMUNICATION_API_TIMEOUT=<Maximum response time of lendico-communication service, default 600>
    + LENDICO_COMMUNICATION_RECOVERY_PASSWORD_TEMPLATE=<Template e-mail to recovery password, defaulf is 'RecoveryPassword'>
    + LENDICO_COMMUNICATION_LOGIN_TEMPLATE=<Template for login email, default is 'Login'>
    + BIOMETRY_RETRY_EMAIL_TEMPLATE=<Template for biometry re-submission notification, default is 'BiometryRetry'>
    + CART_RECOVERY_1_EMAIL_TEMPLATE=<Template for first cart recovery notification, default is 'CartRecoveryOne'>
    + CART_RECOVERY_2_EMAIL_TEMPLATE=<Template for second cart recovery notification, default is 'CartRecoveryTwo'>
    + CART_RECOVERY_3_EMAIL_TEMPLATE=<Template for third cart recovery notification, default is 'CartRecoveryThree'>
    + TOKEN_CREDIT_POLICY= <Token to create and get Credit Policy>
    + TOKEN_ADMINISTRATION= <Token to interact with the admin endpoints>
    + TOKEN_MAINTENANCE= <Token to interact with the maintenance endpoints>
    + EMAILAGE_ACCOUNT_SID= <SID authenticate in emailage>
    + EMAILAGE_AUTH_TOKEN= <Token authenticate in emailage>
    + EMAILAGE_ENVIRONMENT_SANDBOX= <Bool environment sandbox, default is True and False is ''>
    + CDC_BACKOFFICE_API_URL= <url for cdc-backoffice>
    + DATABASE_URI_TEST= postgresql://<user>:<password>@localhost:5432/<database>_URI_FOR_TESTS
    + T2MIO_SHORTENER_API_URL= <uri for T2mio>
    + T2MIO_SHORTENER_API_KEY= <key for T2mio>
    + T2MIO_SHORTENER_API_SECRET= <Secret for T2mio>
    + T2MIO_SHORTENER_API_PARAMS= <JSON with params to create shortened url, default is '{"expires_after": 1,
     "domain_id": 211, "slash_tag": "login-sms"}'>
    + SESSION_EXPIRY_TIME= <JSON with params to expire the session, default is '{"hours": 1}'>
    + NUMBER_DAYS_INTEGRATION_BOOKING_BANK= <Number of days for the integration booking bank>
    + MINIMUM_NUMBER_DAYS_UNTIL_FIRST_DUE_DATE= <Minimum days until first due date.>
    + ORDERHOOK_API_KEY= <key to be configured to be recieved on our order hook endpoint>
    + VTEX_HOOK_CONFIGURATION_API_URL= <uri for the vtex order hook configuration endpoint>
    + TESTING_VTEX= <flag informing whether perform processes related to VTEX Payment Providers tests or not,
     can be "True" or "False">
    + TOKEN_EXPIRATION_HOURS = <Number of hours that the platform token we generate will be valid. Default 500000>
    + VTEX_DELAY_TO_CANCEL= <delay, in seconds, to cancel payment on VTEX>
    + EXPIRE_LENDINGS_CRON_PARAMS= <JSON with params to execute cron to expire lendings, default is '{"hour": "*/1"}'>
    + LIMIT_HOURS_TO_LENDINGS_EXPIRES= <Number of hours that loans expire. Default 48>
    + BIOMETRY_ANALYSIS_TIMEOUT_SECONDS= <Seconds to wait before go to stage biometry_waiting. Default 60>
    + BIOMETRY_WAITING_TIMEOUT_SECONDS= <Seconds to wait before go to stage biometry_communication. Default 60>
    + EXPIRATION_CREDIT_DAYS= <Number of days to search old lendings to compose client credit limit >
    + DEFAULT_EMAIL_ACCOUNT= <Default email account, default is ''>
    + PUBSUB_BACKEND= <Backend implementation used on PubSub. Can be sqs or no_dep. 
      Default no_dep for Development and sqs for Staging and production>
    + SSE_IDLE_TIMEOUT = <time in seconds to close a SSE connection that are not sending messages>
    + BROKER_URL= <url to connect the Celery broker, default is 'sqs://'>
    + BROKER_TRANSPORT_OPTIONS= <JSON with params for configure Celery broker, default is '{}'>
    + QUEUE_NOTIFY_CCB_SIGNATURE_ON_MANAGER = <queue name responsible for execute signature notification>
    + QUEUE_SEND_LENDING_TO_BACKOFFICE = <queue name responsible to send lending to backoffice>
    + QUEUE_CHANGE_STAGE_TO_TIMEOUT = <queue name responsible to change stages to timeout destination stage>
    + QUEUE_SEND_CART_RECOVERY_NOTIFICATION = <queue name responsible for sending cart recovery notifications>
    + PRICING_API_KEY= <pricing service api key (default='')>
    + PRICING_CALCULATOR_URI= <pricing calculator URI (default='')>
    + PRICING_CALCULATOR_DAYS_PER_MONTH= <days per month (default=30)>
    + PRICING_CALCULATOR_DAYS_PER_YEAR= <days per year (default=360)>
    + PRICING_CALCULATOR_DAYS_PER_YEAR_FOR_CET_OUTPUT= <days per year for CET output (default=365)>
    + PRICING_CALCULATOR_DAYS_PER_YEAR_FOR_INTEREST_OUTPUT= <days per year for interest output (default=360)>
    + PRICING_CALCULATOR_FLAT_IOF_RATE= <flat iof rate (default="0.0038")>
    + PRICING_CALCULATOR_MAX_IOF_RATE= <max iof rate (default="0.02993")>
    + PRICING_CALCULATOR_DAILY_IOF_RATE= <daily iof rate (default="0.000082")>
    + PRICING_CALCULATOR_MAX_LOAN_VALUE_DIFF= <max loan value diff (default="0.0000001")>
    + PRICING_CALCULATOR_MIN_DAILY_INTEREST_RATE= <min daily interest rate (default="0")>
    + PRICING_CALCULATOR_MAX_DAILY_INTEREST_RATE= <max daily interest rate (default="0.004")>
    + PRICING_CALCULATOR_MAX_DAILY_INTEREST_RATE_DIFF= <max daily interest rate diff (default="0.000000001")>
    + PRICING_CALCULATOR_MIN_YEARLY_CET_RATE= <min yearly cet rate (default="0")>
    + PRICING_CALCULATOR_MAX_YEARLY_CET_RATE= <max yearly cet rate (default="100.00")>
    + PRICING_CALCULATOR_MAX_YEARLY_CET_RATE_DIFF= <max yearly cet rate diff (default="0.000000001")>
    + UNICO_ISS= <Unico ISS Key>
    + UNICO_TOKEN_URI= <Unico token generation service URI>
    + UNICO_API_URI= <Unico API URI>
    + UNICO_API_KEY= <Unico API Key>
    + UNICO_SECRET_TOKEN_WEBHOOK= <token configured on Unico webhook>
    + CART_RECOVERY_INTERVAL_1 = <First interval of time to send cart recovery communication, default '{"hours": 1}'>
    + CART_RECOVERY_INTERVAL_2 = <Second interval of time to send cart recovery communication, default '{"hours": 5}'>
    + CART_RECOVERY_INTERVAL_3 = <Third interval of time to send cart recovery communication, default '{"hours": 12}'>
    + CART_RECOVERY_INTERVAL_4 = <Fourth interval of time to send cart recovery communication, default '{"hours": 12}'>
    + NUVEMSHOP_TOKEN_URI = <Nuvemshop token generation api url. Default 'https://www.nuvemshop.com.br'>
    + NUVEMSHOP_API_URI = <Numvemshop service api url. Default 'https://api.nuvemshop.com.br/v1'>
    + NUVEMSHOP_REQUEST_EMAIL_TEMPLATE= <Template for Nuvemshop retailer register request notification. Default 'NuvemshopRetailerRequest'>
    + NUVEMSHOP_REQUEST_CONCLUDED_EMAIL_TEMPLATE = <Template for Nuvemshop retailer register conclusion notification. Default 'NuvemshopRetailerRequestConcluded'>
    + NUVEMSHOP_REQUEST_DENIED_EMAIL_TEMPLATE = <Template for Nuvemshop retailer register deny notification. Default 'NuvemshopRetailerRequestDenied'>
    + NUVEMSHOP_REQUEST_NOTIFY_EMAILS_LIST= <List of email addres to send Nuvemshop retailer request notification email. Default '[]'>
    + RETAILER_REDACT_REQUEST_EMAIL_TEMPLATE = <Template for retailer redact request notification. Default 'RetailerRedactRequest'>
    + CLIENT_REDACT_REQUEST_EMAIL_TEMPLATE= = <Template for client redact request notification. Default 'ClientRedactRequest'>
    + CLIENT_DATA_REQUEST_EMAIL_TEMPLATE = <Template for client data request notification. Default 'ClientDataRequest'>
    + DATA_REQUESTS_NOTIFY_EMAILS_LIST = <List of email addres to send redact and data requests notification emails. Default '[]'>
    + NUVEMSHOP_PROVIDER_DESCRIPTION = <Payment Provider desciption to be shown to retailer. Default 'Parcele suas compras em até 24 vezes'>
    + NUVEMSHOP_PROVIDER_LOGO_400 = <Url for logo in 400x120, to be displayed to retailer>
    + NUVEMSHOP_PROVIDER_LOGO_160 = <Url for logo in 160x100, to be displayed to retailer>
    + NUVEMSHOP_SUPPORT_URL = <Url for retailer support>
    + NUVEMSHOP_CHECKOUT_JS_URL = <Url for Nuvemshop checkout CDN>
    + NUVEMSHOP_DAYS_TO_WITHDRAW_MONEY = <Info about days since transaction creation until money be available to retailer>
    + NUVEMSHOP_CHECKOUT_DESCRIPTION = <Payment Option description to be shown to customer. Default 'Parcele suas compras em até 24 vezes'>
    + NUVEMSHOP_CHECKOUT_LOGO = <Url for logo to be displayed to customer on checkout>
    + NUVEMSHOP_INITIAL_APP_ID = <Numveshop app client id loaded on platform creation during load-initial-data command. Default '3280'>
    + NUVEMSHOP_INITIAL_APP_SECRET = <Numveshop app client secret loaded on platform creation during load-initial-data command. Default 'mfA00nZiQOtLhj3HaXEr0TvrSPXSISsE00QLQPnzIxuO9UA6'>
    + NUVEMSHOP_CHECKOUT_NAME = <Name of payment method to be displayed for the merchant and custormer. Default 'Provu Parcelado'>
    + NUVEMSHOP_CHECKOUT_ID = <Id of payment method, must be different for each environment and match checkout script. Default 'bpl_payment'>
    + CDC_MANAGER_PUBLIC_URI = <App public Uri, to be used on webhooks configuration>
    + CDC_BACKOFFICE_PUBLIC_URI = <CDC Backoffice public Uri, to be used on webhooks configuration>

 + Execute
    + `flask db migrate`

 + Start server
    + `flask run`

 + HEALTH endpoints
    + /api/healthz: If API is working, must show {"service": "Lendico CDC API HealthCheck", "version": "9.9.9"}
    + /api/docs/swagger: IF API is working, musta show SWAGGER page

## Commands
 + Reset Database
	+ `flask drop-create-tables`
 + Load Initial Data
	+ `flask load-initial-data`

  To use the Makefile and other utilities, be sure to install
  [GNU Make](https://www.gnu.org/software/make/) and
  [jq](https://stedolan.github.io/jq/).

## Generate the Docker image

In the repository root there is a `Makefile`. You can use it to build a Docker
image from the `Dockerfile` and other things: check the file for the available
targets.

It is also possible also to start an automatic build by `git push`ing
changes do the `docker_build` branch. Bitbucket will start the pipeline
described in the `bitbucket-pipelines.yml`, which will build, tag and push the
image to our Docker registry (Docker Hub).

### Managing the image name and tag

Both Docker image name and tag are defined in the `Makefile`. Here is an
example:

```
IMAGE_NAME=lendicoti/cdc-manager
VERSION=0.1.0
TAG=latest
```

The version should be managed using the [SEMVER](https://semver.org/) scheme,
and versioned with the `Makefile` itself for better control.

## Architecture

### Architecture Decision Reports

`adr-viewer --adr-path doc/architecture/decisions/ --serve`

## Domain

![Domain Diagram](doc/uml/domain.png)

## Lendico standards applied

* [Jenkins](https://lendicobr.atlassian.net/wiki/spaces/TI/pages/119439575/Padr+es+de+jobs+no+Jenkins)
* [Docker](https://lendicobr.atlassian.net/wiki/spaces/TI/pages/35848362/Padr+es+para+containers+Docker)
