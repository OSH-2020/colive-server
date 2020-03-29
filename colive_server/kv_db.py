from redis import Redis

from .app import app

if app.config['DEBUG']:
    from .test.mock_redis import MockRedis
    kv_db = MockRedis()
else:
    kv_db = Redis.from_url(app.config['REDIS_URI'])
