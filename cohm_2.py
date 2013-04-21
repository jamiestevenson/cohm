import csv
import converter
import sys

print "Welcome to COHM"

sourcecsv = raw_input("What is the name of the master (.csv) file?")

start_lat = raw_input("Input starting LAT:")
start_long = raw_input("Input starting LONG:")
course_length = raw_input("Input total course length in metres:")

dist_needed = 0

start_lat = float(start_lat)
start_long = float(start_long)
course_length = float(course_length)
middle_sum = 0

last_latitude = float(start_lat)
last_longditude = float(start_long)

new_path_coordinates = [[start_lat, start_long]]

with open(sourcecsv , 'r') as csvfile:
	curiosity_course = csv.reader(csvfile, delimiter = ',', quotechar = '"')
	print(csvfile.closed)

	for row in curiosity_course:
		try:
			print('Last: ', last_latitude, last_longditude, row[2], row[1])
			
			new_latitude, new_longditude = converter.translateWaypoint(last_latitude, last_longditude, row[2], row[1])

			last_latitude = new_latitude
			last_longditude = new_longditude			

			print('New: ', new_latitude, new_longditude)
			new_path_coordinates.append([new_latitude, new_longditude])

		except:
			print('Exception occured!')
			e = sys.exc_info()[0]
			print( "<p>Error: %s</p>" % e )

print(new_path_coordinates)
