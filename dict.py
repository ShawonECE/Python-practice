thisdict = {
  "brand": "Ford",
  "electric": False,
  "model": "Mustang",
  "year": 1964,
  #"color": "red"
}
thisdict["year"] = 2018
thisdict["color"] = "red"
thisdict.pop("brand")
print(thisdict)
print(thisdict["model"])
print(thisdict.keys())
print(thisdict.values())
print(thisdict.items())
#if "model" in thisdict:
#  print("Yes, 'model' is one of the keys in the thisdict dictionary")
#else:
#    print("No, 'model' is not one of the keys in the thisdict dictionary")
myfamily = {
    {
    "name" : "Emil",
    "year" : 2004
    },
    {
    "name" : "Tobias",
    "year" : 2007
    },
    {
    "name" : "Linus",
    "year" : 2011
    }
}
print(myfamily)
#print(type(myfamily))