#!/usr/bin/python
#coding=utf-8

City_2_country = {
    "CPH" : "DK",
    "CKG" : "CN",
    "AGH" : "SE",
    "BGO" : "NO",
    "HEL" : "FI",
    "SIA" : "CN",
    "YMQ" : "CA",
    "AGP" : "ES",
    "WAS" : "US",
    "MIA" : "US",
    "BRAU" : "DE",
    "BWI" : "US",
    "TAO" : "CN",
    "MIL" : "IT",
    "HAJ" : "DE",
    "HAK" : "CN",
    "HOU" : "US",
    "WAS" : "US",
    "BUF" : "US",
    "LHW" : "CN",
    "LON" : "GB",
    "SIA" : "CN",
    "PHL" : "US",
    "WUX" : "CN",
    "YEA" : "CA",
    "PHX" : "US",
    "LAX" : "US",
    "MAD" : "ES",
    "LXA" : "CN",
    "WUH" : "CN",
    "BRU" : "BE",
    "MAN" : "GB",
    "TSN" : "CN",
    "VCE" : "IT",
    "BER" : "DE",
    "DTT" : "US",
    "PIS" : "FR",
    "VLC" : "ES",
    "BUF" : "US",
    "BUD" : "HU",
    "GRQ" : "NL",
    "BLQ" : "IT",
    "SXB" : "FR",
    "GRX" : "ES",
    "FOC" : "CN",
    "HOU" : "US",
    "PSA" : "IT",
    "MIL" : "IT",
    "LON" : "GB",
    "INN" : "AT",
    "ANR" : "BE",
    "OPO" : "PT",
    "CSX" : "CN",
    "KMG" : "CN",
    "CTU" : "CN",
    "BCN" : "ES",
    "CORS" : "FR",
    "GLA" : "GB",
    "HNL" : "US",
    "BJS" : "CN",
    "BSL" : "CH",
    "VRN" : "IT",
    "ROM" : "IT",
    "HET" : "CN",
    "XMN" : "CN",
    "WAW" : "PL",
    "PAR" : "FR",
    "MMA" : "SE",
    "PAR" : "FR",
    "EDI" : "GB",
    "YTO" : "CA",
    "PRIN" : "CA",
    "SBA" : "US",
    "YYC" : "CA",
    "CHI" : "US",
    "LEXM" : "FR",
    "YYJ" : "CA",
    "DIJO" : "FR",
    "CAN" : "CN",
    "HAM" : "DE",
    "PGA" : "US",
    "SOU" : "GB",
    "MONT" : "US",
    "LON" : "GB",
    "STO" : "SE",
    "STR" : "DE",
    "YOW" : "CA",
    "ZRH" : "CH",
    "ANNE" : "FR",
    "BFS" : "GB",
    "BHX" : "GB",
    "NCL" : "GB",
    "INC" : "CN",
    "NCE" : "FR",
    "STO" : "SE",
    "NYC" : "US",
    "LIL" : "FR",
    "DRES" : "DE",
    "BOS" : "US",
    "NAP" : "IT",
    "LIS" : "PT",
    "BJS" : "CN",
    "BOD" : "FR",
    "FNI" : "FR",
    "PRG" : "CZ",
    "SAN" : "US",
    "BER" : "DE",
    "LYS" : "FR",
    "NNG" : "CN",
    "LBA" : "GB",
    "SIEN" : "IT",
    "KHN" : "CN",
    "SVQ" : "ES",
    "YVR" : "CA",
    "URC" : "CN",
    "MRS" : "FR",
    "BFS" : "GB",
    "LPL" : "GB",
    "YQB" : "CA",
    "HRB" : "CN",
    "VICE" : "IT",
    "TYN" : "CN",
    "VIE" : "AT",
    "SFO" : "US",
    "NGB" : "CN",
    "FLR" : "IT",
    "FLL" : "US",
    "DEN" : "US",
    "THEX" : "NL",
    "BRUG" : "BE",
    "SZX" : "CN",
    "OSL" : "NO",
    "CANN" : "FR",
    "AMS" : "NL",
    "DLC" : "CN",
    "TRN" : "IT",
    "FIRA" : "GR",
    "SHA" : "CN",
    "MONTX" : "CA",
    "SHE" : "CN",
    "NIAGA" : "CA",
    "NYC" : "US",
    "OXF" : "GB",
    "SYX" : "CN",
    "MPL" : "FR",
    "AVIG" : "FR",
    "LAS" : "US",
    "HGH" : "CN",
    "LUX" : "LU",
    "WINDSO" : "CA",
    "ATH" : "GR",
    "IST" : "TR",
    "YHZ" : "CA",
    "MUC" : "DE",
    "LUG" : "CH",
    "ATLA" : "US",
    "HFE" : "CN",
    "XNN" : "CN",
    "CGO" : "CN",
    "CGN" : "DE",
    "SHA" : "CN",
    "CGQ" : "CN",
    "NUE" : "DE",
    "FRA" : "DE",
    "SEA" : "US",
    "PDX" : "US",
    "SJW" : "CN",
    "SJC" : "US",
    "DUS" : "DE",
    "REK" : "IS",
    "LEJ" : "DE",
    "BRS" : "GB",
    "BRN" : "CH",
    "BRE" : "DE",
    "ROM" : "IT",
    "YWG" : "CA",
    "REK" : "IS",
    "BER" : "DE",
    "KWE" : "CN",
    "DAT" : "CN",
    "VCE" : "IT",
    "BADE" : "DE",
    "GVA" : "CH",
    "GOA" : "IT",
    "HOU" : "US",
    "TNA" : "CN",
    "GOT" : "SE",
    "SLC" : "US",
    "ORL" : "US",
    "SZG" : "AT",
    "NKG" : "CN",
    "NYC" : "US",
    "YGK" : "CA",
    "YELL" : "CA",
    "GASP" : "CA",
    "LON" : "GB",
}

