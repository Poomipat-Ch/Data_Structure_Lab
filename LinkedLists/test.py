import time
import sys
import os
start_time = time.time()
os.system("python "+sys.argv[1]+" "+" ".join(sys.argv[2:]))
print(f"--- {time.time() - start_time:.3f} seconds ---")