import time
from multiprocessing.dummy import Pool

def async_function(name, surname):
    time.sleep(1)
    return name+" "+surname
    
def callback_function(name):
    print name


pool = Pool(processes=1)
pool.apply_async(
    async_function,
    args=['jeedau', 'helo'],
    callback=callback_function
)


pool.close()
pool.join()
