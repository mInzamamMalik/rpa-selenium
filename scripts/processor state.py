import psutil
import time
# with tqdm(total=100, desc='cpu%', position=1) as cpubar, tqdm(total=100, desc='ram%', position=0) as rambar:
#     while True:
#         rambar.n = psutil.virtual_memory().percent
#         cpubar.n = psutil.cpu_percent()
#         rambar.refresh()
#         cpubar.refresh()
#         sleep(0.5)

while True:
    time.sleep(1)
    cpu = psutil.cpu_percent()
    print(cpu)
    if(cpu > 50):
        print("cpu is high")