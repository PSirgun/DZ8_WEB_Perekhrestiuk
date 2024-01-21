import argparse
from models import Quote, Author
import connect
import json
import subprocess
import redis
from redis_lru import RedisLRU

#-----------------------------------------------------------------------------------------------------
subprocess.run('docker run --name redis-cache -d -p 6379:6379 redis')
subprocess.run('docker start redis-cache')

client = redis.StrictRedis(host="localhost", port=6379, password=None)
cache = RedisLRU(client, default_ttl=5*60)

#-----------------------------------------------------------------------------------------------------
@cache
def main():
    while True:
        print ('name <authors name>, tag <tag>, tags <tag1,tag2>')
        command = input(">>>")

        if command.startswith("name "):

            author_name = command.split("name ")[1]
            
            author = Author.objects(name__icontains=author_name).first()
            if author:
                quotes = Quote.objects(author=author)
                for quote in quotes:
                    print(quote.quote)
            else:
                print("not found")

        elif command.startswith("tag "):
            tag = command.split("tag ")[1]
            quotes = Quote.objects(tags__icontains=tag)
            for quote in quotes:
                
                print(quote.quote)

        elif command.startswith("tags "):
            tags = command.split("tags ")[1].split(",")
            quotes = Quote.objects(tags__in=tags)
            for quote in quotes:
                
                print(quote.quote)

        elif command == "exit":
            break

        else:
            print("wrong input")


if __name__ == '__main__':
    main()