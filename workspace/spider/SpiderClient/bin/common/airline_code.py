#coding:utf-8
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

Airline_2_Code = {
"9 Air":'AQ',
"AAC Angola Air Charter":'C3',
"ABSA Cargo Airline":'M3',
"ADA Air":'ZY',
"ALS":'K4',
"AOM French Airlines":'IW',
"ASA Atlantic Southeast Airlines":'EV',
"AVIACSA":'6A',
"AVIANCA":'AV',
"AVIOR":'3B',
"Accesrail Inc.":'9B',
"Accessair":'ZA',
"Acvila Air":'WZ',
"Adam Skyconnection":'1A',
"Adria Airways":'JP',
"Aegean Airlines":'A3',
"Aer Arann Express":'RE',
"Aer Arann":'1I',
"Aer Lingus":'EI',
"Aero Airlines A.S.":'EE',
"Aero Asia International":'E4',
"Aero Benin":'1M',
"Aero California":'JR',
"Aero Caribbean":'CRN',
"Aero Continente":'N6',
"Aero Contractors Company of Nigeria Ltd.":'AJ',
"Aero Contractors":'NG',
"Aero Lloyd":'YP',
"Aero-tropics Air Services":'HC',
"Aerocaribe":'QA',
"Aerocondor":'2B',
"Aeroexo":'SX',
"Aeroflot":'SU',
"Aerolineas Argentinas":'AR',
"Aerolineas Galapagos S.A. Aerogal":'2K',
"Aerolineas Internacionales":'N2',
"Aerolineas de Baleares AeBal":'DF',
"Aerolitoral":'5D',
"Aeromar":'VW',
"Aeromexico":'AM',
"Aeromexpress":'3F',
"Aeroperu":'PL',
"Aeropostale":'ARP',
"Aerosucre":'6N',
"Aerosur":'3M',
"Aerosur":'5L',
"Aerosvit Airlines":'3N',
"Aerosvit Airlines":'VV',
"Aerotransportes MAS de Carga":'MY',
"Afriqiyah Airways":'8U',
"Aigle Azur":'ZI',
"Air ALM":'LM',
"Air Afrique":'RK',
"Air Algérie":'AH',
"Air Alliance":'3J',
"Air Alpha Greenland A/S":'GD',
"Air Alps Aviation":'A6',
"Air Andaman Corporation Limited":'2Y',
"Air Arabia Egypt":'E5',
"Air Arabia Maroc":'3O',
"Air Arabia":'4J',
"Air Arabia":'G9',
"Air Armenia":'4K',
"Air Astana":'4L',
"Air Astana":'KC',
"Air Astana":'LQ',
"Air Atlanta Icelandic":'CC',
"Air Atlantic":'9A',
"Air Atlantique":'NL',
"Air Austral":'4R',
"Air Austral":'UU',
"Air BC":'ZX',
"Air Bagan":'4S',
"Air Berlin":'AB',
"Air Bosna":'4V',
"Air Bosna":'JA',
"Air Botswana":'BP',
"Air Bourbon":'4X',
"Air Bretagne":'3E',
"Air Burkina":'2J',
"Air Burkina":'VH',
"Air Burundi":'8Y',
"Air Burundi":'PB',
"Air Busan":'BX',
"Air Cairo":'SM',
"Air Caledonie":'TY',
"Air Canada Rouge":'RV',
"Air Canada":'AC',
"Air China Limited":'CA',
"Air City":'4F',
"Air Class Lineas Aereas (AEROVIP LTDA)":'QD',
"Air Club International":'HB',
"Air Corsica":'XK',
"Air Creedec":'YN',
"Air Do":'HD',
"Air Dolomiti":'EN',
"Air Engiadina":'RQ',
"Air Europa Lineas Aereas":'5S',
"Air Europa":'UX',
"Air Europe Italy":'PE',
"Air Europe":'5T',
"Air France":'AF',
"Air Gabon":'GN',
"Air Guadeloupe":'TX',
"Air Guinee":'GI',
"Air Gulf Falcon":'QL',
"Air Holland Charter":'GG',
"Air Iceland":'NY',
"Air India Express":'IX',
"Air India":'AI',
"Air Inuit":'3H',
"Air Italy S.p.A.":'NN',
"Air Kazakstan":'9Y',
"Air Koryo":'JS',
"Air Labrador":'WJ',
"Air Liberte":'VO',
"Air Link Pty Ltd":'DR',
"Air Littoral":'FU',
"Air Macau":'NX',
"Air Madagascar":'MD',
"Air Malawi":'QM',
"Air Malta":'KM',
"Air Mandalay Ltd":'6T',
"Air Manitoba":'7N',
"Air Marshall Islands":'CW',
"Air Mauritanie":'MR',
"Air Mauritius":'MK',
"Air Micronesia Inc.":'ML',
"Air Moldova International":'RM',
"Air Moldova":'9U',
"Air Namibia":'SW',
"Air New Zealand":'NZ',
"Air Nippon":'EL',
"Air Niugini":'PX',
"Air North":'4N',
"Air Nostrum":'YW',
"Air Nova":'QK',
"Air One":'AP',
"Air Ontario":'GX',
"Air Ostrava":'8K',
"Air Philippines":'3G',
"Air Rarotonga":'GZ',
"Air SERBIA a.d. Beograd":'JU',
"Air Santo Domingo":'EX',
"Air Sao Tome e Principe":'KY',
"Air Seychelles":'HM',
"Air Sinai":'4D',
"Air South Airlines":'WV',
"Air St. Pierre":'PJ',
"Air Sunshine":'YI',
"Air Sweden":'PT',
"Air Tahiti Nui":'TN',
"Air Tahiti":'VT',
"Air Tanzania":'TC',
"Air Tindi Ltd":'8T',
"Air Togo S.A.":'YT',
"Air Toulouse International":'SH',
"Air Transat":'TS',
"Air Transport International":'8C',
"Air Ukraine":'6U',
"Air Vanuatu":'NF',
"Air Wisconsin":'ZW',
"Air Zaire":'QC',
"Air Zimbabwe":'UM',
"Air-Serv., Inc. dba Indigo":'I9',
"AirAsia India":'I5',
"AirAsia Philippines":'PQ',
"AirAsia X":'D7',
"AirAsia Zest":'Z2',
"AirAsia":'AK',
"AirBaltic":'BT',
"AirBridgeCargo Airlines":'RU',
"AirFreight Express":'5Z',
"AirTran Airways":'FL',
"Airborne Express":'GB',
"Aircalin":'SB',
"Airfast Indonesia":'AFE',
"Airkenya Aviation":'QP',
"Airlink Limited":'ND',
"Airlink":'4Z',
"Airtours International":'VZ',
"Airworld":'RL',
"Aklak Air":'6L',
"Alaska Airlines":'AS',
"Alaska Coastal":'7A',
"Albanian Airlines":'LV',
"Alitalia Team":'RD',
"Alitalia":'AZ',
"All Nippon Airways":'NH',
"Allegiant Air":'G4',
"Alliance Airlines":'3A',
"Alliance Airlines":'CD',
"Alpine Aviation":'5A',
"America West Airlines":'HP',
"American Airlines":'AA',
"American Eagle Airlines, Inc.":'MQ',
"American Falcon S.A.":'WK',
"American International":'CB',
"Americana de Aviation":'8A',
"Angel Airlines":'8G',
"Ansett Australia":'AN',
"Arca Colombia":'ZU',
"Arctic Transportation Services":'7S',
"Ariana Afghan Airlines":'FG',
"Arik Air":'W3',
"Arkia Israeli Airlines":'IZ',
"Armenian International Airlines":'R3',
"Asian Spirit":'6K',
"Asiana":'OZ',
"Aspiring Air":'OI',
"Astral Aviation, Inc.":'AL',
"Atlantic Airways Faroe Islands":'RC',
"Atlantic Coast Airlines":'DH',
"Atlantic Southeast Airlines":'C6',
"Atlas Air":'5Y',
"Atlasjet Airlines":'KK',
"Atyrau Airways":'IP',
"Augsburg Airways":'IQ',
"Aurigny Air Services":'GR',
"Austral":'AU',
"Austrian":'OS',
"Avia Air":'3R',
"Aviateca":'GU',
"Aviation Assistance A.S.":'7W',
"Aviation Enterprise TESIS Limited":'UZ',
"Axess International Network Inc.":'1J',
"Axon Airlines":'XN',
"Azerbaijan Airlines":'J2',
"Azul Brazilian Airlines":'AD',
"Azzurra Air":'ZS',
"Aéroservicios Carabobo":'R7',
"Aérovas Venezolanas":'VE',
"BAC Express Airlines":'RPX',
"BH AIR":'8H',
"Bahamasair":'UP',
"Bahrain Air":'BN',
"Balkan Bulgarian Airlines":'LZ',
"Bangkok Air":'PG',
"Baron Aviation Services":'BVN',
"Baseops International, Inc.":'3Y',
"Bearskin Airlines":'JV',
"Belavia - Belarusian Airlines":'B2',
"Bellview Airlines":'B3',
"Bemidji Airlines":'CH',
"Bering Air":'8E',
"Berjaya Air":'J8',
"Big Sky Airlines":'GQ',
"Biman Bangladesh Airlines":'BG',
"Binter Canarias":'NT',
"Binter Mediterraneo":'AX',
"Blue Air":'0B',
"Blue Panorama Airlines":'BV',
"Blue1":'KF',
"Bluebird Cargo":'BF',
"Boliviana de Aviación - BoA":'OB',
"Bouraq Indonesia Airlines":'BO',
"Braathens ASA":'BU',
"Brit Air":'DB',
"Britannia Airways AB":'6B',
"Britannia Airways":'BY',
"British Airways Cargo":'E9',
"British Airways":'BA',
"British International Helicopters":'UR',
"British Mediterranean Airways Limited":'KJ',
"British Midland Airways":'BD',
"British Regional Airlines Limited":'TH',
"British World Airlines":'VF',
"Brussels Airlines":'SN',
"Bulgaria air":'FB',
"Burlington Air Express":'8W',
"Business Air":'II',
"Business Aviation":'4P',
"C.A.L. Cargo Airlines":'5C',
"CC Air":'ED',
"COPA Airlines":'CM',
"CR Airways":'CR',
"Calm Air":'MO',
"Cameroon Airlines":'UY',
"Canada 3000 Airlines":'2T',
"Canadian Airlines International":'CP',
"Canadian Regional Airlines":'KI',
"Canadian Western Airlines":'W2',
"Cape Air":'9K',
"Cape Smythe Air Service Inc":'6C',
"Cargo Plus Aviation Inc.":'8L',
"Cargolux S.A.":'CV',
"Caribbean Airlines":'BW',
"Caribbean Star Airlines":'8B',
"Cathay Pacific":'CX',
"Cayman Airways":'KX',
"Cebu Pacific":'5J',
"Central Mountain Air Ltd.":'9M',
"Chalk's Ocean Airways":'OP',
"Champion Air":'MG',
"Chang-An Airlines":'2Z',
"Chautauqua Airlines":'CHQ',
"Chautauqua Airlines, Inc.":'RP',
"China Airlines":'CI',
"China Cargo Airlines":'CK',
"China Eastern":'MU',
"China Northwest Airlines":'WH',
"China Postal Airlines":'CF',
"China Southern Airlines":'CZ',
"China Southwest Airlines":'SZ',
"China United Airlines":'KN',
"China Yunnan Airlines":'3Q',
"Cimber Air":'QI',
"Citilink":'QG',
"CityJet":'WX',
"Coastal Air Transport.":'DQ',
"Colgan Air":'9L',
"Comair, Inc.":'OH',
"Commercial Airways":'CAW',
"Condor":'DE',
"Contact":'3T',
"Continental Airlines":'CO',
"Continental Micronesia, Inc.":'CS',
"Corendon Airlines":'XC',
"Corporate Air":'DN',
"Corporate Airlines":'3C',
"Corsair International":'SS',
"Cosmic Air Pvt. Ltd.":'F5',
"Crledonian Airways":'KG',
"Croatia Airlines":'OU',
"Crossair Europe":'QE',
"Cubana de Aviacion":'GW',
"Cubana":'CU',
"Cygnus Air":'XG',
"Cyprus Airways":'CY',
"Czech Airlines j.s.c":'OK',
"DAC Air":'GCP',
"DAS Air Limited":'WD',
"DHL Airways":'ER',
"Daallo Airlines":'D3',
"Dalavia-Far East Airways Khabarovsk":'H8',
"Danish Air Transport":'DX',
"Darwin Airline SA":'F7',
"Debonair":'2G',
"Delta Air Lines":'DL',
"Deutsche Bahn AG":'2A',
"Dominicana":'DO',
"Domodedovo Airlines":'HN',
"Donavia":'D9',
"Donbass - Eastern Ukrainian Airlines":'7D',
"Dragonair":'KA',
"Druk Air":'KB',
"EIK Airways":'S8',
"EVA Air":'BR',
"Eastar Jet":'ZE',
"Eastern Airways":'T3',
"EasyFly":'EF',
"EasyJet Switzerland":'DS',
"EasyJet":'U2',
"Ecoair":'9H',
"Egyptair":'MS',
"Emirates":'EK',
"Empire Airlines":'EM',
"Enkor Airlines":'G5',
"Era Aviation":'7H',
"Estonian Air":'OV',
"Ethiopian Airlines":'ET',
"Etihad Airways":'EY',
"Euralair International":'RN',
"Euroatlantic Airways":'YU',
"Eurocypria Airlines":'UI',
"Eurofly":'EEZ',
"Eurofly":'GJ',
"European Air Express":'7Y',
"European Air Transport":'QY',
"European Aviation Air Charter":'EAF',
"European Executive Express":'RY',
"European Regions Airlines":'EA',
"Eurostar":'9F',
"Eurowings":'EW',
"Evergreen International Airlines":'EZ',
"Excel Airways":'JN',
"Executive Airlines/American Eagle":'OW',
"Expo Aviation":'8D',
"Express Airlines":'9E',
"Express One Interational":'EO',
"Fair":'FW',
"Falcon Air":'IH',
"Famner Air Transport":'FAT',
"Fastjet":'FN',
"Federal Express":'FX',
"Felix Airways":'FO',
"Finnair":'AY',
"Firefly":'FY',
"First Air":'7F',
"Fischer Air":'8F',
"Flash Airlines":'7K',
"Florida West":'RF',
"Fly540":'5H',
"FlySafair":'FA',
"Flybe":'BE',
"Flydubai":'FZ',
"Flying Colours Airlines":'FLY',
"Flynas":'XY',
"Freebird Airlines":'FH',
"Frontier Airlines":'F9',
"GB Airways Ltd.":'GT',
"GB Airways":'GBL',
"GMG Airlines":'Z5',
"Gambia International Airlines":'GC',
"Garuda":'GA',
"Georgian Airlines":'6R',
"Georgian Airways":'A9',
"Germania":'GM',
"Germania":'ST',
"Germanwings":'4U',
"Gestair S.A.":'GP',
"Ghana Airways":'GH',
"GoAir":'G8',
"Gol Transportes Aéreos":'G3',
"Golden Air Flyg":'DC',
"Golden Myanmar Airlines":'Y5',
"Great American Airways":'MV',
"Great China Airlines":'IF',
"Great Lakes Aviation":'ZK',
"Guine Bissau Airlines":'G6',
"Gulf Air":'GF',
"Guyana Airways Corporation":'GY',
"HOP!":'A5',
"Hahn Air Systems":'H1',
"Hahn Air":'HR',
"Hainan Airlines":'HU',
"Hapag-Lloyd":'HF',
"Hawaiian Airlines":'HA',
"Hazelton Airlines":'ZL',
"Helgoland Airlines":'LE',
"Heli Air Monaco":'YO',
"Helijet International Inc":'JB',
"Helikopterservice Euro Air":'YQ',
"Helishuttle":'KH',
"Hemus Air":'DU',
"Hi Fly":'5K',
"Hong Kong Airlines":'HX',
"Hong Kong Express Airways":'UO',
"Horizon Air":'QX',
"Hunting Cargo Airlines":'AG',
"IBERIA":'IB',
"IRS Aero":'5R',
"Iberia Express":'I2',
"Icelandair":'FI',
"Imair":'IK',
"IndiGo":'6E',
"Indian Airlines":'IC',
"Indonesia AirAsia X":'XT',
"Indonesia AirAsia":'QZ',
"Intensive Air":'IM',
"Inter Tropical Aviation":'3P',
"Inter-Canadien":'QB',
"InterSky":'3L',
"Intercontinental de Aviatcion":'RS',
"Interjet":'4O',
"Iran Air":'IR',
"Iran Aseman Airlines":'EP',
"Iran Asseman":'Y7',
"Iraqi Airways":'IA',
"Ireland Airways":'EIX',
"Island Air":'WP',
"Island Airlines (US)":'IS',
"Island Express":'2S',
"Islands Nationair":'CN',
"Islena Airlines":'WC',
"Israir":'6H',
"Itapemirim Transportes Aereos S.A.":'LU',
"JAA":'EG',
"JAL Express":'JC',
"JAL Express":'N8',
"JMC Airlines Limited":'MT',
"JSC Nordavia-RA":'5N',
"Jalways":'JO',
"Jambojet":'JX',
"Japan Air Commuter":'3X',
"Japan Air System":'JD',
"Japan Airlines":'JL',
"Japan TransOcean Air":'NU',
"Jazeera Airways":'J9',
"Jeju Air":'7C',
"Jersey European Airways":'JY',
"Jet Airways Inc.":'QJ',
"Jet Airways":'9W',
"Jet Aviation Business Jets AG":'PP',
"Jet Lite (India) Limited":'S2',
"Jet2.com":'LS',
"JetBlue":'B6',
"Jetstar Asia":'3K',
"Jetstar Hong Kong":'JM',
"Jetstar Japan":'GK',
"Jetstar Pacific":'BL',
"Jetstar":'JQ',
"Jin Air":'LJ',
"Juneyao Airlines":'HO',
"KLM cityhopper":'WA',
"KLM":'KL',
"KLMuk":'UK',
"Kabo Air":'KO',
"Kavminvodyavia":'KV',
"Keewatin Air Limited":'FK',
"Kendell Airlines":'KD',
"Kenya Airways":'KQ',
"Keystone Air Service":'BZ',
"Khalifa Airways":'K6',
"Khazar Airlines":'KHR',
"Khors Air Company":'X9',
"Kibris Turkish Airlines":'YK',
"Kitty Hawk Group":'KR',
"Kiwi International Airlines":'KP',
"Korean Air":'KE',
"Krasnoyarsk Airlines":'7B',
"Kulula.com":'MN',
"Kuwait Airways":'KU',
"Kyrgyastan-EX":'K2',
"L.B. Limited":'7Z',
"LAB-Lioyd Aero Bolivia":'LB',
"LACSA":'LR',
"LAER S.E. Lineas Aereas Entre Rios":'2L',
"LAM":'TM',
"LIAT Airlines":'LI',
"LOT Polish Airlines":'LO',
"LTE International Airways":'XO',
"LTU International Airways":'LT',
"Lan Airlines":'LA',
"Lan Argentina":'4M',
"Lan Cargo":'UC',
"Lan Colombia Airlines":'4C',
"Lan Perú":'LP',
"LanEcuador":'XL',
"Lao Aviation":'QV',
"Leisure Intenational Airways":'ULE',
"Libyan Arab Airlines":'LN',
"Lignes Aeriennes Congolaises":'6V',
"Linair Hungarian Regional Airlines":'LF',
"Lineas Aereas Suramericanas":'LAU',
"Lineas Aereas del Estado":'5U',
"Lion Air":'JT',
"Lithuanian Airlines":'TE',
"Loganair":'LC',
"Lufthansa Cargo":'GEC',
"Lufthansa CityLine":'CL',
"Lufthansa CityLine":'CLH',
"Lufthansa":'LH',
"Lufttaxi Dortmund":'DV',
"Luxair":'LG',
"Lviv Airlines":'5V',
"MAT - Macedonian Airlines":'IN',
"MBA Pty Ltd":'CG',
"MEA":'ME',
"MIAT":'OM',
"Maersk Air":'DM',
"Maersk Air":'MSK',
"Mahan Air":'W5',
"Maina Air":'MNI',
"Malaysia Airlines":'MH',
"Malev":'MA',
"Malindo Air":'OD',
"Malmö Aviation":'TF',
"Mandarin Airlines":'AE',
"Mango":'JE',
"Martinair Cargo":'MP',
"Maya Airways":'MW',
"Meridiana fly":'IG',
"Merpati Nusantara Airlines":'MZ',
"Mesa Air Group":'YV',
"Mexicana":'MX',
"Miami Air International":'GL',
"Midway Airlines":'JI',
"Midwest Express Airlines":'YX',
"Mihin Lanka":'MJ',
"Millardair":'MAB',
"Million Air":'OX',
"Missionary Aviation Fellowship":'FS',
"ModiLuft Limited":'HT',
"Modiluft":'M9',
"Monarch Airlines":'ZB',
"Montenegro Airlines":'YM',
"Muk Air":'ZR',
"Myanmar Airways International":'8M',
"Myanmar Airways":'UB',
"NEPC Airlines":'D5',
"Nakanihon Airlines Co. Ltd.":'NV',
"National Airlines":'YJ',
"National Jet System":'NC',
"Nationwide Air":'CE',
"Necon Air":'3Z',
"Nepal Airways":'7E',
"Nesma Airlines":'NE',
"New England Airlines":'EJ',
"Nextjet":'2N',
"Nigeia Airways":'WT',
"Niki":'HG',
"Nile Air":'NP',
"Nippon Cargo Airlines (NCA)":'KZ',
"Nok Air":'DD',
"NokScoot":'XW',
"Nordeste":'JH',
"Nordic European":'N7',
"Nordkalottflyg":'8N',
"North American Airlines.":'NA',
"North Vancouver Air":'VL',
"North-Wright Airways Ltd.":'HW',
"Northwest Airlines":'NW',
"Norwegian Air Shuttle":'DY',
"Norwegian Long Haul":'D8',
"Nouvelair":'BJ',
"Novoair":'VQ',
"O'Connor Airlines":'UQ',
"Okay Airways":'BK',
"Olson Air Service":'4B',
"Olympic Air":'OA',
"Olympic Aviation":'7U',
"Oman Air":'WY',
"Omni Air International, Inc. dba Omni":'OY',
"Omni":'OC',
"Onur Air":'8Q',
"Open Skies Inc.":'1L',
"Orbi Georian Airlines":'NQ',
"Orenair":'R2',
"Origin Pacific Airways":'QO',
"Overland Airways Limited":'OJ',
"PAL Express":'2P',
"PGA-Portugália Airlines":'NI',
"PIA":'PK',
"PLUNA":'PU',
"PT Mandala Airlines":'RI',
"Pacific Airlines":'T5',
"Pacific Coastal Airlines Limited":'8P',
"Pacific Island Aviation, Inc.":'9J',
"Pacific Wings":'LW',
"Palair Macedonian":'3D',
"Palestinian Airlines":'PF',
"Pan Air":'PA',
"Pan American Airways Corp.":'PN',
"PanAm":'KW',
"Papillon Airways":'HI',
"Paradise Island Aielines":'PDI',
"Passaredo Transportes Aereos S/A":'Y8',
"Peach":'MM',
"Pegasus Airlines":'PC',
"Pegasus Asia":'ZM',
"Pelita Air":'6D',
"Pena Transportes Aereos S/A":'5P',
"Penair":'KS',
"Perm Airlines":'9D',
"Petroleum Air Services":'PAS',
"Philippine Airlines":'PR',
"Phuket Airlines Co., Ltd.":'9R',
"Pobeda":'DP',
"Polar Air Cargo":'PO',
"Polynesian Airlines":'PH',
"Porter Airlines":'PD',
"Precision Air":'PW',
"Premiair":'DK',
"Premier Trans Aire":'P3',
"PrivatAir":'PV',
"Qantas":'QF',
"Qatar Airways":'Q7',
"Qatar Airways":'QR',
"RAS Fluggesellschaft mbh":'RW',
"Red Sea Air":'7R',
"Regional Airlines":'VM',
"Regional Compagnie Aerienne Europeene":'YS',
"Regionnair Inc.":'RH',
"Riga Airlines":'GV',
"Romavia":'WQ',
"Rossiya Airlines":'FV',
"Royal Ailines":'QN',
"Royal Air Force":'RR',
"Royal Air Maroc":'AT',
"Royal Brunei":'BI',
"Royal Jordanian":'RJ',
"Royal Khmer Airlines":'FE',
"Royal Nepal Airlines":'RA',
"Royal Swazi National Airways Corp.":'ZC',
"Royal Tongan Airlines":'WR',
"Russ Air Transport Company":'NR',
"RwandAir":'WB',
"Ryan International Airlines":'HS',
"Ryanair":'FR',
"S7 Airlines":'S7',
"SA Airlink Airlines":'A4Z',
"SAA":'SA',
"SAETA-Air Ecuador":'EH',
"SAS":'SK',
"SATA Air Açores":'SP',
"SATA Internacional":'S4',
"SATENA":'ZT',
"SIA":'SQ',
"SKY Airline":'H2',
"SNCF":'2C',
"SWISS":'LX',
"Sabang":'SMC',
"Sakhalinskie Aviatrassy":'HZ',
"Samoa Air":'SE',
"Santa Barbara":'S3',
"Saratov Airlines":'6W',
"Saudi Arabian Airlines":'SV',
"Schreiner Airways":'AW',
"Scoot":'TZ',
"Seaborne Aviation, Inc.":'BB',
"Seagreen Air Transport":'ES',
"Servivensa":'VC',
"Shandong Airlines":'SC',
"Shanghai Airlines":'FM',
"Shenzhen Airlines":'4G',
"Shenzhen Airlines":'ZH',
"Sibaviatrans":'5M',
"Sichuan Airlines":'3U',
"Sierra Pacific Airlines":'SI',
"Silk Route Airways":'NS',
"Silk Way West Airlines":'7L',
"Silkair":'MI',
"SixCargo S.p.A.":'6P',
"Skymark Airlines":'BC',
"Skyways":'JZ',
"Skywest Airlines":'OO',
"Skywest Airlines":'XM',
"SmartWings":'QS',
"Smokey Bay Air":'2E',
"Sol Líneas Aéreas":'8R',
"Solaseed Air":'6J',
"Solomon Airlines":'IE',
"South African Express Airways (Pty) Ltd.":'YB',
"South Airlines":'YG',
"Southern Cross Distribution Systems":'1K',
"Southern air Transport":'SJ',
"Southwest Airlines":'WN',
"Spanair":'JK',
"SpiceJet":'SG',
"Spirit Airlines":'NK',
"Spring Airlines Japan":'IJ',
"Spring Airlines":'9C',
"SriLankan":'UL',
"Star Air":'SRR',
"StarFlyer":'7G',
"State Air Company Tajikistan":'7J',
"State Enterprise Gomelavia":'YD',
"Sterlines European Airlines":'NB',
"Sudan Airways":'SD',
"Sun Country Airlines":'SY',
"SunAir Express, LLC":'2U',
"Sunflower Airlines Ltd.":'PI',
"Sunrise Airlines":'OQ',
"Sunshine Express Airlines Pty. Ltd.":'CQ',
"Sunways Airlines":'SWY',
"Superior Aviation, Inc":'SO',
"Surinam Airways":'PY',
"Swissair":'SR',
"Syrianair":'RB',
"T'way Airlines":'TW',
"T.A.T. European Airlines":'VD',
"TAAG - Angola Airlines":'DT',
"TABA":'T2',
"TACA Peru":'T0',
"TACA":'TA',
"TACV Cabo Verde Airlines":'VR',
"TAG Aviation S.A.":'FP',
"TAM - Transportes Aéreos del Mercosur Sociedad Anónima":'PZ',
"TAM Linhas Aéreas":'JJ',
"TAME - Linea Aérea del Ecuador":'EQ',
"TAMPA":'QT',
"TAP Portugal":'TP',
"TAROM":'RO',
"TCH Of Russian Airlines":'4T',
"TEA Switzerland":'BH',
"THY - Turkish Airlines":'TK',
"TIE Aviation, Inc.":'5B',
"TNT International Aviation Services":'NTR',
"Taifun":'GIG',
"Tanana Air Service":'4E',
"Tashkent Aircraft Production Corp":'3S',
"Tassili Airlines":'SF',
"Thai AirAsia X":'XJ',
"Thai AirAsia":'FD',
"Thai Airways International":'TG',
"Thai Lion Air":'SL',
"Thai Smile":'WE',
"Thalys International":'2H',
"The Mount Cook Group Ltd.":'NM',
"Tianjin Airlines":'GS',
"Tigerair Philippines":'DG',
"Tigerair Taiwan":'IT',
"Tigerair":'TR',
"Tigerair":'TT',
"Titan Airways":'T4',
"Tolair Services":'TOL',
"Tower Air":'FF',
"Trans Air Congo (TAC)":'Q8',
"Trans States Airlines":'9N',
"Trans-Mediterranean Airways":'TL',
"TransAer":'T8',
"TransAsia Airways":'GE',
"Transaero Airlines":'UN',
"Transavia.com France":'TO',
"Transavia.com":'HV',
"Transeuropean Airlines":'UE',
"Transmile Air Service":'9P',
"Transportes Aereos Nacionales de Selva":'TJ',
"Transwede Airways":'TQ',
"Transwest Air":'9T',
"Travelsky Technology Limited":'1E',
"Tropic Air":'PM',
"Tuninter S.A.":'UG',
"Tunisair":'TU',
"Turks & Caicos Airways":'QW',
"Twin Jet":'T7',
"Tyumen Airlines":'7M',
"UNI Air":'B7',
"UPS Airlines":'5X',
"US Airways (USAir)":'US',
"US Airways Shuttle":'TB',
"US-Bangla Airlines":'BS',
"USA Jet Airlines":'U7',
"Ukraine International Airlines":'PS',
"Ukrainian Cargo Airways":'6Z',
"Ukrainian-mediterranean Airlines":'UF',
"United Airlines":'UA',
"United Airways":'4H',
"United Eagle Airlines":'EU',
"Universal Airlines Inc.":'UW',
"Universal Airways Inc.":'UV',
"Up":'LY',
"Ural Airlines":'U6',
"Uzbekistan Airways":'HY',
"V Air":'ZV',
"VASP":'VP',
"VIP Air":'9V',
"VLM Airlines":'VG',
"Vanguard Airlines":'NJ',
"Vanilla Air":'JW',
"Varig":'RG',
"Varmlandsflyg":'T9',
"Venus airlines":'V4',
"Via Rail Canada":'2R',
"Vieques Air Link":'VI',
"VietJet Air":'VJ',
"Vietnam Airlines":'VN',
"Virgin America":'VX',
"Virgin Atlantic":'VS',
"Virgin Australia":'VA',
"Virgin Blue":'DJ',
"Virgin Express S.A./N.V.":'TV',
"Virgin Express":'BQ',
"Viscount Air Service":'VCT',
"VivaColombia":'FC',
"Vivaaerobus.com":'VB',
"Vladivostok Air":'XF',
"Vnukovo Airlines":'V5',
"Volaris":'Y4',
"Volotea":'V7',
"Vueling":'VY',
"WDL Aviation":'WDL',
"WOW air":'WW',
"WaltAir I Linkoping AB":'XV',
"Wamos Air":'EB',
"Wanair":'3W',
"Warbelow's Air Ventures Inc.":'4W',
"Wasaya Airways L.P.":'WG',
"Welcome Air":'2W',
"WestJet":'WS',
"Western Pacific Airlines":'W7',
"White coloured by you":'WI',
"Wideroe":'WF',
"Windward Island Airways International":'WM',
"Wizz Air Ukraine":'WU',
"Wizz Air":'W6',
"World Airways":'WO',
"Wright Air Service":'8V',
"Xiamen Airlines":'MF',
"Yanda Airlines":'YE',
"Yangon Airways Limited":'HK',
"Yemenia":'IY',
"Yute Air Alaska":'4Y',
"Zairean Airlines":'ZAR',
"Zantop International Airlines":'VK',
"Zimbabwe flyafrica.com":'Z7',
"bmi Regional":'BM',
"slandsflug":'HH'
}

temp_airline = [
    {
        "flight_en_name": "Aerolineas de Baleares AeBal", 
        "flight_id": "DF"
    }, 
    {
        "flight_en_name": "ADA Air", 
        "flight_id": "ZY"
    }, 
    {
        "flight_en_name": "Air Alps Aviation", 
        "flight_id": "A6"
    }, 
    {
        "flight_en_name": "Alpine Aviation", 
        "flight_id": "5A"
    }, 
    {
        "flight_en_name": "Air Alpha Greenland A/S", 
        "flight_id": "GD"
    }, 
    {
        "flight_en_name": "Air Algérie", 
        "flight_id": "AH"
    }, 
    {
        "flight_en_name": "Aerocondor", 
        "flight_id": "2B"
    }, 
    {
        "flight_en_name": "Aerosur", 
        "flight_id": "5L"
    }, 
    {
        "flight_en_name": "Afriqiyah Airways", 
        "flight_id": "8U"
    }, 
    {
        "flight_en_name": "Ariana Afghan Airlines", 
        "flight_id": "FG"
    }, 
    {
        "flight_en_name": "Aerolineas Argentinas", 
        "flight_id": "AR"
    }, 
    {
        "flight_en_name": "Arkia Israeli Airlines", 
        "flight_id": "IZ"
    }, 
    {
        "flight_en_name": "Aklak Air", 
        "flight_id": "6L"
    }, 
    {
        "flight_en_name": "Alaska Airlines", 
        "flight_id": "AS"
    }, 
    {
        "flight_en_name": "Yute Air Alaska", 
        "flight_id": "4Y"
    }, 
    {
        "flight_en_name": "Kabo Air", 
        "flight_id": "KO"
    }, 
    {
        "flight_en_name": "Emirates", 
        "flight_id": "EK"
    }, 
    {
        "flight_en_name": "Aer Arann Express", 
        "flight_id": "RE"
    }, 
    {
        "flight_en_name": "Oman Air", 
        "flight_id": "WY"
    }, 
    {
        "flight_en_name": "National Airlines", 
        "flight_id": "YJ"
    }, 
    {
        "flight_en_name": "Azerbaijan Airlines", 
        "flight_id": "J2"
    }, 
    {
        "flight_en_name": "Air Astana", 
        "flight_id": "KC"
    }, 
    {
        "flight_en_name": "Air Astana", 
        "flight_id": "4L"
    }, 
    {
        "flight_en_name": "Accessair", 
        "flight_id": "ZA"
    }, 
    {
        "flight_en_name": "Boliviana de Aviación - BoA", 
        "flight_id": "OB"
    }, 
    {
        "flight_en_name": "Americana de Aviation", 
        "flight_id": "8A"
    }, 
    {
        "flight_en_name": "Atlasjet Airlines", 
        "flight_id": "KK"
    }, 
    {
        "flight_en_name": "Air Philippines", 
        "flight_id": "3G"
    }, 
    {
        "flight_en_name": "Atyrau Airways", 
        "flight_id": "IP"
    }, 
    {
        "flight_en_name": "Etihad Airways", 
        "flight_id": "EY"
    }, 
    {
        "flight_en_name": "Indonesia AirAsia", 
        "flight_id": "QZ"
    }, 
    {
        "flight_en_name": "Aigle Azur", 
        "flight_id": "ZI"
    }, 
    {
        "flight_en_name": "Azzurra Air", 
        "flight_id": "ZS"
    }, 
    {
        "flight_en_name": "Flynas", 
        "flight_id": "XY"
    }, 
    {
        "flight_en_name": "WaltAir I Linkoping AB", 
        "flight_id": "XV"
    }, 
    {
        "flight_en_name": "Egyptair", 
        "flight_id": "MS"
    }, 
    {
        "flight_en_name": "Axon Airlines", 
        "flight_id": "XN"
    }, 
    {
        "flight_en_name": "Expo Aviation", 
        "flight_id": "8D"
    }, 
    {
        "flight_en_name": "Olympic Aviation", 
        "flight_id": "7U"
    }, 
    {
        "flight_en_name": "Ethiopian Airlines", 
        "flight_id": "ET"
    }, 
    {
        "flight_en_name": "Islena Airlines", 
        "flight_id": "WC"
    }, 
    {
        "flight_en_name": "AVIACSA", 
        "flight_id": "6A"
    }, 
    {
        "flight_en_name": "Riga Airlines", 
        "flight_id": "GV"
    }, 
    {
        "flight_en_name": "Aero Airlines A.S.", 
        "flight_id": "EE"
    }, 
    {
        "flight_en_name": "Bluebird Cargo", 
        "flight_id": "BF"
    }, 
    {
        "flight_en_name": "Aer Lingus", 
        "flight_id": "EI"
    }, 
    {
        "flight_en_name": "Lan Colombia Airlines", 
        "flight_id": "4C"
    }, 
    {
        "flight_en_name": "Aegean Airlines", 
        "flight_id": "A3"
    }, 
    {
        "flight_en_name": "Estonian Air", 
        "flight_id": "OV"
    }, 
    {
        "flight_en_name": "VIP Air", 
        "flight_id": "9V"
    }, 
    {
        "flight_en_name": "Air Andaman Corporation Limited", 
        "flight_id": "2Y"
    }, 
    {
        "flight_en_name": "TAAG - Angola Airlines", 
        "flight_id": "DT"
    }, 
    {
        "flight_en_name": "Ansett Australia", 
        "flight_id": "AN"
    }, 
    {
        "flight_en_name": "Hi Fly", 
        "flight_id": "5K"
    }, 
    {
        "flight_en_name": "Austrian", 
        "flight_id": "OS"
    }, 
    {
        "flight_en_name": "Olson Air Service", 
        "flight_id": "4B"
    }, 
    {
        "flight_en_name": "Overland Airways Limited", 
        "flight_id": "OJ"
    }, 
    {
        "flight_en_name": "Augsburg Airways", 
        "flight_id": "IQ"
    }, 
    {
        "flight_en_name": "Okay Airways", 
        "flight_id": "BK"
    }, 
    {
        "flight_en_name": "Aurigny Air Services", 
        "flight_id": "GR"
    }, 
    {
        "flight_en_name": "Olympic Air", 
        "flight_id": "OA"
    }, 
    {
        "flight_en_name": "Orenair", 
        "flight_id": "R2"
    }, 
    {
        "flight_en_name": "Omni", 
        "flight_id": "OC"
    }, 
    {
        "flight_en_name": "Air Austral", 
        "flight_id": "UU"
    }, 
    {
        "flight_en_name": "Austral", 
        "flight_id": "AU"
    }, 
    {
        "flight_en_name": "Qantas", 
        "flight_id": "QF"
    }, 
    {
        "flight_en_name": "Virgin Australia", 
        "flight_id": "VA"
    }, 
    {
        "flight_en_name": "Air Macau", 
        "flight_id": "NX"
    }, 
    {
        "flight_en_name": "MBA Pty Ltd", 
        "flight_id": "CG"
    }, 
    {
        "flight_en_name": "Bahamasair", 
        "flight_id": "UP"
    }, 
    {
        "flight_en_name": "PIA", 
        "flight_id": "PK"
    }, 
    {
        "flight_en_name": "Lineas Aereas del Estado", 
        "flight_id": "5U"
    }, 
    {
        "flight_en_name": "Palestinian Airlines", 
        "flight_id": "PF"
    }, 
    {
        "flight_en_name": "COPA Airlines", 
        "flight_id": "CM"
    }, 
    {
        "flight_en_name": "Varig", 
        "flight_id": "RG"
    }, 
    {
        "flight_en_name": "TAM Linhas Aéreas", 
        "flight_id": "JJ"
    }, 
    {
        "flight_en_name": "Loganair", 
        "flight_id": "LC"
    }, 
    {
        "flight_en_name": "Belavia - Belarusian Airlines", 
        "flight_id": "B2"
    }, 
    {
        "flight_en_name": "Berjaya Air", 
        "flight_id": "J8"
    }, 
    {
        "flight_en_name": "Bering Air", 
        "flight_id": "8E"
    }, 
    {
        "flight_en_name": "Canadian Western Airlines", 
        "flight_id": "W2"
    }, 
    {
        "flight_en_name": "Air Berlin", 
        "flight_id": "AB"
    }, 
    {
        "flight_en_name": "Hunting Cargo Airlines", 
        "flight_id": "AG"
    }, 
    {
        "flight_en_name": "Tower Air", 
        "flight_id": "FF"
    }, 
    {
        "flight_en_name": "Bulgaria air", 
        "flight_id": "FB"
    }, 
    {
        "flight_en_name": "Trans-Mediterranean Airways", 
        "flight_id": "TL"
    }, 
    {
        "flight_en_name": "ABSA Cargo Airline", 
        "flight_id": "M3"
    }, 
    {
        "flight_en_name": "Air North", 
        "flight_id": "4N"
    }, 
    {
        "flight_en_name": "Air Do", 
        "flight_id": "HD"
    }, 
    {
        "flight_en_name": "Arctic Transportation Services", 
        "flight_id": "7S"
    }, 
    {
        "flight_en_name": "North American Airlines.", 
        "flight_id": "NA"
    }, 
    {
        "flight_en_name": "Aerosucre", 
        "flight_id": "6N"
    }, 
    {
        "flight_en_name": "Linair Hungarian Regional Airlines", 
        "flight_id": "LF"
    }, 
    {
        "flight_en_name": "SAS", 
        "flight_id": "SK"
    }, 
    {
        "flight_en_name": "North Vancouver Air", 
        "flight_id": "VL"
    }, 
    {
        "flight_en_name": "Bearskin Airlines", 
        "flight_id": "JV"
    }, 
    {
        "flight_en_name": "Bellview Airlines", 
        "flight_id": "B3"
    }, 
    {
        "flight_en_name": "TCH Of Russian Airlines", 
        "flight_id": "4T"
    }, 
    {
        "flight_en_name": "Empire Airlines", 
        "flight_id": "EM"
    }, 
    {
        "flight_en_name": "LIAT Airlines", 
        "flight_id": "LI"
    }, 
    {
        "flight_en_name": "Brussels Airlines", 
        "flight_id": "SN"
    }, 
    {
        "flight_en_name": "AirFreight Express", 
        "flight_id": "5Z"
    }, 
    {
        "flight_en_name": "Frontier Airlines", 
        "flight_id": "F9"
    }, 
    {
        "flight_en_name": "Air Littoral", 
        "flight_id": "FU"
    }, 
    {
        "flight_en_name": "Air Iceland", 
        "flight_id": "NY"
    }, 
    {
        "flight_en_name": "Icelandair", 
        "flight_id": "FI"
    }, 
    {
        "flight_en_name": "slandsflug", 
        "flight_id": "HH"
    }, 
    {
        "flight_en_name": "Air Atlanta Icelandic", 
        "flight_id": "CC"
    }, 
    {
        "flight_en_name": "Polar Air Cargo", 
        "flight_id": "PO"
    }, 
    {
        "flight_en_name": "Helikopterservice Euro Air", 
        "flight_id": "YQ"
    }, 
    {
        "flight_en_name": "LOT Polish Airlines", 
        "flight_id": "LO"
    }, 
    {
        "flight_en_name": "Polynesian Airlines", 
        "flight_id": "PH"
    }, 
    {
        "flight_en_name": "AirBaltic", 
        "flight_id": "BT"
    }, 
    {
        "flight_en_name": "Air Bourbon", 
        "flight_id": "4X"
    }, 
    {
        "flight_en_name": "Air Bosna", 
        "flight_id": "JA"
    }, 
    {
        "flight_en_name": "Porter Airlines", 
        "flight_id": "PD"
    }, 
    {
        "flight_en_name": "LAB-Lioyd Aero Bolivia", 
        "flight_id": "LB"
    }, 
    {
        "flight_en_name": "Air Botswana", 
        "flight_id": "BP"
    }, 
    {
        "flight_en_name": "Air Bosna", 
        "flight_id": "4V"
    }, 
    {
        "flight_en_name": "AVIOR", 
        "flight_id": "3B"
    }, 
    {
        "flight_en_name": "Bemidji Airlines", 
        "flight_id": "CH"
    }, 
    {
        "flight_en_name": "Blue1", 
        "flight_id": "KF"
    }, 
    {
        "flight_en_name": "Britannia Airways AB", 
        "flight_id": "6B"
    }, 
    {
        "flight_en_name": "Brit Air", 
        "flight_id": "DB"
    }, 
    {
        "flight_en_name": "Chang-An Airlines", 
        "flight_id": "2Z"
    }, 
    {
        "flight_en_name": "Air Burkina", 
        "flight_id": "2J"
    }, 
    {
        "flight_en_name": "Phuket Airlines Co., Ltd.", 
        "flight_id": "9R"
    }, 
    {
        "flight_en_name": "Aviation Enterprise TESIS Limited", 
        "flight_id": "UZ"
    }, 
    {
        "flight_en_name": "Braathens ASA", 
        "flight_id": "BU"
    }, 
    {
        "flight_en_name": "Air Burundi", 
        "flight_id": "8Y"
    }, 
    {
        "flight_en_name": "Airworld", 
        "flight_id": "RL"
    }, 
    {
        "flight_en_name": "EVA Air", 
        "flight_id": "BR"
    }, 
    {
        "flight_en_name": "Evergreen International Airlines", 
        "flight_id": "EZ"
    }, 
    {
        "flight_en_name": "United Eagle Airlines", 
        "flight_id": "EU"
    }, 
    {
        "flight_en_name": "Air City", 
        "flight_id": "4F"
    }, 
    {
        "flight_en_name": "China Postal Airlines", 
        "flight_id": "CF"
    }, 
    {
        "flight_en_name": "CityJet", 
        "flight_id": "WX"
    }, 
    {
        "flight_en_name": "European Regions Airlines", 
        "flight_id": "EA"
    }, 
    {
        "flight_en_name": "Transwest Air", 
        "flight_id": "9T"
    }, 
    {
        "flight_en_name": "Spring Airlines", 
        "flight_id": "9C"
    }, 
    {
        "flight_en_name": "Tigerair Taiwan", 
        "flight_id": "IT"
    }, 
    {
        "flight_en_name": "Aerolineas Internacionales", 
        "flight_id": "N2"
    }, 
    {
        "flight_en_name": "Korean Air", 
        "flight_id": "KE"
    }, 
    {
        "flight_en_name": "Southern Cross Distribution Systems", 
        "flight_id": "1K"
    }, 
    {
        "flight_en_name": "Great Lakes Aviation", 
        "flight_id": "ZK"
    }, 
    {
        "flight_en_name": "Continental Airlines", 
        "flight_id": "CO"
    }, 
    {
        "flight_en_name": "Continental Micronesia, Inc.", 
        "flight_id": "CS"
    }, 
    {
        "flight_en_name": "JMC Airlines Limited", 
        "flight_id": "MT"
    }, 
    {
        "flight_en_name": "ASA Atlantic Southeast Airlines", 
        "flight_id": "EV"
    }, 
    {
        "flight_en_name": "Air Tahiti", 
        "flight_id": "VT"
    }, 
    {
        "flight_en_name": "Islands Nationair", 
        "flight_id": "CN"
    }, 
    {
        "flight_en_name": "DAS Air Limited", 
        "flight_id": "WD"
    }, 
    {
        "flight_en_name": "Palair Macedonian", 
        "flight_id": "3D"
    }, 
    {
        "flight_en_name": "Danish Air Transport", 
        "flight_id": "DX"
    }, 
    {
        "flight_en_name": "Pacific Island Aviation, Inc.", 
        "flight_id": "9J"
    }, 
    {
        "flight_en_name": "Island Airlines (US)", 
        "flight_id": "IS"
    }, 
    {
        "flight_en_name": "Corporate Air", 
        "flight_id": "DN"
    }, 
    {
        "flight_en_name": "Schreiner Airways", 
        "flight_id": "AW"
    }, 
    {
        "flight_en_name": "Germania", 
        "flight_id": "ST"
    }, 
    {
        "flight_en_name": "Lufthansa", 
        "flight_id": "LH"
    }, 
    {
        "flight_en_name": "Deutsche Bahn AG", 
        "flight_id": "2A"
    }, 
    {
        "flight_en_name": "Germanwings", 
        "flight_id": "4U"
    }, 
    {
        "flight_en_name": "Dalavia-Far East Airways Khabarovsk", 
        "flight_id": "H8"
    }, 
    {
        "flight_en_name": "Druk Air", 
        "flight_id": "KB"
    }, 
    {
        "flight_en_name": "Flydubai", 
        "flight_id": "FZ"
    }, 
    {
        "flight_en_name": "Air Transport International", 
        "flight_id": "8C"
    }, 
    {
        "flight_en_name": "Horizon Air", 
        "flight_id": "QX"
    }, 
    {
        "flight_en_name": "Airkenya Aviation", 
        "flight_id": "QP"
    }, 
    {
        "flight_en_name": "Air Moldova International", 
        "flight_id": "RM"
    }, 
    {
        "flight_en_name": "TAM - Transportes Aéreos del Mercosur Sociedad Anónima", 
        "flight_id": "PZ"
    }, 
    {
        "flight_en_name": "Sol Líneas Aéreas", 
        "flight_id": "8R"
    }, 
    {
        "flight_en_name": "AirAsia X", 
        "flight_id": "D7"
    }, 
    {
        "flight_en_name": "Donbass - Eastern Ukrainian Airlines", 
        "flight_id": "7D"
    }, 
    {
        "flight_en_name": "Nordeste", 
        "flight_id": "JH"
    }, 
    {
        "flight_en_name": "Premiair", 
        "flight_id": "DK"
    }, 
    {
        "flight_en_name": "Tigerair Philippines", 
        "flight_id": "DG"
    }, 
    {
        "flight_en_name": "Air Bretagne", 
        "flight_id": "3E"
    }, 
    {
        "flight_en_name": "Vivaaerobus.com", 
        "flight_id": "VB"
    }, 
    {
        "flight_en_name": "Atlantic Coast Airlines", 
        "flight_id": "DH"
    }, 
    {
        "flight_en_name": "Air Togo S.A.", 
        "flight_id": "YT"
    }, 
    {
        "flight_en_name": "Air Dolomiti", 
        "flight_id": "EN"
    }, 
    {
        "flight_en_name": "Lan Argentina", 
        "flight_id": "4M"
    }, 
    {
        "flight_en_name": "Avia Air", 
        "flight_id": "3R"
    }, 
    {
        "flight_en_name": "Aeroflot", 
        "flight_id": "SU"
    }, 
    {
        "flight_en_name": "JSC Nordavia-RA", 
        "flight_id": "5N"
    }, 
    {
        "flight_en_name": "LanEcuador", 
        "flight_id": "XL"
    }, 
    {
        "flight_en_name": "Servivensa", 
        "flight_id": "VC"
    }, 
    {
        "flight_en_name": "Air France", 
        "flight_id": "AF"
    }, 
    {
        "flight_en_name": "SNCF", 
        "flight_id": "2C"
    }, 
    {
        "flight_en_name": "Atlantic Airways Faroe Islands", 
        "flight_id": "RC"
    }, 
    {
        "flight_en_name": "AirAsia Philippines", 
        "flight_id": "PQ"
    }, 
    {
        "flight_en_name": "Air Micronesia Inc.", 
        "flight_id": "ML"
    }, 
    {
        "flight_en_name": "Missionary Aviation Fellowship", 
        "flight_id": "FS"
    }, 
    {
        "flight_en_name": "PAL Express", 
        "flight_id": "2P"
    }, 
    {
        "flight_en_name": "Philippine Airlines", 
        "flight_id": "PR"
    }, 
    {
        "flight_en_name": "Premier Trans Aire", 
        "flight_id": "P3"
    }, 
    {
        "flight_en_name": "Fischer Air", 
        "flight_id": "8F"
    }, 
    {
        "flight_en_name": "Finnair", 
        "flight_id": "AY"
    }, 
    {
        "flight_en_name": "TACV Cabo Verde Airlines", 
        "flight_id": "VR"
    }, 
    {
        "flight_en_name": "Pan Air", 
        "flight_id": "PA"
    }, 
    {
        "flight_en_name": "C.A.L. Cargo Airlines", 
        "flight_id": "5C"
    }, 
    {
        "flight_en_name": "Florida West", 
        "flight_id": "RF"
    }, 
    {
        "flight_en_name": "Royal Air Force", 
        "flight_id": "RR"
    }, 
    {
        "flight_en_name": "Flybe", 
        "flight_id": "BE"
    }, 
    {
        "flight_en_name": "Arik Air", 
        "flight_id": "W3"
    }, 
    {
        "flight_en_name": "AirBridgeCargo Airlines", 
        "flight_id": "RU"
    }, 
    {
        "flight_en_name": "Vieques Air Link", 
        "flight_id": "VI"
    }, 
    {
        "flight_en_name": "Air Busan", 
        "flight_id": "BX"
    }, 
    {
        "flight_en_name": "TransAsia Airways", 
        "flight_id": "GE"
    }, 
    {
        "flight_en_name": "Aerolineas Galapagos S.A. Aerogal", 
        "flight_id": "2K"
    }, 
    {
        "flight_en_name": "Gambia International Airlines", 
        "flight_id": "GC"
    }, 
    {
        "flight_en_name": "Trans Air Congo (TAC)", 
        "flight_id": "Q8"
    }, 
    {
        "flight_en_name": "Open Skies Inc.", 
        "flight_id": "1L"
    }, 
    {
        "flight_en_name": "BH AIR", 
        "flight_id": "8H"
    }, 
    {
        "flight_en_name": "Gol Transportes Aéreos", 
        "flight_id": "G3"
    }, 
    {
        "flight_en_name": "Silk Route Airways", 
        "flight_id": "NS"
    }, 
    {
        "flight_en_name": "Big Sky Airlines", 
        "flight_id": "GQ"
    }, 
    {
        "flight_en_name": "Air Koryo", 
        "flight_id": "JS"
    }, 
    {
        "flight_en_name": "Air Afrique", 
        "flight_id": "RK"
    }, 
    {
        "flight_en_name": "Cosmic Air Pvt. Ltd.", 
        "flight_id": "F5"
    }, 
    {
        "flight_en_name": "State Enterprise Gomelavia", 
        "flight_id": "YD"
    }, 
    {
        "flight_en_name": "AVIANCA", 
        "flight_id": "AV"
    }, 
    {
        "flight_en_name": "LACSA", 
        "flight_id": "LR"
    }, 
    {
        "flight_en_name": "Miami Air International", 
        "flight_id": "GL"
    }, 
    {
        "flight_en_name": "Inter-Canadien", 
        "flight_id": "QB"
    }, 
    {
        "flight_en_name": "Air BC", 
        "flight_id": "ZX"
    }, 
    {
        "flight_en_name": "RAS Fluggesellschaft mbh", 
        "flight_id": "RW"
    }, 
    {
        "flight_en_name": "Cubana", 
        "flight_id": "CU"
    }, 
    {
        "flight_en_name": "Champion Air", 
        "flight_id": "MG"
    }, 
    {
        "flight_en_name": "Tashkent Aircraft Production Corp", 
        "flight_id": "3S"
    }, 
    {
        "flight_en_name": "Air Class Lineas Aereas (AEROVIP LTDA)", 
        "flight_id": "QD"
    }, 
    {
        "flight_en_name": "Helijet International Inc", 
        "flight_id": "JB"
    }, 
    {
        "flight_en_name": "Nordic European", 
        "flight_id": "N7"
    }, 
    {
        "flight_en_name": "National Jet System", 
        "flight_id": "NC"
    }, 
    {
        "flight_en_name": "Nationwide Air", 
        "flight_id": "CE"
    }, 
    {
        "flight_en_name": "Hahn Air", 
        "flight_id": "HR"
    }, 
    {
        "flight_en_name": "LAER S.E. Lineas Aereas Entre Rios", 
        "flight_id": "2L"
    }, 
    {
        "flight_en_name": "Hapag-Lloyd", 
        "flight_id": "HF"
    }, 
    {
        "flight_en_name": "Air Kazakstan", 
        "flight_id": "9Y"
    }, 
    {
        "flight_en_name": "Coastal Air Transport.", 
        "flight_id": "DQ"
    }, 
    {
        "flight_en_name": "Vladivostok Air", 
        "flight_id": "XF"
    }, 
    {
        "flight_en_name": "Island Air", 
        "flight_id": "WP"
    }, 
    {
        "flight_en_name": "Hainan Airlines", 
        "flight_id": "HU"
    }, 
    {
        "flight_en_name": "Seaborne Aviation, Inc.", 
        "flight_id": "BB"
    }, 
    {
        "flight_en_name": "Gulf Air", 
        "flight_id": "GF"
    }, 
    {
        "flight_en_name": "Asiana", 
        "flight_id": "OZ"
    }, 
    {
        "flight_en_name": "Air Austral", 
        "flight_id": "4R"
    }, 
    {
        "flight_en_name": "Lufthansa CityLine", 
        "flight_id": "CL"
    }, 
    {
        "flight_en_name": "T.A.T. European Airlines", 
        "flight_id": "VD"
    }, 
    {
        "flight_en_name": "Transavia.com", 
        "flight_id": "HV"
    }, 
    {
        "flight_en_name": "KLM", 
        "flight_id": "KL"
    }, 
    {
        "flight_en_name": "KLM cityhopper", 
        "flight_id": "WA"
    }, 
    {
        "flight_en_name": "Ecoair", 
        "flight_id": "9H"
    }, 
    {
        "flight_en_name": "Hemus Air", 
        "flight_id": "DU"
    }, 
    {
        "flight_en_name": "Express One Interational", 
        "flight_id": "EO"
    }, 
    {
        "flight_en_name": "Montenegro Airlines", 
        "flight_id": "YM"
    }, 
    {
        "flight_en_name": "Hazelton Airlines", 
        "flight_id": "ZL"
    }, 
    {
        "flight_en_name": "Red Sea Air", 
        "flight_id": "7R"
    }, 
    {
        "flight_en_name": "Tigerair", 
        "flight_id": "TR"
    }, 
    {
        "flight_en_name": "Warbelow's Air Ventures Inc.", 
        "flight_id": "4W"
    }, 
    {
        "flight_en_name": "Mandarin Airlines", 
        "flight_id": "AE"
    }, 
    {
        "flight_en_name": "Transaero Airlines", 
        "flight_id": "UN"
    }, 
    {
        "flight_en_name": "T'way Airlines", 
        "flight_id": "TW"
    }, 
    {
        "flight_en_name": "Varmlandsflyg", 
        "flight_id": "T9"
    }, 
    {
        "flight_en_name": "British World Airlines", 
        "flight_id": "VF"
    }, 
    {
        "flight_en_name": "Euralair International", 
        "flight_id": "RN"
    }, 
    {
        "flight_en_name": "Kitty Hawk Group", 
        "flight_id": "KR"
    }, 
    {
        "flight_en_name": "PanAm", 
        "flight_id": "KW"
    }, 
    {
        "flight_en_name": "AirAsia Zest", 
        "flight_id": "Z2"
    }, 
    {
        "flight_en_name": "Helishuttle", 
        "flight_id": "KH"
    }, 
    {
        "flight_en_name": "Muk Air", 
        "flight_id": "ZR"
    }, 
    {
        "flight_en_name": "Juneyao Airlines", 
        "flight_id": "HO"
    }, 
    {
        "flight_en_name": "Air Astana", 
        "flight_id": "LQ"
    }, 
    {
        "flight_en_name": "SunAir Express, LLC", 
        "flight_id": "2U"
    }, 
    {
        "flight_en_name": "Jeju Air", 
        "flight_id": "7C"
    }, 
    {
        "flight_en_name": "Aerocaribe", 
        "flight_id": "QA"
    }, 
    {
        "flight_en_name": "Silk Way West Airlines", 
        "flight_id": "7L"
    }, 
    {
        "flight_en_name": "Caribbean Star Airlines", 
        "flight_id": "8B"
    }, 
    {
        "flight_en_name": "Kendell Airlines", 
        "flight_id": "KD"
    }, 
    {
        "flight_en_name": "Aero California", 
        "flight_id": "JR"
    }, 
    {
        "flight_en_name": "Air Europe", 
        "flight_id": "5T"
    }, 
    {
        "flight_en_name": "Via Rail Canada", 
        "flight_id": "2R"
    }, 
    {
        "flight_en_name": "Air Canada", 
        "flight_id": "AC"
    }, 
    {
        "flight_en_name": "Air Nova", 
        "flight_id": "QK"
    }, 
    {
        "flight_en_name": "Atlantic Southeast Airlines", 
        "flight_id": "C6"
    }, 
    {
        "flight_en_name": "Binter Canarias", 
        "flight_id": "NT"
    }, 
    {
        "flight_en_name": "Ghana Airways", 
        "flight_id": "GH"
    }, 
    {
        "flight_en_name": "Air Gabon", 
        "flight_id": "GN"
    }, 
    {
        "flight_en_name": "Crledonian Airways", 
        "flight_id": "KG"
    }, 
    {
        "flight_en_name": "VietJet Air", 
        "flight_id": "VJ"
    }, 
    {
        "flight_en_name": "Shenzhen Airlines", 
        "flight_id": "4G"
    }, 
    {
        "flight_en_name": "Khalifa Airways", 
        "flight_id": "K6"
    }, 
    {
        "flight_en_name": "Vanilla Air", 
        "flight_id": "JW"
    }, 
    {
        "flight_en_name": "Air Ontario", 
        "flight_id": "GX"
    }, 
    {
        "flight_en_name": "Jet2.com", 
        "flight_id": "LS"
    }, 
    {
        "flight_en_name": "SpiceJet", 
        "flight_id": "SG"
    }, 
    {
        "flight_en_name": "Czech Airlines j.s.c", 
        "flight_id": "OK"
    }, 
    {
        "flight_en_name": "Jetstar", 
        "flight_id": "JQ"
    }, 
    {
        "flight_en_name": "Jetstar Asia", 
        "flight_id": "3K"
    }, 
    {
        "flight_en_name": "Japan Air System", 
        "flight_id": "JD"
    }, 
    {
        "flight_en_name": "Golden Air Flyg", 
        "flight_id": "DC"
    }, 
    {
        "flight_en_name": "Air Zimbabwe", 
        "flight_id": "UM"
    }, 
    {
        "flight_en_name": "Aspiring Air", 
        "flight_id": "OI"
    }, 
    {
        "flight_en_name": "Spirit Airlines", 
        "flight_id": "NK"
    }, 
    {
        "flight_en_name": "Calm Air", 
        "flight_id": "MO"
    }, 
    {
        "flight_en_name": "SixCargo S.p.A.", 
        "flight_id": "6P"
    }, 
    {
        "flight_en_name": "Monarch Airlines", 
        "flight_id": "ZB"
    }, 
    {
        "flight_en_name": "Aircalin", 
        "flight_id": "SB"
    }, 
    {
        "flight_en_name": "Air Caledonie", 
        "flight_id": "TY"
    }, 
    {
        "flight_en_name": "Cameroon Airlines", 
        "flight_id": "UY"
    }, 
    {
        "flight_en_name": "Kavminvodyavia", 
        "flight_id": "KV"
    }, 
    {
        "flight_en_name": "Air Guadeloupe", 
        "flight_id": "TX"
    }, 
    {
        "flight_en_name": "Air Engiadina", 
        "flight_id": "RQ"
    }, 
    {
        "flight_en_name": "Air Canada Rouge", 
        "flight_id": "RV"
    }, 
    {
        "flight_en_name": "IRS Aero", 
        "flight_id": "5R"
    }, 
    {
        "flight_en_name": "Qatar Airways", 
        "flight_id": "QR"
    }, 
    {
        "flight_en_name": "Cayman Airways", 
        "flight_id": "KX"
    }, 
    {
        "flight_en_name": "Keystone Air Service", 
        "flight_id": "BZ"
    }, 
    {
        "flight_en_name": "Condor", 
        "flight_id": "DE"
    }, 
    {
        "flight_en_name": "AAC Angola Air Charter", 
        "flight_id": "C3"
    }, 
    {
        "flight_en_name": "Cape Air", 
        "flight_id": "9K"
    }, 
    {
        "flight_en_name": "Colgan Air", 
        "flight_id": "9L"
    }, 
    {
        "flight_en_name": "Flash Airlines", 
        "flight_id": "7K"
    }, 
    {
        "flight_en_name": "Air Holland Charter", 
        "flight_id": "GG"
    }, 
    {
        "flight_en_name": "Kulula.com", 
        "flight_id": "MN"
    }, 
    {
        "flight_en_name": "Comair, Inc.", 
        "flight_id": "OH"
    }, 
    {
        "flight_en_name": "Kuwait Airways", 
        "flight_id": "KU"
    }, 
    {
        "flight_en_name": "Air Corsica", 
        "flight_id": "XK"
    }, 
    {
        "flight_en_name": "Corsair International", 
        "flight_id": "SS"
    }, 
    {
        "flight_en_name": "Krasnoyarsk Airlines", 
        "flight_id": "7B"
    }, 
    {
        "flight_en_name": "Air Creedec", 
        "flight_id": "YN"
    }, 
    {
        "flight_en_name": "Croatia Airlines", 
        "flight_id": "OU"
    }, 
    {
        "flight_en_name": "Crossair Europe", 
        "flight_id": "QE"
    }, 
    {
        "flight_en_name": "Air Armenia", 
        "flight_id": "4K"
    }, 
    {
        "flight_en_name": "Kenya Airways", 
        "flight_id": "KQ"
    }, 
    {
        "flight_en_name": "Nile Air", 
        "flight_id": "NP"
    }, 
    {
        "flight_en_name": "SKY Airline", 
        "flight_id": "H2"
    }, 
    {
        "flight_en_name": "Airborne Express", 
        "flight_id": "GB"
    }, 
    {
        "flight_en_name": "Airlink Limited", 
        "flight_id": "ND"
    }, 
    {
        "flight_en_name": "FlySafair", 
        "flight_id": "FA"
    }, 
    {
        "flight_en_name": "Aeroperu", 
        "flight_id": "PL"
    }, 
    {
        "flight_en_name": "Skyways", 
        "flight_id": "JZ"
    }, 
    {
        "flight_en_name": "Air Zaire", 
        "flight_id": "QC"
    }, 
    {
        "flight_en_name": "Cubana de Aviacion", 
        "flight_id": "GW"
    }, 
    {
        "flight_en_name": "Air Transat", 
        "flight_id": "TS"
    }, 
    {
        "flight_en_name": "Air Sao Tome e Principe", 
        "flight_id": "KY"
    }, 
    {
        "flight_en_name": "Air Labrador", 
        "flight_id": "WJ"
    }, 
    {
        "flight_en_name": "Itapemirim Transportes Aereos S.A.", 
        "flight_id": "LU"
    }, 
    {
        "flight_en_name": "Air Rarotonga", 
        "flight_id": "GZ"
    }, 
    {
        "flight_en_name": "LAM", 
        "flight_id": "TM"
    }, 
    {
        "flight_en_name": "Helgoland Airlines", 
        "flight_id": "LE"
    }, 
    {
        "flight_en_name": "Jet Airways Inc.", 
        "flight_id": "QJ"
    }, 
    {
        "flight_en_name": "L.B. Limited", 
        "flight_id": "7Z"
    }, 
    {
        "flight_en_name": "Wright Air Service", 
        "flight_id": "8V"
    }, 
    {
        "flight_en_name": "Khors Air Company", 
        "flight_id": "X9"
    }, 
    {
        "flight_en_name": "CC Air", 
        "flight_id": "ED"
    }, 
    {
        "flight_en_name": "Blue Panorama Airlines", 
        "flight_id": "BV"
    }, 
    {
        "flight_en_name": "Turks & Caicos Airways", 
        "flight_id": "QW"
    }, 
    {
        "flight_en_name": "Aero Lloyd", 
        "flight_id": "YP"
    }, 
    {
        "flight_en_name": "Aero Contractors", 
        "flight_id": "NG"
    }, 
    {
        "flight_en_name": "Lao Aviation", 
        "flight_id": "QV"
    }, 
    {
        "flight_en_name": "Thai Lion Air", 
        "flight_id": "SL"
    }, 
    {
        "flight_en_name": "UNI Air", 
        "flight_id": "B7"
    }, 
    {
        "flight_en_name": "Lithuanian Airlines", 
        "flight_id": "TE"
    }, 
    {
        "flight_en_name": "Tigerair", 
        "flight_id": "TT"
    }, 
    {
        "flight_en_name": "Libyan Arab Airlines", 
        "flight_id": "LN"
    }, 
    {
        "flight_en_name": "Aerolitoral", 
        "flight_id": "5D"
    }, 
    {
        "flight_en_name": "Lviv Airlines", 
        "flight_id": "5V"
    }, 
    {
        "flight_en_name": "Air ALM", 
        "flight_id": "LM"
    }, 
    {
        "flight_en_name": "Federal Express", 
        "flight_id": "FX"
    }, 
    {
        "flight_en_name": "UPS Airlines", 
        "flight_id": "5X"
    }, 
    {
        "flight_en_name": "United Airways", 
        "flight_id": "4H"
    }, 
    {
        "flight_en_name": "Alliance Airlines", 
        "flight_id": "CD"
    }, 
    {
        "flight_en_name": "Alliance Airlines", 
        "flight_id": "3A"
    }, 
    {
        "flight_en_name": "Falcon Air", 
        "flight_id": "IH"
    }, 
    {
        "flight_en_name": "VivaColombia", 
        "flight_id": "FC"
    }, 
    {
        "flight_en_name": "Air Link Pty Ltd", 
        "flight_id": "DR"
    }, 
    {
        "flight_en_name": "Cargolux S.A.", 
        "flight_id": "CV"
    }, 
    {
        "flight_en_name": "Luxair", 
        "flight_id": "LG"
    }, 
    {
        "flight_en_name": "RwandAir", 
        "flight_id": "WB"
    }, 
    {
        "flight_en_name": "Thai Smile", 
        "flight_id": "WE"
    }, 
    {
        "flight_en_name": "TAROM", 
        "flight_id": "RO"
    }, 
    {
        "flight_en_name": "Romavia", 
        "flight_id": "WQ"
    }, 
    {
        "flight_en_name": "Air Madagascar", 
        "flight_id": "MD"
    }, 
    {
        "flight_en_name": "The Mount Cook Group Ltd.", 
        "flight_id": "NM"
    }, 
    {
        "flight_en_name": "Martinair Cargo", 
        "flight_id": "MP"
    }, 
    {
        "flight_en_name": "Virgin Express", 
        "flight_id": "BQ"
    }, 
    {
        "flight_en_name": "Aeromar", 
        "flight_id": "VW"
    }, 
    {
        "flight_en_name": "Malmö Aviation", 
        "flight_id": "TF"
    }, 
    {
        "flight_en_name": "Air Malta", 
        "flight_id": "KM"
    }, 
    {
        "flight_en_name": "Air Malawi", 
        "flight_id": "QM"
    }, 
    {
        "flight_en_name": "Malaysia Airlines", 
        "flight_id": "MH"
    }, 
    {
        "flight_en_name": "MAT - Macedonian Airlines", 
        "flight_id": "IN"
    }, 
    {
        "flight_en_name": "Air Marshall Islands", 
        "flight_id": "CW"
    }, 
    {
        "flight_en_name": "Aerotransportes MAS de Carga", 
        "flight_id": "MY"
    }, 
    {
        "flight_en_name": "Maya Airways", 
        "flight_id": "MW"
    }, 
    {
        "flight_en_name": "PT Mandala Airlines", 
        "flight_id": "RI"
    }, 
    {
        "flight_en_name": "Air Mandalay Ltd", 
        "flight_id": "6T"
    }, 
    {
        "flight_en_name": "Bangkok Air", 
        "flight_id": "PG"
    }, 
    {
        "flight_en_name": "Air Mauritius", 
        "flight_id": "MK"
    }, 
    {
        "flight_en_name": "Air Mauritanie", 
        "flight_id": "MR"
    }, 
    {
        "flight_en_name": "White coloured by you", 
        "flight_id": "WI"
    }, 
    {
        "flight_en_name": "Merpati Nusantara Airlines", 
        "flight_id": "MZ"
    }, 
    {
        "flight_en_name": "Maersk Air", 
        "flight_id": "DM"
    }, 
    {
        "flight_en_name": "Thai AirAsia X", 
        "flight_id": "XJ"
    }, 
    {
        "flight_en_name": "Mesa Air Group", 
        "flight_id": "YV"
    }, 
    {
        "flight_en_name": "Intensive Air", 
        "flight_id": "IM"
    }, 
    {
        "flight_en_name": "AirTran Airways", 
        "flight_id": "FL"
    }, 
    {
        "flight_en_name": "Delta Air Lines", 
        "flight_id": "DL"
    }, 
    {
        "flight_en_name": "American Airlines", 
        "flight_id": "AA"
    }, 
    {
        "flight_en_name": "JetBlue", 
        "flight_id": "B6"
    }, 
    {
        "flight_en_name": "United Airlines", 
        "flight_id": "UA"
    }, 
    {
        "flight_en_name": "American Falcon S.A.", 
        "flight_id": "WK"
    }, 
    {
        "flight_en_name": "Canadian Airlines International", 
        "flight_id": "CP"
    }, 
    {
        "flight_en_name": "Albanian Airlines", 
        "flight_id": "LV"
    }, 
    {
        "flight_en_name": "American Eagle Airlines, Inc.", 
        "flight_id": "MQ"
    }, 
    {
        "flight_en_name": "America West Airlines", 
        "flight_id": "HP"
    }, 
    {
        "flight_en_name": "MIAT", 
        "flight_id": "OM"
    }, 
    {
        "flight_en_name": "Sibaviatrans", 
        "flight_id": "5M"
    }, 
    {
        "flight_en_name": "Biman Bangladesh Airlines", 
        "flight_id": "BG"
    }, 
    {
        "flight_en_name": "European Air Express", 
        "flight_id": "7Y"
    }, 
    {
        "flight_en_name": "British Midland Airways", 
        "flight_id": "BD"
    }, 
    {
        "flight_en_name": "WOW air", 
        "flight_id": "WW"
    }, 
    {
        "flight_en_name": "ModiLuft Limited", 
        "flight_id": "HT"
    }, 
    {
        "flight_en_name": "Lan Perú", 
        "flight_id": "LP"
    }, 
    {
        "flight_en_name": "Transportes Aereos Nacionales de Selva", 
        "flight_id": "TJ"
    }, 
    {
        "flight_en_name": "Myanmar Airways", 
        "flight_id": "UB"
    }, 
    {
        "flight_en_name": "Myanmar Airways International", 
        "flight_id": "8M"
    }, 
    {
        "flight_en_name": "Fly540", 
        "flight_id": "5H"
    }, 
    {
        "flight_en_name": "Samoa Air", 
        "flight_id": "SE"
    }, 
    {
        "flight_en_name": "Air Moldova", 
        "flight_id": "9U"
    }, 
    {
        "flight_en_name": "Royal Air Maroc", 
        "flight_id": "AT"
    }, 
    {
        "flight_en_name": "Heli Air Monaco", 
        "flight_id": "YO"
    }, 
    {
        "flight_en_name": "Mexicana", 
        "flight_id": "MX"
    }, 
    {
        "flight_en_name": "Aeromexico", 
        "flight_id": "AM"
    }, 
    {
        "flight_en_name": "Origin Pacific Airways", 
        "flight_id": "QO"
    }, 
    {
        "flight_en_name": "Meridiana fly", 
        "flight_id": "IG"
    }, 
    {
        "flight_en_name": "Mahan Air", 
        "flight_id": "W5"
    }, 
    {
        "flight_en_name": "Necon Air", 
        "flight_id": "3Z"
    }, 
    {
        "flight_en_name": "Air Manitoba", 
        "flight_id": "7N"
    }, 
    {
        "flight_en_name": "Air Namibia", 
        "flight_id": "SW"
    }, 
    {
        "flight_en_name": "Malindo Air", 
        "flight_id": "OD"
    }, 
    {
        "flight_en_name": "Jambojet", 
        "flight_id": "JX"
    }, 
    {
        "flight_en_name": "South Airlines", 
        "flight_id": "YG"
    }, 
    {
        "flight_en_name": "Air South Airlines", 
        "flight_id": "WV"
    }, 
    {
        "flight_en_name": "SAA", 
        "flight_id": "SA"
    }, 
    {
        "flight_en_name": "South African Express Airways (Pty) Ltd.", 
        "flight_id": "YB"
    }, 
    {
        "flight_en_name": "Airlink", 
        "flight_id": "4Z"
    }, 
    {
        "flight_en_name": "Air SERBIA a.d. Beograd", 
        "flight_id": "JU"
    }, 
    {
        "flight_en_name": "China Southwest Airlines", 
        "flight_id": "SZ"
    }, 
    {
        "flight_en_name": "Royal Nepal Airlines", 
        "flight_id": "RA"
    }, 
    {
        "flight_en_name": "Niki", 
        "flight_id": "HG"
    }, 
    {
        "flight_en_name": "Aero Contractors Company of Nigeria Ltd.", 
        "flight_id": "AJ"
    }, 
    {
        "flight_en_name": "Nigeia Airways", 
        "flight_id": "WT"
    }, 
    {
        "flight_en_name": "Norwegian Air Shuttle", 
        "flight_id": "DY"
    }, 
    {
        "flight_en_name": "Accesrail Inc.", 
        "flight_id": "9B"
    }, 
    {
        "flight_en_name": "Vanguard Airlines", 
        "flight_id": "NJ"
    }, 
    {
        "flight_en_name": "Nordkalottflyg", 
        "flight_id": "8N"
    }, 
    {
        "flight_en_name": "Nok Air", 
        "flight_id": "DD"
    }, 
    {
        "flight_en_name": "North-Wright Airways Ltd.", 
        "flight_id": "HW"
    }, 
    {
        "flight_en_name": "Air Nostrum", 
        "flight_id": "YW"
    }, 
    {
        "flight_en_name": "O'Connor Airlines", 
        "flight_id": "UQ"
    }, 
    {
        "flight_en_name": "TIE Aviation, Inc.", 
        "flight_id": "5B"
    }, 
    {
        "flight_en_name": "Euroatlantic Airways", 
        "flight_id": "YU"
    }, 
    {
        "flight_en_name": "Regional Compagnie Aerienne Europeene", 
        "flight_id": "YS"
    }, 
    {
        "flight_en_name": "Eurofly", 
        "flight_id": "GJ"
    }, 
    {
        "flight_en_name": "Air Europe Italy", 
        "flight_id": "PE"
    }, 
    {
        "flight_en_name": "European Air Transport", 
        "flight_id": "QY"
    }, 
    {
        "flight_en_name": "Eurocypria Airlines", 
        "flight_id": "UI"
    }, 
    {
        "flight_en_name": "Nesma Airlines", 
        "flight_id": "NE"
    }, 
    {
        "flight_en_name": "Eurostar", 
        "flight_id": "9F"
    }, 
    {
        "flight_en_name": "Eurowings", 
        "flight_id": "EW"
    }, 
    {
        "flight_en_name": "European Executive Express", 
        "flight_id": "RY"
    }, 
    {
        "flight_en_name": "Gestair S.A.", 
        "flight_id": "GP"
    }, 
    {
        "flight_en_name": "Russ Air Transport Company", 
        "flight_id": "NR"
    }, 
    {
        "flight_en_name": "Papillon Airways", 
        "flight_id": "HI"
    }, 
    {
        "flight_en_name": "Ukrainian Cargo Airways", 
        "flight_id": "6Z"
    }, 
    {
        "flight_en_name": "Penair", 
        "flight_id": "KS"
    }, 
    {
        "flight_en_name": "Pelita Air", 
        "flight_id": "6D"
    }, 
    {
        "flight_en_name": "Jet Aviation Business Jets AG", 
        "flight_id": "PP"
    }, 
    {
        "flight_en_name": "PGA-Portugália Airlines", 
        "flight_id": "NI"
    }, 
    {
        "flight_en_name": "TAP Portugal", 
        "flight_id": "TP"
    }, 
    {
        "flight_en_name": "Burlington Air Express", 
        "flight_id": "8W"
    }, 
    {
        "flight_en_name": "Precision Air", 
        "flight_id": "PW"
    }, 
    {
        "flight_en_name": "Rossiya Airlines", 
        "flight_id": "FV"
    }, 
    {
        "flight_en_name": "Air Burundi", 
        "flight_id": "PB"
    }, 
    {
        "flight_en_name": "Chalk's Ocean Airways", 
        "flight_id": "OP"
    }, 
    {
        "flight_en_name": "Georgian Airways", 
        "flight_id": "A9"
    }, 
    {
        "flight_en_name": "Tyumen Airlines", 
        "flight_id": "7M"
    }, 
    {
        "flight_en_name": "US Airways (USAir)", 
        "flight_id": "US"
    }, 
    {
        "flight_en_name": "All Nippon Airways", 
        "flight_id": "NH"
    }, 
    {
        "flight_en_name": "SAETA-Air Ecuador", 
        "flight_id": "EH"
    }, 
    {
        "flight_en_name": "Tropic Air", 
        "flight_id": "PM"
    }, 
    {
        "flight_en_name": "Aero-tropics Air Services", 
        "flight_id": "HC"
    }, 
    {
        "flight_en_name": "Airtours International", 
        "flight_id": "VZ"
    }, 
    {
        "flight_en_name": "Axess International Network Inc.", 
        "flight_id": "1J"
    }, 
    {
        "flight_en_name": "JAL Express", 
        "flight_id": "JC"
    }, 
    {
        "flight_en_name": "Orbi Georian Airlines", 
        "flight_id": "NQ"
    }, 
    {
        "flight_en_name": "Japan Airlines", 
        "flight_id": "JL"
    }, 
    {
        "flight_en_name": "Nippon Cargo Airlines (NCA)", 
        "flight_id": "KZ"
    }, 
    {
        "flight_en_name": "Japan TransOcean Air", 
        "flight_id": "NU"
    }, 
    {
        "flight_en_name": "Jalways", 
        "flight_id": "JO"
    }, 
    {
        "flight_en_name": "Alitalia Team", 
        "flight_id": "RD"
    }, 
    {
        "flight_en_name": "Ryanair", 
        "flight_id": "FR"
    }, 
    {
        "flight_en_name": "Air Toulouse International", 
        "flight_id": "SH"
    }, 
    {
        "flight_en_name": "SWISS", 
        "flight_id": "LX"
    }, 
    {
        "flight_en_name": "Swissair", 
        "flight_id": "SR"
    }, 
    {
        "flight_en_name": "EasyJet Switzerland", 
        "flight_id": "DS"
    }, 
    {
        "flight_en_name": "Corporate Airlines", 
        "flight_id": "3C"
    }, 
    {
        "flight_en_name": "Jet Lite (India) Limited", 
        "flight_id": "S2"
    }, 
    {
        "flight_en_name": "Sakhalinskie Aviatrassy", 
        "flight_id": "HZ"
    }, 
    {
        "flight_en_name": "Saratov Airlines", 
        "flight_id": "6W"
    }, 
    {
        "flight_en_name": "Island Express", 
        "flight_id": "2S"
    }, 
    {
        "flight_en_name": "Trans States Airlines", 
        "flight_id": "9N"
    }, 
    {
        "flight_en_name": "Jin Air", 
        "flight_id": "LJ"
    }, 
    {
        "flight_en_name": "Cyprus Airways", 
        "flight_id": "CY"
    }, 
    {
        "flight_en_name": "Kibris Turkish Airlines", 
        "flight_id": "YK"
    }, 
    {
        "flight_en_name": "Air Seychelles", 
        "flight_id": "HM"
    }, 
    {
        "flight_en_name": "SATA Air Açores", 
        "flight_id": "SP"
    }, 
    {
        "flight_en_name": "Saudi Arabian Airlines", 
        "flight_id": "SV"
    }, 
    {
        "flight_en_name": "Air Atlantique", 
        "flight_id": "NL"
    }, 
    {
        "flight_en_name": "Shandong Airlines", 
        "flight_id": "SC"
    }, 
    {
        "flight_en_name": "TAMPA", 
        "flight_id": "QT"
    }, 
    {
        "flight_en_name": "Shanghai Airlines", 
        "flight_id": "FM"
    }, 
    {
        "flight_en_name": "Shenzhen Airlines", 
        "flight_id": "ZH"
    }, 
    {
        "flight_en_name": "Excel Airways", 
        "flight_id": "JN"
    }, 
    {
        "flight_en_name": "PrivatAir", 
        "flight_id": "PV"
    }, 
    {
        "flight_en_name": "VASP", 
        "flight_id": "VP"
    }, 
    {
        "flight_en_name": "Air Santo Domingo", 
        "flight_id": "EX"
    }, 
    {
        "flight_en_name": "Midway Airlines", 
        "flight_id": "JI"
    }, 
    {
        "flight_en_name": "Air St. Pierre", 
        "flight_id": "PJ"
    }, 
    {
        "flight_en_name": "Era Aviation", 
        "flight_id": "7H"
    }, 
    {
        "flight_en_name": "World Airways", 
        "flight_id": "WO"
    }, 
    {
        "flight_en_name": "Pobeda", 
        "flight_id": "DP"
    }, 
    {
        "flight_en_name": "Lufttaxi Dortmund", 
        "flight_id": "DV"
    }, 
    {
        "flight_en_name": "American International", 
        "flight_id": "CB"
    }, 
    {
        "flight_en_name": "SriLankan", 
        "flight_id": "UL"
    }, 
    {
        "flight_en_name": "Mihin Lanka", 
        "flight_id": "MJ"
    }, 
    {
        "flight_en_name": "Air Gulf Falcon", 
        "flight_id": "QL"
    }, 
    {
        "flight_en_name": "Southern air Transport", 
        "flight_id": "SJ"
    }, 
    {
        "flight_en_name": "Germania", 
        "flight_id": "GM"
    }, 
    {
        "flight_en_name": "Cape Smythe Air Service Inc", 
        "flight_id": "6C"
    }, 
    {
        "flight_en_name": "Smokey Bay Air", 
        "flight_id": "2E"
    }, 
    {
        "flight_en_name": "Sterlines European Airlines", 
        "flight_id": "NB"
    }, 
    {
        "flight_en_name": "Air Cairo", 
        "flight_id": "SM"
    }, 
    {
        "flight_en_name": "Royal Swazi National Airways Corp.", 
        "flight_id": "ZC"
    }, 
    {
        "flight_en_name": "Sichuan Airlines", 
        "flight_id": "3U"
    }, 
    {
        "flight_en_name": "Yangon Airways Limited", 
        "flight_id": "HK"
    }, 
    {
        "flight_en_name": "Sudan Airways", 
        "flight_id": "SD"
    }, 
    {
        "flight_en_name": "Universal Airways Inc.", 
        "flight_id": "UV"
    }, 
    {
        "flight_en_name": "Surinam Airways", 
        "flight_id": "PY"
    }, 
    {
        "flight_en_name": "Cebu Pacific", 
        "flight_id": "5J"
    }, 
    {
        "flight_en_name": "Solomon Airlines", 
        "flight_id": "IE"
    }, 
    {
        "flight_en_name": "Omni Air International, Inc. dba Omni", 
        "flight_id": "OY"
    }, 
    {
        "flight_en_name": "Air Bagan", 
        "flight_id": "4S"
    }, 
    {
        "flight_en_name": "Superior Aviation, Inc", 
        "flight_id": "SO"
    }, 
    {
        "flight_en_name": "State Air Company Tajikistan", 
        "flight_id": "7J"
    }, 
    {
        "flight_en_name": "TACA", 
        "flight_id": "TA"
    }, 
    {
        "flight_en_name": "TAME - Linea Aérea del Ecuador", 
        "flight_id": "EQ"
    }, 
    {
        "flight_en_name": "Tanana Air Service", 
        "flight_id": "4E"
    }, 
    {
        "flight_en_name": "Tassili Airlines", 
        "flight_id": "SF"
    }, 
    {
        "flight_en_name": "Felix Airways", 
        "flight_id": "FO"
    }, 
    {
        "flight_en_name": "Air Tahiti Nui", 
        "flight_id": "TN"
    }, 
    {
        "flight_en_name": "Aeromexpress", 
        "flight_id": "3F"
    }, 
    {
        "flight_en_name": "Pacific Coastal Airlines Limited", 
        "flight_id": "8P"
    }, 
    {
        "flight_en_name": "Pacific Wings", 
        "flight_id": "LW"
    }, 
    {
        "flight_en_name": "Sunflower Airlines Ltd.", 
        "flight_id": "PI"
    }, 
    {
        "flight_en_name": "Sunshine Express Airlines Pty. Ltd.", 
        "flight_id": "CQ"
    }, 
    {
        "flight_en_name": "Arca Colombia", 
        "flight_id": "ZU"
    }, 
    {
        "flight_en_name": "Million Air", 
        "flight_id": "OX"
    }, 
    {
        "flight_en_name": "Thai Airways International", 
        "flight_id": "TG"
    }, 
    {
        "flight_en_name": "Inter Tropical Aviation", 
        "flight_id": "3P"
    }, 
    {
        "flight_en_name": "Angel Airlines", 
        "flight_id": "8G"
    }, 
    {
        "flight_en_name": "Thai AirAsia", 
        "flight_id": "FD"
    }, 
    {
        "flight_en_name": "Transwede Airways", 
        "flight_id": "TQ"
    }, 
    {
        "flight_en_name": "Air Tanzania", 
        "flight_id": "TC"
    }, 
    {
        "flight_en_name": "Royal Tongan Airlines", 
        "flight_id": "WR"
    }, 
    {
        "flight_en_name": "Britannia Airways", 
        "flight_id": "BY"
    }, 
    {
        "flight_en_name": "Perm Airlines", 
        "flight_id": "9D"
    }, 
    {
        "flight_en_name": "Caribbean Airlines", 
        "flight_id": "BW"
    }, 
    {
        "flight_en_name": "Wizz Air Ukraine", 
        "flight_id": "WU"
    }, 
    {
        "flight_en_name": "Air Liberte", 
        "flight_id": "VO"
    }, 
    {
        "flight_en_name": "Skymark Airlines", 
        "flight_id": "BC"
    }, 
    {
        "flight_en_name": "Tianjin Airlines", 
        "flight_id": "GS"
    }, 
    {
        "flight_en_name": "Azul Brazilian Airlines", 
        "flight_id": "AD"
    }, 
    {
        "flight_en_name": "Sierra Pacific Airlines", 
        "flight_id": "SI"
    }, 
    {
        "flight_en_name": "Air Tindi Ltd", 
        "flight_id": "8T"
    }, 
    {
        "flight_en_name": "Jetstar Japan", 
        "flight_id": "GK"
    }, 
    {
        "flight_en_name": "Tuninter S.A.", 
        "flight_id": "UG"
    }, 
    {
        "flight_en_name": "Tunisair", 
        "flight_id": "TU"
    }, 
    {
        "flight_en_name": "Nouvelair", 
        "flight_id": "BJ"
    }, 
    {
        "flight_en_name": "Canada 3000 Airlines", 
        "flight_id": "2T"
    }, 
    {
        "flight_en_name": "Contact", 
        "flight_id": "3T"
    }, 
    {
        "flight_en_name": "THY - Turkish Airlines", 
        "flight_id": "TK"
    }, 
    {
        "flight_en_name": "Dominicana", 
        "flight_id": "DO"
    }, 
    {
        "flight_en_name": "Air Vanuatu", 
        "flight_id": "NF"
    }, 
    {
        "flight_en_name": "Aerosur", 
        "flight_id": "3M"
    }, 
    {
        "flight_en_name": "Aviateca", 
        "flight_id": "GU"
    }, 
    {
        "flight_en_name": "Wideroe", 
        "flight_id": "WF"
    }, 
    {
        "flight_en_name": "Air Wisconsin", 
        "flight_id": "ZW"
    }, 
    {
        "flight_en_name": "Virgin Blue", 
        "flight_id": "DJ"
    }, 
    {
        "flight_en_name": "VLM Airlines", 
        "flight_id": "VG"
    }, 
    {
        "flight_en_name": "Business Aviation", 
        "flight_id": "4P"
    }, 
    {
        "flight_en_name": "Vueling", 
        "flight_id": "VY"
    }, 
    {
        "flight_en_name": "Air Italy S.p.A.", 
        "flight_id": "NN"
    }, 
    {
        "flight_en_name": "Air Atlantic", 
        "flight_id": "9A"
    }, 
    {
        "flight_en_name": "Regional Airlines", 
        "flight_id": "VM"
    }, 
    {
        "flight_en_name": "Virgin Atlantic", 
        "flight_id": "VS"
    }, 
    {
        "flight_en_name": "Virgin America", 
        "flight_id": "VX"
    }, 
    {
        "flight_en_name": "Wizz Air", 
        "flight_id": "W6"
    }, 
    {
        "flight_en_name": "Freebird Airlines", 
        "flight_id": "FH"
    }, 
    {
        "flight_en_name": "Alaska Coastal", 
        "flight_id": "7A"
    }, 
    {
        "flight_en_name": "Welcome Air", 
        "flight_id": "2W"
    }, 
    {
        "flight_en_name": "LTU International Airways", 
        "flight_id": "LT"
    }, 
    {
        "flight_en_name": "Royal Brunei", 
        "flight_id": "BI"
    }, 
    {
        "flight_en_name": "AOM French Airlines", 
        "flight_id": "IW"
    }, 
    {
        "flight_en_name": "Aerosvit Airlines", 
        "flight_id": "3N"
    }, 
    {
        "flight_en_name": "Ukrainian-mediterranean Airlines", 
        "flight_id": "UF"
    }, 
    {
        "flight_en_name": "Ukraine International Airlines", 
        "flight_id": "PS"
    }, 
    {
        "flight_en_name": "Air Ukraine", 
        "flight_id": "6U"
    }, 
    {
        "flight_en_name": "Aerosvit Airlines", 
        "flight_id": "VV"
    }, 
    {
        "flight_en_name": "Ural Airlines", 
        "flight_id": "U6"
    }, 
    {
        "flight_en_name": "PLUNA", 
        "flight_id": "PU"
    }, 
    {
        "flight_en_name": "Uzbekistan Airways", 
        "flight_id": "HY"
    }, 
    {
        "flight_en_name": "Guine Bissau Airlines", 
        "flight_id": "G6"
    }, 
    {
        "flight_en_name": "IBERIA", 
        "flight_id": "IB"
    }, 
    {
        "flight_en_name": "Spanair", 
        "flight_id": "JK"
    }, 
    {
        "flight_en_name": "Firefly", 
        "flight_id": "FY"
    }, 
    {
        "flight_en_name": "Express Airlines", 
        "flight_id": "9E"
    }, 
    {
        "flight_en_name": "Northwest Airlines", 
        "flight_id": "NW"
    }, 
    {
        "flight_en_name": "Thalys International", 
        "flight_id": "2H"
    }, 
    {
        "flight_en_name": "S7 Airlines", 
        "flight_id": "S7"
    }, 
    {
        "flight_en_name": "Wasaya Airways L.P.", 
        "flight_id": "WG"
    }, 
    {
        "flight_en_name": "Virgin Express S.A./N.V.", 
        "flight_id": "TV"
    }, 
    {
        "flight_en_name": "Air Sweden", 
        "flight_id": "PT"
    }, 
    {
        "flight_en_name": "WestJet", 
        "flight_id": "WS"
    }, 
    {
        "flight_en_name": "Skywest Airlines", 
        "flight_id": "OO"
    }, 
    {
        "flight_en_name": "Acvila Air", 
        "flight_id": "WZ"
    }, 
    {
        "flight_en_name": "Keewatin Air Limited", 
        "flight_id": "FK"
    }, 
    {
        "flight_en_name": "Air Sinai", 
        "flight_id": "4D"
    }, 
    {
        "flight_en_name": "Southwest Airlines", 
        "flight_id": "WN"
    }, 
    {
        "flight_en_name": "Nepal Airways", 
        "flight_id": "7E"
    }, 
    {
        "flight_en_name": "Hawaiian Airlines", 
        "flight_id": "HA"
    }, 
    {
        "flight_en_name": "Xiamen Airlines", 
        "flight_id": "MF"
    }, 
    {
        "flight_en_name": "Dragonair", 
        "flight_id": "KA"
    }, 
    {
        "flight_en_name": "Cathay Pacific", 
        "flight_id": "CX"
    }, 
    {
        "flight_en_name": "Hong Kong Airlines", 
        "flight_id": "HX"
    }, 
    {
        "flight_en_name": "Hong Kong Express Airways", 
        "flight_id": "UO"
    }, 
    {
        "flight_en_name": "Windward Island Airways International", 
        "flight_id": "WM"
    }, 
    {
        "flight_en_name": "Chautauqua Airlines, Inc.", 
        "flight_id": "RP"
    }, 
    {
        "flight_en_name": "Aviation Assistance A.S.", 
        "flight_id": "7W"
    }, 
    {
        "flight_en_name": "Cimber Air", 
        "flight_id": "QI"
    }, 
    {
        "flight_en_name": "Aero Continente", 
        "flight_id": "N6"
    }, 
    {
        "flight_en_name": "NokScoot", 
        "flight_id": "XW"
    }, 
    {
        "flight_en_name": "Air Niugini", 
        "flight_id": "PX"
    }, 
    {
        "flight_en_name": "SIA", 
        "flight_id": "SQ"
    }, 
    {
        "flight_en_name": "Silkair", 
        "flight_id": "MI"
    }, 
    {
        "flight_en_name": "Air New Zealand", 
        "flight_id": "NZ"
    }, 
    {
        "flight_en_name": "New England Airlines", 
        "flight_id": "EJ"
    }, 
    {
        "flight_en_name": "Pegasus Asia", 
        "flight_id": "ZM"
    }, 
    {
        "flight_en_name": "Malev", 
        "flight_id": "MA"
    }, 
    {
        "flight_en_name": "Pena Transportes Aereos S/A", 
        "flight_id": "5P"
    }, 
    {
        "flight_en_name": "Syrianair", 
        "flight_id": "RB"
    }, 
    {
        "flight_en_name": "Jetstar Hong Kong", 
        "flight_id": "JM"
    }, 
    {
        "flight_en_name": "Canadian Regional Airlines", 
        "flight_id": "KI"
    }, 
    {
        "flight_en_name": "Adria Airways", 
        "flight_id": "JP"
    }, 
    {
        "flight_en_name": "Great American Airways", 
        "flight_id": "MV"
    }, 
    {
        "flight_en_name": "Royal Ailines", 
        "flight_id": "QN"
    }, 
    {
        "flight_en_name": "AirAsia", 
        "flight_id": "AK"
    }, 
    {
        "flight_en_name": "Asian Spirit", 
        "flight_id": "6K"
    }, 
    {
        "flight_en_name": "Guyana Airways Corporation", 
        "flight_id": "GY"
    }, 
    {
        "flight_en_name": "Yanda Airlines", 
        "flight_id": "YE"
    }, 
    {
        "flight_en_name": "Passaredo Transportes Aereos S/A", 
        "flight_id": "Y8"
    }, 
    {
        "flight_en_name": "Air Sunshine", 
        "flight_id": "YI"
    }, 
    {
        "flight_en_name": "Sun Country Airlines", 
        "flight_id": "SY"
    }, 
    {
        "flight_en_name": "Yemenia", 
        "flight_id": "IY"
    }, 
    {
        "flight_en_name": "Air One", 
        "flight_id": "AP"
    }, 
    {
        "flight_en_name": "First Air", 
        "flight_id": "7F"
    }, 
    {
        "flight_en_name": "Iraqi Airways", 
        "flight_id": "IA"
    }, 
    {
        "flight_en_name": "Iran Aseman Airlines", 
        "flight_id": "EP"
    }, 
    {
        "flight_en_name": "Iran Air", 
        "flight_id": "IR"
    }, 
    {
        "flight_en_name": "Imair", 
        "flight_id": "IK"
    }, 
    {
        "flight_en_name": "Air Inuit", 
        "flight_id": "3H"
    }, 
    {
        "flight_en_name": "Great China Airlines", 
        "flight_id": "IF"
    }, 
    {
        "flight_en_name": "Air Guinee", 
        "flight_id": "GI"
    }, 
    {
        "flight_en_name": "Up", 
        "flight_id": "LY"
    }, 
    {
        "flight_en_name": "Israir", 
        "flight_id": "6H"
    }, 
    {
        "flight_en_name": "Fair", 
        "flight_id": "FW"
    }, 
    {
        "flight_en_name": "EasyJet", 
        "flight_id": "U2"
    }, 
    {
        "flight_en_name": "Aérovas Venezolanas", 
        "flight_id": "VE"
    }, 
    {
        "flight_en_name": "Air-Serv., Inc. dba Indigo", 
        "flight_id": "I9"
    }, 
    {
        "flight_en_name": "Alitalia", 
        "flight_id": "AZ"
    }, 
    {
        "flight_en_name": "Skywest Airlines", 
        "flight_id": "XM"
    }, 
    {
        "flight_en_name": "IndiGo", 
        "flight_id": "6E"
    }, 
    {
        "flight_en_name": "Air India Express", 
        "flight_id": "IX"
    }, 
    {
        "flight_en_name": "Indian Airlines", 
        "flight_id": "IC"
    }, 
    {
        "flight_en_name": "Air India", 
        "flight_id": "AI"
    }, 
    {
        "flight_en_name": "Jet Airways", 
        "flight_id": "9W"
    }, 
    {
        "flight_en_name": "Bouraq Indonesia Airlines", 
        "flight_id": "BO"
    }, 
    {
        "flight_en_name": "Lion Air", 
        "flight_id": "JT"
    }, 
    {
        "flight_en_name": "Garuda", 
        "flight_id": "GA"
    }, 
    {
        "flight_en_name": "bmi Regional", 
        "flight_id": "BM"
    }, 
    {
        "flight_en_name": "Regionnair Inc.", 
        "flight_id": "RH"
    }, 
    {
        "flight_en_name": "British Mediterranean Airways Limited", 
        "flight_id": "KJ"
    }, 
    {
        "flight_en_name": "US-Bangla Airlines", 
        "flight_id": "BS"
    }, 
    {
        "flight_en_name": "British Airways", 
        "flight_id": "BA"
    }, 
    {
        "flight_en_name": "British Regional Airlines Limited", 
        "flight_id": "TH"
    }, 
    {
        "flight_en_name": "Jersey European Airways", 
        "flight_id": "JY"
    }, 
    {
        "flight_en_name": "InterSky", 
        "flight_id": "3L"
    }, 
    {
        "flight_en_name": "TEA Switzerland", 
        "flight_id": "BH"
    }, 
    {
        "flight_en_name": "Wanair", 
        "flight_id": "3W"
    }, 
    {
        "flight_en_name": "Transeuropean Airlines", 
        "flight_id": "UE"
    }, 
    {
        "flight_en_name": "Baseops International, Inc.", 
        "flight_id": "3Y"
    }, 
    {
        "flight_en_name": "Georgian Airlines", 
        "flight_id": "6R"
    }, 
    {
        "flight_en_name": "Universal Airlines Inc.", 
        "flight_id": "UW"
    }, 
    {
        "flight_en_name": "Royal Khmer Airlines", 
        "flight_id": "FE"
    }, 
    {
        "flight_en_name": "Royal Jordanian", 
        "flight_id": "RJ"
    }, 
    {
        "flight_en_name": "Vietnam Airlines", 
        "flight_id": "VN"
    }, 
    {
        "flight_en_name": "Jetstar Pacific", 
        "flight_id": "BL"
    }, 
    {
        "flight_en_name": "Cargo Plus Aviation Inc.", 
        "flight_id": "8L"
    }, 
    {
        "flight_en_name": "SATENA", 
        "flight_id": "ZT"
    }, 
    {
        "flight_en_name": "Air Arabia", 
        "flight_id": "4J"
    }, 
    {
        "flight_en_name": "Fastjet", 
        "flight_id": "FN"
    }, 
    {
        "flight_en_name": "GB Airways Ltd.", 
        "flight_id": "GT"
    }, 
    {
        "flight_en_name": "Ryan International Airlines", 
        "flight_id": "HS"
    }, 
    {
        "flight_en_name": "Lan Airlines", 
        "flight_id": "LA"
    }, 
    {
        "flight_en_name": "Lan Cargo", 
        "flight_id": "UC"
    }, 
    {
        "flight_en_name": "MEA", 
        "flight_id": "ME"
    }, 
    {
        "flight_en_name": "China Eastern", 
        "flight_id": "MU"
    }, 
    {
        "flight_en_name": "Air China Limited", 
        "flight_id": "CA"
    }, 
    {
        "flight_en_name": "Enkor Airlines", 
        "flight_id": "G5"
    }, 
    {
        "flight_en_name": "China Cargo Airlines", 
        "flight_id": "CK"
    }, 
    {
        "flight_en_name": "China United Airlines", 
        "flight_id": "KN"
    }, 
    {
        "flight_en_name": "Travelsky Technology Limited", 
        "flight_id": "1E"
    }, 
    {
        "flight_en_name": "China Southern Airlines", 
        "flight_id": "CZ"
    }, 
    {
        "flight_en_name": "China Northwest Airlines", 
        "flight_id": "WH"
    }, 
    {
        "flight_en_name": "Pan American Airways Corp.", 
        "flight_id": "PN"
    }, 
    {
        "flight_en_name": "LTE International Airways", 
        "flight_id": "XO"
    }, 
    {
        "flight_en_name": "China Yunnan Airlines", 
        "flight_id": "3Q"
    }, 
    {
        "flight_en_name": "China Airlines", 
        "flight_id": "CI"
    }, 
    {
        "flight_en_name": "Nakanihon Airlines Co. Ltd.", 
        "flight_id": "NV"
    }, 
    {
        "flight_en_name": "V Air", 
        "flight_id": "ZV"
    }, 
    {
        "flight_en_name": "Midwest Express Airlines", 
        "flight_id": "YX"
    }, 
    {
        "flight_en_name": "Astral Aviation, Inc.", 
        "flight_id": "AL"
    }, 
    {
        "flight_en_name": "Central Mountain Air Ltd.", 
        "flight_id": "9M"
    }, 
    {
        "flight_en_name": "Sunrise Airlines", 
        "flight_id": "OQ"
    }, 
    {
        "flight_en_name": "Domodedovo Airlines", 
        "flight_id": "HN"
    }, 
    {
        "flight_en_name": "Lignes Aeriennes Congolaises", 
        "flight_id": "6V"
    }, 
    {
        "flight_en_name": "Indonesia AirAsia X", 
        "flight_id": "XT"
    }, 
    {
        "flight_en_name": "TAG Aviation S.A.", 
        "flight_id": "FP"
    }, 
    {
        "flight_en_name": "Executive Airlines/American Eagle", 
        "flight_id": "OW"
    }, 
    {
        "flight_en_name": "Transavia.com France", 
        "flight_id": "TO"
    }, 
    {
        "flight_en_name": "Adam Skyconnection", 
        "flight_id": "1A"
    }, 
    {
        "flight_en_name": "Aer Arann", 
        "flight_id": "1I"
    }, 
    {
        "flight_en_name": "Aero Benin", 
        "flight_id": "1M"
    }, 
    {
        "flight_en_name": "Debonair", 
        "flight_id": "2G"
    }, 
    {
        "flight_en_name": "Air Alliance", 
        "flight_id": "3J"
    }, 
    {
        "flight_en_name": "Japan Air Commuter", 
        "flight_id": "3X"
    }, 
    {
        "flight_en_name": "Air Europa Lineas Aereas", 
        "flight_id": "5S"
    }, 
    {
        "flight_en_name": "Atlas Air", 
        "flight_id": "5Y"
    }, 
    {
        "flight_en_name": "StarFlyer", 
        "flight_id": "7G"
    }, 
    {
        "flight_en_name": "Air Ostrava", 
        "flight_id": "8K"
    }, 
    {
        "flight_en_name": "Transmile Air Service", 
        "flight_id": "9P"
    }, 
    {
        "flight_en_name": "SA Airlink Airlines", 
        "flight_id": "A4Z"
    }, 
    {
        "flight_en_name": "Airfast Indonesia", 
        "flight_id": "AFE"
    }, 
    {
        "flight_en_name": "9 Air", 
        "flight_id": "AQ"
    }, 
    {
        "flight_en_name": "Aeropostale", 
        "flight_id": "ARP"
    }, 
    {
        "flight_en_name": "Binter Mediterraneo", 
        "flight_id": "AX"
    }, 
    {
        "flight_en_name": "Baron Aviation Services", 
        "flight_id": "BVN"
    }, 
    {
        "flight_en_name": "Commercial Airways", 
        "flight_id": "CAW"
    }, 
    {
        "flight_en_name": "Chautauqua Airlines", 
        "flight_id": "CHQ"
    }, 
    {
        "flight_en_name": "Lufthansa CityLine", 
        "flight_id": "CLH"
    }, 
    {
        "flight_en_name": "CR Airways", 
        "flight_id": "CR"
    }, 
    {
        "flight_en_name": "Aero Caribbean", 
        "flight_id": "CRN"
    }, 
    {
        "flight_en_name": "Daallo Airlines", 
        "flight_id": "D3"
    }, 
    {
        "flight_en_name": "NEPC Airlines", 
        "flight_id": "D5"
    }, 
    {
        "flight_en_name": "Donavia", 
        "flight_id": "D9"
    }, 
    {
        "flight_en_name": "Aero Asia International", 
        "flight_id": "E4"
    }, 
    {
        "flight_en_name": "British Airways Cargo", 
        "flight_id": "E9"
    }, 
    {
        "flight_en_name": "European Aviation Air Charter", 
        "flight_id": "EAF"
    }, 
    {
        "flight_en_name": "Wamos Air", 
        "flight_id": "EB"
    }, 
    {
        "flight_en_name": "Eurofly", 
        "flight_id": "EEZ"
    }, 
    {
        "flight_en_name": "EasyFly", 
        "flight_id": "EF"
    }, 
    {
        "flight_en_name": "JAA", 
        "flight_id": "EG"
    }, 
    {
        "flight_en_name": "Ireland Airways", 
        "flight_id": "EIX"
    }, 
    {
        "flight_en_name": "Air Nippon", 
        "flight_id": "EL"
    }, 
    {
        "flight_en_name": "DHL Airways", 
        "flight_id": "ER"
    }, 
    {
        "flight_en_name": "Seagreen Air Transport", 
        "flight_id": "ES"
    }, 
    {
        "flight_en_name": "Famner Air Transport", 
        "flight_id": "FAT"
    }, 
    {
        "flight_en_name": "Flying Colours Airlines", 
        "flight_id": "FLY"
    }, 
    {
        "flight_en_name": "GB Airways", 
        "flight_id": "GBL"
    }, 
    {
        "flight_en_name": "DAC Air", 
        "flight_id": "GCP"
    }, 
    {
        "flight_en_name": "Lufthansa Cargo", 
        "flight_id": "GEC"
    }, 
    {
        "flight_en_name": "Taifun", 
        "flight_id": "GIG"
    }, 
    {
        "flight_en_name": "Air Club International", 
        "flight_id": "HB"
    }, 
    {
        "flight_en_name": "Business Air", 
        "flight_id": "II"
    }, 
    {
        "flight_en_name": "Spring Airlines Japan", 
        "flight_id": "IJ"
    }, 
    {
        "flight_en_name": "Mango", 
        "flight_id": "JE"
    }, 
    {
        "flight_en_name": "Kyrgyastan-EX", 
        "flight_id": "K2"
    }, 
    {
        "flight_en_name": "ALS", 
        "flight_id": "K4"
    }, 
    {
        "flight_en_name": "Khazar Airlines", 
        "flight_id": "KHR"
    }, 
    {
        "flight_en_name": "Kiwi International Airlines", 
        "flight_id": "KP"
    }, 
    {
        "flight_en_name": "Lineas Aereas Suramericanas", 
        "flight_id": "LAU"
    }, 
    {
        "flight_en_name": "Balkan Bulgarian Airlines", 
        "flight_id": "LZ"
    }, 
    {
        "flight_en_name": "Modiluft", 
        "flight_id": "M9"
    }, 
    {
        "flight_en_name": "Millardair", 
        "flight_id": "MAB"
    }, 
    {
        "flight_en_name": "Peach", 
        "flight_id": "MM"
    }, 
    {
        "flight_en_name": "Maina Air", 
        "flight_id": "MNI"
    }, 
    {
        "flight_en_name": "Maersk Air", 
        "flight_id": "MSK"
    }, 
    {
        "flight_en_name": "JAL Express", 
        "flight_id": "N8"
    }, 
    {
        "flight_en_name": "TNT International Aviation Services", 
        "flight_id": "NTR"
    }, 
    {
        "flight_en_name": "Petroleum Air Services", 
        "flight_id": "PAS"
    }, 
    {
        "flight_en_name": "Paradise Island Aielines", 
        "flight_id": "PDI"
    }, 
    {
        "flight_en_name": "Qatar Airways", 
        "flight_id": "Q7"
    }, 
    {
        "flight_en_name": "SmartWings", 
        "flight_id": "QS"
    }, 
    {
        "flight_en_name": "Armenian International Airlines", 
        "flight_id": "R3"
    }, 
    {
        "flight_en_name": "Aéroservicios Carabobo", 
        "flight_id": "R7"
    }, 
    {
        "flight_en_name": "BAC Express Airlines", 
        "flight_id": "RPX"
    }, 
    {
        "flight_en_name": "Intercontinental de Aviatcion", 
        "flight_id": "RS"
    }, 
    {
        "flight_en_name": "Santa Barbara", 
        "flight_id": "S3"
    }, 
    {
        "flight_en_name": "EIK Airways", 
        "flight_id": "S8"
    }, 
    {
        "flight_en_name": "Sabang", 
        "flight_id": "SMC"
    }, 
    {
        "flight_en_name": "Star Air", 
        "flight_id": "SRR"
    }, 
    {
        "flight_en_name": "Sunways Airlines", 
        "flight_id": "SWY"
    }, 
    {
        "flight_en_name": "Aeroexo", 
        "flight_id": "SX"
    }, 
    {
        "flight_en_name": "TACA Peru", 
        "flight_id": "T0"
    }, 
    {
        "flight_en_name": "TABA", 
        "flight_id": "T2"
    }, 
    {
        "flight_en_name": "Titan Airways", 
        "flight_id": "T4"
    }, 
    {
        "flight_en_name": "Pacific Airlines", 
        "flight_id": "T5"
    }, 
    {
        "flight_en_name": "TransAer", 
        "flight_id": "T8"
    }, 
    {
        "flight_en_name": "US Airways Shuttle", 
        "flight_id": "TB"
    }, 
    {
        "flight_en_name": "Tolair Services", 
        "flight_id": "TOL"
    }, 
    {
        "flight_en_name": "Scoot", 
        "flight_id": "TZ"
    }, 
    {
        "flight_en_name": "USA Jet Airlines", 
        "flight_id": "U7"
    }, 
    {
        "flight_en_name": "KLMuk", 
        "flight_id": "UK"
    }, 
    {
        "flight_en_name": "Leisure Intenational Airways", 
        "flight_id": "ULE"
    }, 
    {
        "flight_en_name": "British International Helicopters", 
        "flight_id": "UR"
    }, 
    {
        "flight_en_name": "Venus airlines", 
        "flight_id": "V4"
    }, 
    {
        "flight_en_name": "Vnukovo Airlines", 
        "flight_id": "V5"
    }, 
    {
        "flight_en_name": "Viscount Air Service", 
        "flight_id": "VCT"
    }, 
    {
        "flight_en_name": "Air Burkina", 
        "flight_id": "VH"
    }, 
    {
        "flight_en_name": "Zantop International Airlines", 
        "flight_id": "VK"
    }, 
    {
        "flight_en_name": "Western Pacific Airlines", 
        "flight_id": "W7"
    }, 
    {
        "flight_en_name": "WDL Aviation", 
        "flight_id": "WDL"
    }, 
    {
        "flight_en_name": "Volaris", 
        "flight_id": "Y4"
    }, 
    {
        "flight_en_name": "Iran Asseman", 
        "flight_id": "Y7"
    }, 
    {
        "flight_en_name": "Zimbabwe flyafrica.com", 
        "flight_id": "Z7"
    }, 
    {
        "flight_en_name": "Zairean Airlines", 
        "flight_id": "ZAR"
    }, 
    {
        "flight_en_name": "Air Europa", 
        "flight_id": "UX"
    }, 
    {
        "flight_en_name": "Nextjet", 
        "flight_id": "2N"
    }, 
    {
        "flight_en_name": "Air Arabia Maroc", 
        "flight_id": "3O"
    }, 
    {
        "flight_en_name": "Interjet", 
        "flight_id": "4O"
    }, 
    {
        "flight_en_name": "Onur Air", 
        "flight_id": "8Q"
    }, 
    {
        "flight_en_name": "HOP!", 
        "flight_id": "A5"
    }, 
    {
        "flight_en_name": "Norwegian Long Haul", 
        "flight_id": "D8"
    }, 
    {
        "flight_en_name": "Darwin Airline SA", 
        "flight_id": "F7"
    }, 
    {
        "flight_en_name": "Hahn Air Systems", 
        "flight_id": "H1"
    }, 
    {
        "flight_en_name": "Pegasus Airlines", 
        "flight_id": "PC"
    }, 
    {
        "flight_en_name": "SATA Internacional", 
        "flight_id": "S4"
    }, 
    {
        "flight_en_name": "Eastern Airways", 
        "flight_id": "T3"
    }, 
    {
        "flight_en_name": "Twin Jet", 
        "flight_id": "T7"
    }, 
    {
        "flight_en_name": "Volotea", 
        "flight_id": "V7"
    }, 
    {
        "flight_en_name": "Cygnus Air", 
        "flight_id": "XG"
    }, 
    {
        "flight_en_name": "GMG Airlines", 
        "flight_id": "Z5"
    }, 
    {
        "flight_en_name": "Novoair", 
        "flight_id": "VQ"
    }, 
    {
        "flight_en_name": "Golden Myanmar Airlines", 
        "flight_id": "Y5"
    }, 
    {
        "flight_en_name": "AirAsia India", 
        "flight_id": "I5"
    }, 
    {
        "flight_en_name": "GoAir", 
        "flight_id": "G8"
    }, 
    {
        "flight_en_name": "Citilink", 
        "flight_id": "QG"
    }, 
    {
        "flight_en_name": "Eastar Jet", 
        "flight_id": "ZE"
    }, 
    {
        "flight_en_name": "Blue Air", 
        "flight_id": "0B"
    }, 
    {
        "flight_en_name": "Iberia Express", 
        "flight_id": "I2"
    }, 
    {
        "flight_en_name": "Corendon Airlines", 
        "flight_id": "XC"
    }, 
    {
        "flight_en_name": "Bahrain Air", 
        "flight_id": "BN"
    }, 
    {
        "flight_en_name": "Jazeera Airways", 
        "flight_id": "J9"
    }, 
    {
        "flight_en_name": "Air Arabia", 
        "flight_id": "G9"
    }, 
    {
        "flight_en_name": "Allegiant Air", 
        "flight_id": "G4"
    }, 
    {
        "flight_en_name": "Air Arabia Egypt", 
        "flight_id": "E5"
    }, 
    {
        "flight_en_name": "Solaseed Air", 
        "flight_id": "6J"
    }
]