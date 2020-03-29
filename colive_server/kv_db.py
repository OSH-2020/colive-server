from redis import Redis

from .app import app

kv_db = Redis.from_url(app.config['REDIS_URI'])
