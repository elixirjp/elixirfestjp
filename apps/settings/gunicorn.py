bind = 'unix:/tmp/gunicorn.elixirconf.jp.sock'
backlog = 2048
workers = 2
worker_connections = 1024
max_requests = 0
# worker_class = 'gevent'
timeout = 3600
keepalive = 2

debug = True
spew = False

preload_app = True
daemon = False
pidfile = '/tmp/gunicorn_elixirconf.jp_live.pid'
user = 'www-data'
group = 'www-data'
umask = 0o002

logfile = '/var/log/supervisor/gunicorn.log'
loglevel = 'debug'
logconfig = None

limit_request_field_size = 32768
