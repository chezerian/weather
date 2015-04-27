import urllib2
import httplib
import json
import StringIO
import gzip
import sqlite3


conn=sqlite3.connect("$PATH/weather.db")
c=conn.cursor()
stations=["IDN60801.94596","IDN60801.94599","IDN60801.94573","IDN60801.94592","IDN60801.94598","IDN60801.95571","IDN60801.95570","IDN60801.94571","IDN60801.94572","IDN60801.94586","IDN60801.94582","IDN60801.94589","IDN60801.94791","IDN60801.94789","IDN60801.95778","IDN60801.94788","IDN60801.94785","IDN60801.94783","IDN60801.94786","IDN60801.94790","IDN60801.95784","IDN60801.95771","IDN60801.94782","IDN60801.94739","IDN60801.95767","IDN60801.95775","IDN60801.95774","IDN60801.95754","IDN60801.94756","IDN60801.95747","IDN60801.95779","IDN60801.94774","IDN60801.94781","IDN60801.95770","IDN60801.95758","IDN60801.94733","IDN60801.94775","IDN60801.94776","IDN60801.94773","IDN60801.95773","IDN60801.94588","IDN60801.94772","IDN60801.95541","IDN60801.94541","IDN60801.94553","IDN60801.94587","IDN60801.94556","IDN60801.94752","IDN60801.94765","IDN60801.94755","IDN60801.94757","IDN60801.94766","IDN60801.94769","IDN60801.95761","IDN60801.94760","IDN60801.95756","IDN60801.94780","IDN60801.95757","IDN60801.95768","IDN60801.94764","IDN60801.94763","IDN60801.94736","IDN60801.95753","IDN60801.95764","IDN60801.94767","IDN60801.94768","IDN60801.95766","IDN60801.95765","IDN60801.94759","IDN60801.95752","IDN60801.95748","IDN60801.94749","IDN60801.94747","IDN60801.95749","IDN60801.94746","IDN60801.94750","IDN60801.95940","IDN60801.95745","IDN60801.94941","IDN60801.95931","IDN60801.94933","IDN60801.94934","IDN60801.95929","IDN60801.94939","IDN60801.95937","IDN60801.94937","IDN60801.95935","IDN60801.94938","IDN60801.94730","IDN60801.94729","IDN60801.94732","IDN60801.94744","IDN60801.94741","IDN60801.94743","IDN60801.94727","IDN60801.94754","IDN60801.95735","IDN60801.95725","IDN60801.95726","IDN60801.95744","IDN60801.94927","IDN60801.94909","IDN60801.94926","IDN60801.94716","IDN60801.95716","IDN60801.95925","IDN60801.94943","IDN60801.94735","IDN60801.94925","IDN60801.95723","IDN60801.94928","IDN60801.94929","IDN60801.95916","IDN60801.94923","IDN60801.94921","IDN60801.94915","IDN60801.95909","IDN60801.95908","IDN60801.94761","IDN60801.94530","IDN60801.95740","IDN60801.95527","IDN60801.94520","IDN60801.95734","IDN60801.94544","IDN60801.95746","IDN60801.95762","IDN60801.95715","IDN60801.94792","IDN60801.95708","IDN60801.94728","IDN60801.95728","IDN60801.95718","IDN60801.95721","IDN60801.95719","IDN60801.95727","IDN60801.94715","IDN60801.94725","IDN60801.95707","IDN60801.94708","IDN60801.95717","IDN60801.94721","IDN60801.94704","IDN60801.95722","IDN60801.95710","IDN60801.94723","IDN60801.95709","IDN60801.94709","IDN60801.94714","IDN60801.94890","IDN60801.94919","IDN60801.94918","IDN60801.94712","IDN60801.95896","IDN60801.95895","IDN60801.95869","IDN60801.95704","IDN60801.94698","IDN60801.94702","IDN60801.94700","IDN60801.94901","IDN60801.95706","IDN60801.94843","IDN60801.94877","IDN60801.94910","IDN60801.95705","IDN60801.94862","IDN60801.94696","IDN60801.94689","IDN60801.94691","IDN60801.95697","IDN60801.94692","IDN60801.94694","IDN60801.94693","IDN60801.95692","IDN60801.94703","IDN60801.95512","IDN60801.94711","IDN60801.94710","IDN60801.95520","IDN60801.94686","IDN60801.94498","IDN60801.94485","IDN60801.95485","IDN60801.94497","IDN60801.95699","IDN60801.94695","IDN60801.95695","IDN60801.94995","IDN60801.95995","IDN60801.94996"]

def unzip(opener):
	if opener.headers.get("content-encoding")=="gzip":
		compresseddata = opener.read()                              
		#print(len(compresseddata))


		compressedstream = StringIO.StringIO(compresseddata)   

		gzipper = gzip.GzipFile(fileobj=compressedstream)      
		data = gzipper.read()                                  
		return data
		#print(data)
	else:
		data = opener.read()
		return data
		#print(data)


#print(len(data))

#download page, unzip it, read it into json, create table based on "name", 

for station in stations:
	#print station
	page=access_bom(station)
	json_data=json.loads(unzip(page))
	table_name=json_data["observations"]["header"][0]["name"].replace("-","").replace(" ","_").lower()
	#print table_name
	c.execute("CREATE TABLE IF NOT EXISTS " +table_name + "			(swell_period text,wind_dir text, lat real, cloud_oktas text, gust_kt real,history_product text, local_date_time_full text,	cloud text,press_msl real, cloud_type text, wind_spd_kmh real, lon real, swell_height text, wmo int, press_qnh real, weather text,wind_spd_kt real, rain_trace real, aifstime_utc text unique, delta_t real, press_tend text, rel_hum real, local_date_time text, press real,vis_km real, sea_state text , air_temp real, name text, cloud_base_m text, cloud_type_id text, gust_kmh real, dewpt real, swell_dir_worded text, sort_order int,apparent_t real)")
	#transform the dictionary into a list to insert into database
	insert=[]
	for i in range(len(json_data["observations"]["data"])):
		insert.append([v for k,v in json_data["observations"]["data"][i].items()])
	#print insert[1][23]
	c.executemany("INSERT OR IGNORE INTO "+table_name+ " VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", insert)
	conn.commit()


conn.close()
