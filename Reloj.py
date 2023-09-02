import datetime, time

while True:
    ahora = datetime.datetime.now()
    print(ahora.strftime("%H:%M:%S"),end="", flush=True)
    print("\r", end ="", flush=True)
    time.sleep(1)