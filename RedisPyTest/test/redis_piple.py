# python3
# Redis 新特性---pipeline（管道）
import redis
import time
def without_pipeline():
    r = redis.Redis("localhost", 6379)
    for i in range(10000):
        r.ping()    # 使用客户端向 Redis 服务器发送一个 PING ，如果服务器运作正常的话，会返回一个 PONG
    return
def with_pipeline():
    r = redis.Redis()
    pipeline = r.pipeline()
    for i in range(10000):
        pipeline.ping()
    pipeline.execute()
    return
def bench(desc) :
    start = time.clock()
    desc()
    stop = time.clock()
    diff = stop - start
    print("%s has token %s" % (desc.__name__, str(diff)))
if __name__ == '__main__':
    bench(without_pipeline)
    bench(with_pipeline)