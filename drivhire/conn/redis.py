import redis
import os

conn = redis.Redis(host=os.environ.get('REDIS_HOST'),port=os.environ.get('REDIS_PORT'),db=os.environ.get('REDIS_DB'))
