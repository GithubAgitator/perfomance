from redis import Redis

cashe = Redis(host="redis", port="6379")
cashe.incr("times", amount=1)
print(cashe.get("times"))
