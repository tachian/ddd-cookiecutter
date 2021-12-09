import logging
from distutils.util import strtobool
from json import loads
from dot
from env_kills.assertions import EnvKills

load_dotenv()


class BaseConfig(object):
    env_cfg = EnvKills(namespace='LENDICO_CDCMANAGER',
                       environment='DEPLOY_ENV')
    DEBUG = False
    TESTING = False
    LOGS_LEVEL = logging.INFO
    RESTX_VALIDATE = True

    DEPLOY_ENV = env_cfg.deploy_env(default='Development')
    ENV_KILLS = env_cfg
    BASE_URL_FRONT = env_cfg.base_url_front(default='http://localhost:4000')
    SESSION_EXPIRY_TIME = loads(
        env_cfg.session_expiry_time(default='{"hours":1}'))
    NUMBER_DAYS_INTEGRATION_BOOKING_BANK = int(
        env_cfg.number_days_integration_booking_bank(default=15))
    MINIMUM_NUMBER_DAYS_UNTIL_FIRST_DUE_DATE = int(
        env_cfg.minimum_number_days_until_first_due_date(default=30))
    EXPIRE_LENDINGS_CRON_PARAMS = loads(
        env_cfg.expire_lendings_cron_params(default='{"hour":"*/1"}'))
    LIMIT_HOURS_TO_LENDINGS_EXPIRES = int(
        env_cfg.limit_hours_to_lendings_expires(default=48))
    EXPIRATION_CREDIT_DAYS = int(
        env_cfg.expiration_credit_days(default=60))
    DEFAULT_EMAIL_ACCOUNT = env_cfg.default_email_account(default='')

    # Database
    # for the default URI, check Makefile
    SQLALCHEMY_DATABASE_URI = env_cfg.database_manager_uri(
        default='postgresql://postgres:mysecretpassword@localhost:5432/Lendico')
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # Config contract-manager
    LENDICO_CONTRACT_API_URL = env_cfg.lendico_contract_api_url(default='')
    LENDICO_CONTRACT_API_KEY = env_cfg.lendico_contract_api_key(default='')
    LENDICO_CONTRACT_API_TIMEOUT = int(
        env_cfg.lendico_contract_api_timeout(default=600))
    LENDICO_CONTRACT_PARTNER = env_cfg.lendico_contract_partner(
        default='SOROCRED')

    # Config lendico-communication
    LENDICO_COMMUNICATION_API_URL = env_cfg.lendico_communication_api_url(
        default='')
    LENDICO_COMMUNICATION_API_KEY = env_cfg.lendico_communication_api_key(
        default='')
    LENDICO_COMMUNICATION_API_TIMEOUT = int(
        env_cfg.lendico_communication_api_timeout(default=600))
    LENDICO_COMMUNICATION_LOGIN_TEMPLATE = env_cfg.lendico_communication_login_template(default='Login')
    LENDICO_COMMUNICATION_RECOVERY_PASSWORD_TEMPLATE = env_cfg.lendico_communication_recovery_password_template(
        default='RecoveryPassword')
    BIOMETRY_RETRY_EMAIL_TEMPLATE = env_cfg.biometry_retry_email_template(default='BiometryRetry')
    CART_RECOVERY_1_EMAIL_TEMPLATE = env_cfg.cart_recovery_1_email_template(default='CartRecoveryOne')
    CART_RECOVERY_2_EMAIL_TEMPLATE = env_cfg.cart_recovery_2_email_template(default='CartRecoveryTwo')
    CART_RECOVERY_3_EMAIL_TEMPLATE = env_cfg.cart_recovery_3_email_template(default='CartRecoveryThree')
    EMAIL_FILES_PATH = env_cfg.email_files_path(default="./src/cdc/application_layer/communication/templates")

    # Shopping Cart recovery communications
    CART_RECOVERY_INTERVAL_1 = loads(env_cfg.cart_recovery_interval_1(default='{"hours": 1}'))
    CART_RECOVERY_INTERVAL_2 = loads(env_cfg.cart_recovery_interval_2(default='{"hours": 5}'))
    CART_RECOVERY_INTERVAL_3 = loads(env_cfg.cart_recovery_interval_3(default='{"hours": 12}'))
    CART_RECOVERY_INTERVAL_4 = loads(env_cfg.cart_recovery_interval_4(default='{"hours": 12}'))

    # Config credit-engine
    CREDIT_ANALYSIS_ENGINE_URI = env_cfg.credit_analysis_engine_uri(
        default='http://localhost:3000')

    # Config IDWall
    IDWALL_SECRET_TOKEN_WEBHOOK = env_cfg.idwall_secret_token_webhook(
        default='')
    IDWALL_TOKEN = env_cfg.idwall_token(default='')
    IDWALL_URI = env_cfg.idwall_uri(default='')
    IDWALL_MATRIZ_RG = env_cfg.idwall_matriz_rg(default='')
    IDWALL_MATRIZ_CNH = env_cfg.idwall_matriz_cnh(default='')
    IDWALL_MATRIZ_DOCUMENTOSCOPIA = env_cfg.idwall_matriz_documentoscopia(default='')

    # Config Unico
    UNICO_ISS = env_cfg.unico_iss(default='')
    UNICO_TOKEN_URI = env_cfg.unico_token_uri(default='')
    UNICO_API_KEY = env_cfg.unico_api_key(default='')
    UNICO_API_URI = env_cfg.unico_api_uri(default='')
    UNICO_SECRET_TOKEN_WEBHOOK = env_cfg.unico_secret_token_webhook(default='')

    UNICO_MAX_ATTEMPTS_BIOMETRY = int(env_cfg.unico_max_attempts_biometry(default='3'))
    UNICO_BIOMETRY_SCORE_NO_DOCUMENTOSCOPIA = int(env_cfg.unico_biometry_score_no_documentoscopia(default='40'))

    # Config CreditPolicy
    TOKEN_CREDIT_POLICY = env_cfg.token_credit_policy(default='')

    # Backoffice
    CDC_BACKOFFICE_API_URL = env_cfg.cdc_backoffice_api_url(default='')
    BASE_URL_FRONT_BACKOFFICE = env_cfg.base_url_front_backoffice(default='')

    # Config delay to cancel for VTEX
    VTEX_DELAY_TO_CANCEL = env_cfg.vtex_delay_to_cancel(default=90000)

    # Token JWT
    JWT_EXP_DELTA_SECONDS_ECOMMERCE = int(env_cfg.jwt_exp_delta_secs_ecommerce(default=60))
    JWT_EXP_DELTA_SECONDS_RECOVERY_PASSWORD = int(env_cfg.jwt_exp_delta_secs_recovery_password(default=600))
    JWT_EXP_DELTA_SECS_NUVEMSHOP_PAYMENT = int(env_cfg.jwt_exp_delta_secs_nuvemshop_payment(default='10'))

    # Maintenance
    TOKEN_MAINTENANCE = env_cfg.token_maintenance(default='1234567890')

    # Token Administration
    TOKEN_ADMINISTRATION = env_cfg.token_administration(default='1234567890')

    # T2mio - Shortener url
    T2MIO_SHORTENER_API_URL = env_cfg.t2mio_shortener_api_url(default='')
    T2MIO_SHORTENER_API_KEY = env_cfg.t2mio_shortener_api_key(default='')
    T2MIO_SHORTENER_API_SECRET = env_cfg.t2mio_shortener_api_secret(default='')
    T2MIO_SHORTENER_API_PARAMS = loads(
        env_cfg.t2mio_shortener_api_params(default='{}'))

    # Emailage
    EMAILAGE_ACCOUNT_SID = env_cfg.emailage_account_sid(default='')
    EMAILAGE_AUTH_TOKEN = env_cfg.emailage_auth_token(default='')
    EMAILAGE_ENVIRONMENT_SANDBOX = bool(
        env_cfg.emailage_environment_sandbox(default=True))

    # envs to platforms communication
    X_API_APP_KEY = env_cfg.x_api_app_key(default='appkey-test')
    X_API_APP_TOKEN = env_cfg.x_api_app_token(default='apptoken-test')
    VTEX_API_APP_KEY = env_cfg.vtex_api_app_key(default='vtex-appkey-test')
    VTEX_API_APP_TOKEN = env_cfg.vtex_api_app_token(
        default='vtex-apptoken-test')
    TOKEN_EXPIRATION_HOURS = int(
        env_cfg.token_expiration_hours(default=500000))

    # Flow Stages timeouts
    BIOMETRY_WAITING_TIMEOUT_SECONDS = int(
        env_cfg.biometry_waiting_timeout_seconds(default=60))
    BIOMETRY_ANALYSIS_TIMEOUT_SECONDS = int(
        env_cfg.biometry_analysis_timeout_seconds(default=60))

    # Flag to activate VTEX payment providers testing processes
    TESTING_VTEX = bool(strtobool(env_cfg.testing_vtex(default='False')))

    # Celery
    BROKER_URL = env_cfg.broker_url(default='sqs://')
    BROKER_TRANSPORT_OPTIONS = loads(
        env_cfg.broker_transport_options(default='{}'))
    QUEUE_NOTIFY_CCB_SIGNATURE_ON_MANAGER = env_cfg.queue_notify_ccb_signature_on_manager(default='')
    QUEUE_SEND_LENDING_TO_BACKOFFICE = env_cfg.queue_send_lending_to_backoffice(default='')
    QUEUE_CHANGE_STAGE_TO_TIMEOUT = env_cfg.queue_change_stage_to_timeout(
        default='')

    LOCALSTACK_URL = env_cfg.localstack_url(default='') or None

    # Backend implementation of PubSub, can be sqs or no_dep
    PUBSUB_BACKEND = env_cfg.pubsub_backend(
        default='no_dep' if DEPLOY_ENV == 'Development'
        else 'sqs')

    # Time in seconds to close a SSE connection that are not sending messages
    SSE_IDLE_TIMEOUT = int(env_cfg.sse_idle_timeout(default='120'))

    # Pricing - calculator
    PRICING_API_KEY = env_cfg.pricing_api_key(default='')
    PRICING_CALCULATOR_URI = env_cfg.pricing_calculator_uri(default='')
    PRICING_CALCULATOR_DAYS_PER_MONTH = env_cfg.pricing_calculator_days_per_month(default=30)
    PRICING_CALCULATOR_DAYS_PER_YEAR = env_cfg.pricing_calculator_days_per_year(default=360)
    PRICING_CALCULATOR_DAYS_PER_YEAR_FOR_CET_OUTPUT = env_cfg.pricing_calculator_days_per_year_for_cet_output(
        default=365)
    PRICING_CALCULATOR_DAYS_PER_YEAR_FOR_INTEREST_OUTPUT = env_cfg.pricing_calculator_days_per_year_for_interest_output(
        default=360)
    PRICING_CALCULATOR_FLAT_IOF_RATE = env_cfg.pricing_calculator_flat_iof_rate(default="0.0038")
    PRICING_CALCULATOR_MAX_IOF_RATE = env_cfg.pricing_calculator_max_iof_rate(default="0.02993")
    PRICING_CALCULATOR_DAILY_IOF_RATE = env_cfg.pricing_calculator_daily_iof_rate(default="0.000082")
    PRICING_CALCULATOR_MAX_LOAN_VALUE_DIFF = env_cfg.pricing_calculator_max_loan_value_diff(default="0.0000001")
    PRICING_CALCULATOR_MIN_DAILY_INTEREST_RATE = env_cfg.pricing_calculator_min_daily_interest_rate(default="0")
    PRICING_CALCULATOR_MAX_DAILY_INTEREST_RATE = env_cfg.pricing_calculator_max_daily_interest_rate(default="0.004")
    PRICING_CALCULATOR_MAX_DAILY_INTEREST_RATE_DIFF = env_cfg.pricing_calculator_max_daily_interest_rate_diff(
        default="0.000000001")
    PRICING_CALCULATOR_MIN_YEARLY_CET_RATE = env_cfg.pricing_calculator_min_yearly_cet_rate(default="0")
    PRICING_CALCULATOR_MAX_YEARLY_CET_RATE = env_cfg.pricing_calculator_max_yearly_cet_rate(default="100.00")
    PRICING_CALCULATOR_MAX_YEARLY_CET_RATE_DIFF = env_cfg.pricing_calculator_max_yearly_cet_rate_diff(
        default="0.000000001")

    # Nuvemshop
    NUVEMSHOP_TOKEN_URI = env_cfg.nuvemshop_token_uri(default='https://www.nuvemshop.com.br')
    NUVEMSHOP_API_URI = env_cfg.nuvemshop_api_uri(default='https://api.nuvemshop.com.br/v1')
    NUVEMSHOP_REQUEST_NOTIFY_EMAILS_LIST = loads(env_cfg.nuvemshop_request_notify_emails_list(default='[]'))
    NUVEMSHOP_REQUEST_EMAIL_TEMPLATE = env_cfg.nuvemshop_request_email_template(default='NuvemshopRetailerRequest')
    NUVEMSHOP_REQUEST_CONCLUDED_EMAIL_TEMPLATE = env_cfg.nuvemshop_request_concluded_email_template(
        default='NuvemshopRetailerRequestConcluded')
    NUVEMSHOP_REQUEST_DENIED_EMAIL_TEMPLATE = env_cfg.nuvemshop_request_denied_email_template(
        default='NuvemshopRetailerRequestDenied')

    # Nuvemshop Payment Provider Configurations
    NUVEMSHOP_PROVIDER_DESCRIPTION = env_cfg.nuvemshop_provider_description(
        default='Parcele suas compras em até 24 vezes')
    NUVEMSHOP_PROVIDER_LOGO_400 = env_cfg.nuvemshop_provider_logo_400(default='')
    NUVEMSHOP_PROVIDER_LOGO_160 = env_cfg.nuvemshop_provider_logo_160(default='')
    NUVEMSHOP_SUPPORT_URL = env_cfg.nuvemshop_support_url(default='')
    NUVEMSHOP_CHECKOUT_JS_URL = env_cfg.nuvemshop_checkout_js_url(default='')
    NUVEMSHOP_DAYS_TO_WITHDRAW_MONEY = int(env_cfg.nuvemshop_days_to_withdraw_money(default=6))
    NUVEMSHOP_CHECKOUT_DESCRIPTION = env_cfg.nuvemshop_checkout_description(
        default='Parcele suas compras em até 24 vezes')
    NUVEMSHOP_CHECKOUT_LOGO = env_cfg.nuvemshop_checkout_logo(default='')
    NUVEMSHOP_CHECKOUT_NAME = env_cfg.nuvemshop_checkout_name(default='Provu Parcelado')
    NUVEMSHOP_CHECKOUT_ID = env_cfg.nuvemshop_checkout_id(default='bpl_payment')

    # Nuvemshop app authentication loaded on load-initial-data
    NUVEMSHOP_INITIAL_APP_ID = env_cfg.nuvemshop_initial_app_id(default='3280')
    NUVEMSHOP_INITIAL_APP_SECRET = env_cfg.nuvemshop_initial_app_secret(
        default='mfA00nZiQOtLhj3HaXEr0TvrSPXSISsE00QLQPnzIxuO9UA6')

    DATA_REQUESTS_NOTIFY_EMAILS_LIST = loads(env_cfg.data_requests_notify_emails_list(default='[]'))
    RETAILER_REDACT_REQUEST_EMAIL_TEMPLATE = env_cfg.retailer_redact_request_email_template(
        default='RetailerRedactRequest')
    CLIENT_REDACT_REQUEST_EMAIL_TEMPLATE = env_cfg.client_redact_request_email_template(
        default='ClientRedactRequest')
    CLIENT_DATA_REQUEST_EMAIL_TEMPLATE = env_cfg.client_data_request_email_template(
        default='ClientDataRequest')

    CDC_MANAGER_PUBLIC_URI = env_cfg.cdc_manager_public_uri(default='')
    CDC_BACKOFFICE_PUBLIC_URI = env_cfg.cdc_backoffice_public_uri(default='')

    ENV_KILLS = env_cfg


class TestingConfig(BaseConfig):
    env_cfg = EnvKills(namespace='LENDICO_CDCMANAGER',
                       environment='DEPLOY_ENV')

    DEBUG = True
    TESTING = True
    PROPAGATE_EXCEPTIONS = False
    LOGS_LEVEL = logging.CRITICAL
    SQLALCHEMY_DATABASE_URI = env_cfg.database_manager_uri_test(default='postgresql://')

    BASE_URL_FRONT = 'http://localhost:4000'

    # Config Communication
    LENDICO_COMMUNICATION_API_URL = 'https://test-communications.com'
    LENDICO_COMMUNICATION_API_KEY = '1234567890'
    EMAIL_FILES_PATH = "./tests/fixtures/templates"

    BASE_URL_FRONT_BACKOFFICE = 'http://localhost:4002'

    TOKEN_EXPIRATION_HOURS = 24

    LOCALSTACK_URL = None


class StagingConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    LOGS_LEVEL = logging.INFO


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    env_cfg = EnvKills(namespace='LENDICO_CDCMANAGER',
                       environment='DEPLOY_ENV')

    LOGS_LEVEL = int(env_cfg.log_level(default=logging.INFO))
