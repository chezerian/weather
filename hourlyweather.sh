date=$(date +%Y-%m-%d)
cd /home/chez/weather/scripts
curl 'http://www.bom.gov.au/fwo/IDN60801/IDN60801.94777.json' > '../centralcoast/IDN60801.94777.json'
curl 'http://www.bom.gov.au/fwo/IDN60903/IDN60903.94925.json' > '../canberra/IDN60903.94925.json'
python2.7 weather.py
sh gnuplot.sh
cat gnuplot.txt | gnuplot
mv $date.png /var/www/weather
