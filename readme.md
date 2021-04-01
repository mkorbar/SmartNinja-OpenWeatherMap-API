# Namestitev
Po namestitvi ustari še datoteko `secrets.py`, ki vsebuje sledečo kodo

```python
#
# Never commit this file to git !!!!!
#
import os

os.environ["OPEN_WEATHER_MAP_API_KEY"] = "<<<==TU=VSTAVI=SVOJ=API=KLJUC==>>>"
```