from time import sleep
from redis import Redis

def disp_message(message):
    data = message['data']
    channel = message['channel'].decode('utf-8')

    try:
        data = data.decode('utf-8')
    except (UnicodeDecodeError, AttributeError):
        pass
        
    print("New pub on", channel, '->', data)

if __name__ == "__main__":
    red = Redis(host='localhost', port='6379')
    
    flux = red.pubsub()
    flux.psubscribe(**{'news:*':disp_message})
    thread = flux.run_in_thread(sleep_time=0.01)
    
    # Publish messages, the thread will receive them
    sleep(1)
    red.publish('news:fr', "Emmanuel Macron est élu président !")
    sleep(2)
    red.publish('news:us', "Joe Biden is the new president!")
    sleep(1)
    red.publish('news:us', "Not what Trump says...")
    
    sleep(1)
    thread.stop()