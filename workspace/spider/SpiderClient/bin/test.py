import mechanize
p = '212.19.8.185:80'

brow = mechanize.Browser()

brow.set_proxies({'http':p,'https':p})

print brow.open('http://www.tripsta.cn/flights/results?dep=PEK&arr=CDG&isRoundtrip=0&obDate=12%2F10%2F2016&ibDate=29%2F12%2F2015&obTime=&ibTime=&extendedDates=0&resetStaticSearchResults=1&passengersAdult=2&passengersChild=0&passengersInfant=0&airlineCode=&class=Y&directFlightsOnly=0').read()
