import matplotlib.pyplot as plt
import sqlite3
from datetime import datetime

#def generate_chart(location, variable, start_date, end_date):
	#open db
location="gosford"
variable="air_temp"
start_date="0000000000000"
end_date="20140530000000"

var_list= ("wind_dir","lat","gust_kt","local_date_time_full","press_msl","wind_spd_kmh","lon","wmo int","press_qnh","wind_spd_kt","rain_trace","aifstime_utc","delta_t","press_tend","rel_hum","local_date_time","press","vis_km","air_temp","gust_kmh","dewpt","apparent_t")

conn=sqlite3.connect("$PATH/weather.db")
c=conn.cursor()

c.execute("SELECT name FROM sqlite_master WHERE type='table';")
table_list=zip(*c.fetchall())[0]

#check that the location they want eists, this is a table name so it will screw up badly if it doesnt
if location not in table_list or variable not in var_list:
	print("Error")

#also need to check that the variable in question eists, also some variable e.g. swell exists only for certain locations, this should be checked later on
#problems occur when trying to plot null values
#select records, this will have to accept variables for the field selected, the table (location) and the times
c.execute("SELECT "+variable+",local_date_time_full	FROM "+location+" WHERE local_date_time_full > ? AND local_date_time_full < ? ORDER BY local_date_time_full", (start_date, end_date) )

#store the selected results			
results=c.fetchall()

#print results[1][0]
#somecheck in case no results are returned will run into problems when trying to change to date time

#transpose and turn into list
results_list=map(list,zip(*results))

#print len(results_list[0])
#print (results_list[0][0:5])

#print(results_list[0][2])

#convert to date time format, useful when making a chart, possibly include a new field in the db rather than convert it each time
for i in range(len(results_list[1])):
	results_list[1][i]=datetime.strptime(results_list[1][i],'%Y%m%d%H%M%S')

#plot the results needs work on the labelling and need a way to get multiple lines e.g. multiple locations
plt.plot(results_list[1],results_list[0])
plt.savefig("$PATH/weather.png",dpi=400)
plt.close()
conn.close()

#	return plt.plot
