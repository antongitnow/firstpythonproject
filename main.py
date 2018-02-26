from icalendar import Calendar, Event
from datetime import datetime, timedelta
from datetime import date
from datetime import time
from pytz import UTC # timezone
import urllib.request
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world(): 
   
   with open ("/Users/antonhavekes/python-docs-hello-world/agendaurl.txt", "r") as myfile:
    agendadata=myfile.read().replace('\n', '')

   local_filename, headers = urllib.request.urlretrieve(agendadata)
   g = open(local_filename)

   gcal = Calendar.from_ical(g.read())

   strTable = """
   <!DOCTYPE html>
   <html>
   <head>
   <style>
   table, th, td {
       border: 1px solid black;
       border-collapse: collapse;
       background-color:#202020;
       padding: 15px;
       font-size: 35px;
    
   }
   th, td {
    padding: 15px;
    text-align: left;
    border: 0px solid black;

   }
   tr {
    border: 5px solid black;
   }
   th {
     padding: 30px;
     text-align: center;
     font-size: 70px;
   }
    .desc td {
    color:#C8C8C8;
    

   }

   </style>

   <STYLE TYPE="text/css">
   <!--
   TD{font-family: Air Americana; font-size: 7}
    --->
   </STYLE>
   </head>
   strTable = strTable +"<body style='background-color:black'><table style='width:100%; color: white'><tr><th colspan='3'><font face='Air Americana'>Demo's vandaag</font></th></tr><tr><th  style='background-color:black' colspan='3'></th></tr>"


   """
   rowcount = 0

   for component in gcal.walk():
       if component.name == "VEVENT":
        
  
           summary = component.get('summary')      
           start = component.get('dtstart')
           description = component.get('description')
           location = component.get('location')
           sttime = start.dt
           sttime = sttime + timedelta(hours=1) #+1 uur tijdverschil
        
           if sttime.date() == datetime.today().date(): 

               if sttime.time() > datetime.today().time():
                   startdemo = str(sttime.strftime('%H:%M'))
                
                   strRW1 = "<tr><td width='20%'>"+startdemo+"</td><td width='55%'>"+summary+"</td><td width='25%'>"+location+"</td></tr>"
                   strRW2 = "<tr><td class=desc colspan='3' STYLE='font-size: 25px; color: #C8C8C8;'>"+description+"</td></tr>"
                   strTable = strTable+strRW1+strRW2
                   rowcount = rowcount + 1
                   print(summary +":" +location)
           
   if rowcount == 0:
       strRW0 = "<tr><td colspan='3'>No sprintdemo's today</td></tr>"
       strTable = strTable+strRW0


   g.close()
   strTable = strTable+"</table>hi!!</body></html>"
   eenvar = 'testtesttest'
   return strTable

if __name__ == '__main__':
  app.run()

