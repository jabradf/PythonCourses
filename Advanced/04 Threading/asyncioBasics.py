import time
import asyncio

# ensure the function has 'async' in front of def
async def greeting_with_sleep_async(string):
  s = time.perf_counter()
  print(string)
  await asyncio.sleep(2)
  #time.sleep(2)
  print("says hello!")
  elapsed = time.perf_counter() - s
  print("Asyncio Elapsed Time: " + str(elapsed) + " seconds")

loop = asyncio.get_event_loop()
#loop.run_until_complete(greeting_with_sleep_async('Codecademy'))   # <3.7 version
asyncio.run(greeting_with_sleep_async('Codecademy'))    # >3.7
# for python 3.7+ use: asyncio.run(hello_async)