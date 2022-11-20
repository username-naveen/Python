#crop_recommendation
import pickle
import json
from time import sleep
import time
import time
import board
import adafruit_dht
import psutil
import urllib.request
import json
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

for proc in psutil.process_iter():
    if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
        proc.kill()
sensor = adafruit_dht.DHT11(board.D23)


CLK  = 11
MISO = 9
MOSI = 10
CS   = 22
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)
filename_crop = 'crop_train.sav'

while True:
    try:
        te = sensor.temperature
        hu = sensor.humidity
        if te>0:
            break
        print("Temperature: {}*C   Humidity: {}% ".format(te, hu))
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        sensor.exit()
        raise error
    time.sleep(2.0)


# ra=mcp.read_adc(1)
loaded_model_crop = pickle.load(open(filename_crop, 'rb'))

ni=float(input("ENTER INPUT FOR NITROGEN: "))
ps=float(input("ENTER INPUT FOR PHOSPORUS: "))
po=float(input("ENTER INPUT FOR POTASSIUM: "))
ph=float(input("ENTER INPUT FOR PH: "))
ra=float(input("ENTER INPUT FOR RAINFALL: "))

person_reports_crop = [[ni,ps,po,te,hu,ph,ra]]
print(ni)
print(ps)
print(po)
print(te)
print(hu)
print(ph)
print(ra)
crop_predicted = loaded_model_crop.predict(person_reports_crop)
print("ANALYSING....")
print(crop_predicted)

crop_recommend = [ni, ps, po, te, hu, ph, ra, crop_predicted]
# crop="https://api.thingspeak.com/update?api_key=A7CQV2WFBIE8PAPQ&field1="+str(ni)+"&field2="+str(ps)+"&field3="+str(po)+"&field4="+str(te)+"&field5="+str(hu)+"&field6="+str(ph)+"&field7="+str(ra)+"&field8="+str(crop_predicted)
# conn = urllib.request.urlopen(crop)
# response = conn.read()


#rainfall

# import pickle
# import json
# from time import sleep
# import time
# import time
# import board
# import adafruit_dht
# import psutil
# import urllib.request
# import json
# import Adafruit_GPIO.SPI as SPI
# import Adafruit_MCP3008

# for proc in psutil.process_iter():
#     if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
#         proc.kill()
# sensor = adafruit_dht.DHT11(board.D23)


# CLK  = 11
# MISO = 9
# MOSI = 10
# CS   = 22
# mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)
filename_fall = 'fall_train.sav'

# while True:
#     try:
#         d = sensor.temperature
#         e = sensor.humidity
#         if d>0:
#             break
#         print("Temperature: {}*C   Humidity: {}% ".format(temp, humidity))
#     except RuntimeError as error:
#         print(error.args[0])
#         time.sleep(2.0)
#         continue
#     except Exception as error:
#         sensor.exit()
#         raise error
#     time.sleep(2.0)



loaded_model_fall = pickle.load(open(filename_fall, 'rb'))


mon=float(input("ENTER MONTH "))
da=float(input("ENTER DAY "))

vi=float(input("ENTER INPUT FOR VISIBLITY "))
aw=float(input("ENTER INPUT FOR AVERAGE WIND "))
person_reports_fall = [[mon,da,te,hu,vi,aw]]
print(te)
print(hu)
print(vi)
print(aw)
rain = loaded_model_fall.predict(person_reports_fall)
print("ANALYSING....")
if int(rain[0])==0:
  print("No_Rain_Fall")
  t="No_Rain_Fall" 
else:
  print("Possiblities_for_rain_today")
  t="Possiblities_for_rain_today"

print(t)

rain_predict = [mon, da, te, hu, vi, aw, t]
# rain_fall="https://api.thingspeak.com/update?api_key=A7CQV2WFBIE8PAPQ&field9="+str(mon)+"&field10="+str(da)+"&field11="+str(te)+"&field12="+str(hu)+"&field13="+str(vi)+"&field14="+str(aw)+"&field15="+str(t)
# conn = urllib.request.urlopen(rain_fall)
# response = conn.read()

#agri rating

# import pickle
# import json
# from time import sleep
# import time
# import time
# import board
# import adafruit_dht
# import psutil
# import urllib.request
# import json
# import Adafruit_GPIO.SPI as SPI
# import Adafruit_MCP3008

# for proc in psutil.process_iter():
#     if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
#         proc.kill()
# sensor = adafruit_dht.DHT11(board.D23)


# CLK  = 11
# MISO = 9
# MOSI = 10
# CS   = 22
# mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)
filename_rate = 'rating_train.sav'

# while True:
#     try:
#         d = sensor.temperature
#         e = sensor.humidity
#         if d>0:
#             break
#         print("Temperature: {}*C   Humidity: {}% ".format(temp, humidity))
#     except RuntimeError as error:
#         print(error.args[0])
#         time.sleep(2.0)
#         continue
#     except Exception as error:
#         sensor.exit()
#         raise error
#     time.sleep(2.0)

ai=mcp.read_adc(0)
mo=mcp.read_adc(1)
loaded_model_rate = pickle.load(open(filename_rate, 'rb'))



# f=float(input("ENTER PH "))

person_reports_rate = [[te,hu,ph,ai,mo]]
print(te)
print(hu)
print(ph)
print(ai)
print(mo)
rating = loaded_model_rate.predict(person_reports_rate)
print("ANALYSING....")

agri = [te, hu, ph, ai, mo, rating]
# print(rating)
# agri="https://api.thingspeak.com/update?api_key=A7CQV2WFBIE8PAPQ&field16="+str(te)+"&field17="+str(hu)+"&field18="+str(ph)+"&field19="+str(ai)+"&field20="+str(mo)+"&field21="+str(rating)
# conn = urllib.request.urlopen(agri)
# response = conn.read()


# m="https://api.thingspeak.com/update?api_key=A7CQV2WFBIE8PAPQ&field1="+str(ni)+"&field2="+str(ps)+"&field3="+str(po)+"&field4="+str(te)+"&field5="+str(hu)+"&field6="+str(ph)+"&field7="+str(ra)+"&field8="+str(crop_predicted)+"&field9="+str(mon)+"&field10="+str(da)+"&field11="+str(te)+"&field12="+str(hu)+"&field13="+str(vi)+"&field14="+str(aw)+"&field15="+str(t)+"&field16="+str(te)+"&field17="+str(hu)+"&field18="+str(ph)+"&field19="+str(ai)+"&field20="+str(mo)+"&field21="+str(rating)

m="https://api.thingspeak.com/update?api_key=A7CQV2WFBIE8PAPQ&field1="+crop_recommend+"&field2="+rain_predict+"&field3="+agri
conn = urllib.request.urlopen(m)
response = conn.read()