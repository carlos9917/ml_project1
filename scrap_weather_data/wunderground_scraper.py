#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 11:25:38 2020

@author: bojanstavrikj

https://bojanstavrikj.github.io/content/page1/wunderground_scraper
"""

from bs4 import BeautifulSoup as BS
from selenium import webdriver
from functools import reduce
import pandas as pd
import time
import os
import sys
#Set the path for your chromedriver file
try:
    CHROME=os.environ["CHROME_DRIVER"]
except:
    print("Chrome driver not found!")
    print("Plese download appropriate driver from")
    download_driver="https://chromedriver.chromium.org/downloads"
    print(download_driver)
    print("and set variable CHROME_DRIVER to the appropriate path")
    sys.exit(1)

# function to load wunderground data (without this it has no records to show)
def render_page(url):
    #driver = webdriver.Chrome(CHROME) # 'path_to/chromedriver')
    from selenium.webdriver.chrome.options import Options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(CHROME,options=chrome_options)

    driver.get(url)
    time.sleep(3)
    r = driver.page_source
    driver.quit()
    return r


# function to scrape wunderground
def scraper(page, dates):
    output = pd.DataFrame()

    for d in dates:

        url = str(str(page) + str(d))

        r = render_page(url)

        soup = BS(r, "html.parser")
        container = soup.find('lib-city-history-observation')
        check = container.find('tbody')

        data = []

        for c in check.find_all('tr', class_='ng-star-inserted'):
            for i in c.find_all('td', class_='ng-star-inserted'):
                trial = i.text
                trial = trial.strip('  ')
                data.append(trial)
        if round(len(data) / 17 - 1) == 31:
            Temperature = pd.DataFrame([data[32:128][x:x + 3] for x in range(0, len(data[32:128]), 3)][1:],
                                       columns=['Temp_max', 'Temp_avg', 'Temp_min'])
            Dew_Point = pd.DataFrame([data[128:224][x:x + 3] for x in range(0, len(data[128:224]), 3)][1:],
                                     columns=['Dew_max', 'Dew_avg', 'Dew_min'])
            Humidity = pd.DataFrame([data[224:320][x:x + 3] for x in range(0, len(data[224:320]), 3)][1:],
                                    columns=['Hum_max', 'Hum_avg', 'Hum_min'])
            Wind = pd.DataFrame([data[320:416][x:x + 3] for x in range(0, len(data[320:416]), 3)][1:],
                                columns=['Wind_max', 'Wind_avg', 'Wind_min'])
            Pressure = pd.DataFrame([data[416:512][x:x + 3] for x in range(0, len(data[416:512]), 3)][1:],
                                    columns=['Pres_max', 'Pres_avg', 'Pres_min'])
            Date = pd.DataFrame(data[:32][1:], columns=data[:1])
            Precipitation = pd.DataFrame(data[512:][1:], columns=['Precipitation'])
            print(str(str(d) + ' finished!'))
        elif round(len(data) / 17 - 1) == 28:
            Temperature = pd.DataFrame([data[29:116][x:x + 3] for x in range(0, len(data[29:116]), 3)][1:],
                                       columns=['Temp_max', 'Temp_avg', 'Temp_min'])
            Dew_Point = pd.DataFrame([data[116:203][x:x + 3] for x in range(0, len(data[116:203]), 3)][1:],
                                     columns=['Dew_max', 'Dew_avg', 'Dew_min'])
            Humidity = pd.DataFrame([data[203:290][x:x + 3] for x in range(0, len(data[203:290]), 3)][1:],
                                    columns=['Hum_max', 'Hum_avg', 'Hum_min'])
            Wind = pd.DataFrame([data[290:377][x:x + 3] for x in range(0, len(data[290:377]), 3)][1:],
                                columns=['Wind_max', 'Wind_avg', 'Wind_min'])
            Pressure = pd.DataFrame([data[377:464][x:x + 3] for x in range(0, len(data[377:463]), 3)][1:],
                                    columns=['Pres_max', 'Pres_avg', 'Pres_min'])
            Date = pd.DataFrame(data[:29][1:], columns=data[:1])
            Precipitation = pd.DataFrame(data[464:][1:], columns=['Precipitation'])
            print(str(str(d) + ' finished!'))
        elif round(len(data) / 17 - 1) == 29:
            Temperature = pd.DataFrame([data[30:120][x:x + 3] for x in range(0, len(data[30:120]), 3)][1:],
                                       columns=['Temp_max', 'Temp_avg', 'Temp_min'])
            Dew_Point = pd.DataFrame([data[120:210][x:x + 3] for x in range(0, len(data[120:210]), 3)][1:],
                                     columns=['Dew_max', 'Dew_avg', 'Dew_min'])
            Humidity = pd.DataFrame([data[210:300][x:x + 3] for x in range(0, len(data[210:300]), 3)][1:],
                                    columns=['Hum_max', 'Hum_avg', 'Hum_min'])
            Wind = pd.DataFrame([data[300:390][x:x + 3] for x in range(0, len(data[300:390]), 3)][1:],
                                columns=['Wind_max', 'Wind_avg', 'Wind_min'])
            Pressure = pd.DataFrame([data[390:480][x:x + 3] for x in range(0, len(data[390:480]), 3)][1:],
                                    columns=['Pres_max', 'Pres_avg', 'Pres_min'])
            Date = pd.DataFrame(data[:30][1:], columns=data[:1])
            Precipitation = pd.DataFrame(data[480:][1:], columns=['Precipitation'])
            print(str(str(d) + ' finished!'))
        elif round(len(data) / 17 - 1) == 30:
            Temperature = pd.DataFrame([data[31:124][x:x + 3] for x in range(0, len(data[31:124]), 3)][1:],
                                       columns=['Temp_max', 'Temp_avg', 'Temp_min'])
            Dew_Point = pd.DataFrame([data[124:217][x:x + 3] for x in range(0, len(data[124:217]), 3)][1:],
                                     columns=['Dew_max', 'Dew_avg', 'Dew_min'])
            Humidity = pd.DataFrame([data[217:310][x:x + 3] for x in range(0, len(data[217:310]), 3)][1:],
                                    columns=['Hum_max', 'Hum_avg', 'Hum_min'])
            Wind = pd.DataFrame([data[310:403][x:x + 3] for x in range(0, len(data[310:403]), 3)][1:],
                                columns=['Wind_max', 'Wind_avg', 'Wind_min'])
            Pressure = pd.DataFrame([data[403:496][x:x + 3] for x in range(0, len(data[403:496]), 3)][1:],
                                    columns=['Pres_max', 'Pres_avg', 'Pres_min'])
            Date = pd.DataFrame(data[:31][1:], columns=data[:1])
            Precipitation = pd.DataFrame(data[496:][1:], columns=['Precipitation'])
            print(str(str(d) + ' finished!'))
        else:
            print('Data not in normal length')

        dfs = [Date, Temperature, Dew_Point, Humidity, Wind, Pressure, Precipitation]

        df_final = reduce(lambda left, right: pd.merge(left, right, left_index=True, right_index=True), dfs)

        df_final['Date'] = str(d) + "-" + df_final.iloc[:, :1].astype(str)

        output = output.append(df_final)

    print('Scraper done!')

    output = output[['Temp_avg', 'Temp_min', 'Dew_max', 'Dew_avg', 'Dew_min', 'Hum_max',
                     'Hum_avg', 'Hum_min', 'Wind_max', 'Wind_avg', 'Wind_min', 'Pres_max',
                     'Pres_avg', 'Pres_min', 'Precipitation', 'Date']]

    return output

if __name__=="__main__":
    from datetime import datetime as dt
    year="2021"
    #dates = ['2019-4', '2019-5']
    #Select month. It will print only last day at the end
    dates = [dt.strftime(dt.today(),"%Y-%m")]
    print(dates)
    #Chievres station
    pages={"daily":"https://www.wunderground.com/history/daily/EBCI/date/",
           "monthly":"https://www.wunderground.com/history/monthly/EBCI/date/date"}
    
    #This one not working!
    #date=[dt.strftime(dt.today(),"%Y-%m-%d")]
    #df = scraper(pages["daily"], date)
    
    #Is using monthly, use the "dates" list
    df = scraper(pages["monthly"], dates)
    
    cols=["Temp_avg","Hum_avg","Wind_avg","Pres_avg","Date"]
    dict_out={"Date":"date","Temp_avg":"T_out","Hum_avg":"RH_out",
            "Dew_avg":"Tdewpoint",
               "Wind_avg":"Windspeed","Pres_avg":"Press_mm_hg"}
    from collections import OrderedDict
    
    out=OrderedDict()
    #change units!!!!
    #Time	Temperature (° F)	Dew Point (° F)	Humidity (%)	Wind Speed (mph)	Pressure (Hg)	Precipitation (in)
    for key in dict_out.keys():
        if key  in ["Temp_avg","Dew_avg"]: #F to C
            val_F = float(df.tail(1)[key].values[0])
            out[dict_out[key]] = (val_F - 32)*5/9
        elif key  == "Pres_avg":
            val_Hg = float(df.tail(1)[key].values[0])
            out[dict_out[key]] = val_Hg*25.4 #Hg to mm hg
        elif key=="Wind_avg":
            val_mph = float(df.tail(1)[key].values[0])
            out[dict_out[key]] = val_mph/2.237 #mph to m/s
        else:
            out[dict_out[key]] = df.tail(1)[key].values[0]
    today = dt.strftime(dt.today(),"%Y-%m-%d")
    print(f"Weather input for {today} (Visibility not found in this link, sorry)")
    print("{")
    for key in out.keys():
        print(f"{key} : {out[key]},")
    print("}")
    df_out = pd.DataFrame(out,index=[0])
    df_out.to_csv("weather_data.csv",index=False)
    #print(out)
    #df_out=pd.DataFrame(out)
