import json

import redis


class CacheRedis:
    def __init__(self, host, port, db=0):
        self.cache_redis = redis.Redis(host=host, port=port, db=db)

    def get(self, key):
        return self.cache_redis.get(key)

    def set(self, key, data):
        self.cache_redis.set(key, json.dumps(data))

    def get_cache_from_db(self, key: str, get_db_func, ex=None):
        data_redis = self.cache_redis.get(key)
        if data_redis is None:
            data = get_db_func()
            data_str = json.dumps(data)
            self.cache_redis.set(key, data_str, ex=ex)
        else:
            data = json.loads(data_redis)
        return data
