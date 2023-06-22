from datetime import datetime
hh, mm = map(int, input().split())
start_time = datetime(year=2022, month=1, day=1, hour=9)
end_time = datetime(year=2022, month=1, day=1, hour=hh, minute=mm)
consumed_time = end_time - start_time
print(consumed_time.seconds // 60)
