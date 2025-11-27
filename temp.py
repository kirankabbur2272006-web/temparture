
import sys

if len(sys.argv) >= 3:
  script_name = sys.argv[0]
  temp = sys.argv[1]
else:
  script_name = sys.argv[0]
  temp = 25
if temp < 15:
  print("Cold (below 15°C)")
elif 15 <=temp <= 30:
  print("Normal (15°C to 30°C)")
else:
  print("Hot (above 30°C)")
