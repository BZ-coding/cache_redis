# cache_redis

使用redis作为数据库的缓存。当然，也可以单独使用redis。

## 安装

```shell
git clone https://github.com/BZ-coding/cache_redis utils/cache_redis
```

## 使用

```python
from UTILS.cache_redis import CacheRedis

cache_redis = CacheRedis(host=redis_host, port=redis_port, db=0)

cache_redis.set('rss', data)
data = cache_redis.get('rss')
cache_redis.get_cache_from_db('rss', get_db_rsses_func)
```

