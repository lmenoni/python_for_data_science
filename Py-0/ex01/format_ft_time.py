
import time
import datetime

secs_from_epoch = time.time()

print(f"Seconds since January 1, 1970 {secs_from_epoch:.4f} or {secs_from_epoch:.2e} in scientific notation")

today = datetime.date.today()
print(today.strftime("%b %d %Y"))