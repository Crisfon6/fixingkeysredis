import redis
import numpy as np

class Database():
    def __init__(self,address,port,db):
        self.client1 = redis.Redis(host=address,port=port,db=db[0],charset="utf-8", decode_responses=True)#original
        self.client2 = redis.Redis(host=address,port=port,db=db[1],charset="utf-8", decode_responses=True)#with columns fixed
        self.client3 = redis.Redis(host=address,port=port,db=db[2],charset="utf-8", decode_responses=True)#with problems

    

