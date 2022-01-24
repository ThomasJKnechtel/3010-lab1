import pandas
import sqlite3
import matplotlib.pyplot as plt
import matplotlib.dates as mpl_dates
from datetime import datetime
conn=sqlite3.connect('sensorDB.db')
data = pandas.read_sql_query('SELECT * FROM sensordata',conn, parse_dates={'date':'%Y-%m-%d %H:%M:%S.%f'})


fig, ax1 = plt.subplots()
ax1.set_xlabel('Time') 
ax1.set_ylabel('Temperature(C) Humidity (%)')
ax2 = ax1.twinx() 
  
ax2.set_ylabel('Pressure (millibars)')

ax1.set_ylim(0,50);
ax1.plot_date(data['date'], data['temperature'], label='temperature' )
ax1.plot_date(data['date'], data['humidity'], label='humidity' )
ax2.set_ylim(800,1000);
ax2.plot_date(data['date'], data['pressure'],label='pressure', color='brown' )

plt.gcf().autofmt_xdate
date_format =mpl_dates.DateFormatter('%H:%M:%S')
ax1.legend()
ax2.legend()
plt.gca().xaxis.set_major_formatter(date_format)

plt.show()