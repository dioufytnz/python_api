from multiprocessing import cpu_count

# Socket Path
#bind = 'unix:/projets/python_api/gunicorn.sock'

# Worker Options
workers = cpu_count() + 1
worker_class = 'uvicorn.workers.UvicornWorker'

# Logging Options
loglevel = 'debug'
accesslog = '/var/log/apache2/access_FastApi_log'
errorlog = '/var/log/apache2/error_FastApi_log'
