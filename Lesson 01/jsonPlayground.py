#!/usr/bin/python

import json
import requests


BASE_URL = "http://musicbrainz.org/ws/2/"
ARTIST_URL = BASE_URL + "artist/"

query_type = {  "simple": {},
                "atr": {"inc": "aliases+tags+ratings"},
                "aliases": {"inc": "aliases"},
                "releases": {"inc": "releases"}}


def query_site(url, params, uid="", fmt="json"):
    params["fmt"] = fmt
    r = requests.get(url + uid, params=params)
    print "requesting", r.url

    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        r.raise_for_status()


def query_by_name(url, params, name):
    params["query"] = "artist:" + name
    return query_site(url, params)


def pretty_print(data, indent=4):
    if type(data) == dict:
        print json.dumps(data, indent=indent, sort_keys=True)
    else:
        print data


def main():


    #Question 01: How many bands named "First aid kit"

    results = query_by_name(ARTIST_URL, query_type["simple"], "First Aid Kit")
    count = 0
    for item in results["artists"]:
	if item["name"].lower() == 'first aid kit':
		count = count +1

    print "There is ",count," bands named 'First Aid Kit'"    
    #Answer is 2


    #Question 02: Begin area name for Queen
    
    results = query_by_name(ARTIST_URL, query_type["simple"], "Queen")
    pretty_print(results)
    
    for item in results["artists"]:
	if "begin-area" in item.keys():
		print "Begin area name for Queen is ",item["begin-area"]["name"]
	    
    #Answer is London, Gorizia, Newark

    #Question 03: Spanish Alias for Bettles
    results = query_by_name(ARTIST_URL, query_type["simple"], "Beatles")
    pretty_print(results)
    
    for item in results["artists"][0]["aliases"]:
	if item["locale"] == 'es':
     		print "Spanish Alias for bettles is ", item["name"]

    #Answer is Los Beatles

 
    #Question 04 Nirvana Disambiguation

    results = query_by_name(ARTIST_URL, query_type["simple"], "Nirvana")
    pretty_print(results)

    for item in results["artists"]:
	if (item["name"].lower() == 'nirvana') and "disambiguation" in item.keys():
			print "Nisvanas' disambiguation is ",item["disambiguation"]

    #Answer is 90s US grunge band, 60s band form the UK, Early 1980's Finnish punk band
 
    #Question 05 When was one direction formed

    results = query_by_name(ARTIST_URL, query_type["simple"], "One Direction")
    pretty_print(results)
    
    #Answer is 2010

if __name__ == '__main__':
    main()
