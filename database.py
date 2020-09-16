import redis
import numpy as np

client1 = redis.Redis(host="127.0.0.1",port="6379",db=0,charset="utf-8", decode_responses=True)#original
client2 = redis.Redis(host="127.0.0.1",port="6379",db=2,charset="utf-8", decode_responses=True)#with columns fixed
client3 = redis.Redis(host="127.0.0.1",port="6379",db=3,charset="utf-8", decode_responses=True)#with problems

keys = np.array(client1.keys(),dtype=np.str)

