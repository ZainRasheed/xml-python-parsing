# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
for data pre-processing of VHQ data
"""

import pandas as pd
import xml.etree.ElementTree as et



xml_raw_data = """<?xml version="1.0"?>
<catalog>
   <book id="bk101">
      <author>Gambardella, Matthew</author>
      <title>XML Developer's Guide</title>
      <genre>Computer</genre>
      <price>44.95</price>
      <publish_date>2000-10-01</publish_date>
      <description>An in-depth look at creating applications 
      with XML.</description>
   </book>
   <book id="bk102">
      <author>Ralls, Kim</author>
      <title>Midnight Rain</title>
      <genre>Fantasy</genre>
      <price>5.95</price>
      <publish_date>2000-12-16</publish_date>
      <description>A former architect battles corporate zombies, 
      an evil sorceress, and her own childhood to become queen 
      of the world.</description>
   </book>
   <book id="bk103">
      <author>Corets, Eva</author>
      <title>Maeve Ascendant</title>
      <genre>Fantasy</genre>
      <price>5.95</price>
      <publish_date>2000-11-17</publish_date>
      <description>After the collapse of a nanotechnology 
      society in England, the young survivors lay the 
      foundation for a new society.</description>
   </book>
   <book id="bk104">
      <author>Corets, Eva</author>
      <title>Oberon's Legacy</title>
      <genre>Fantasy</genre>
      <price>5.95</price>
      <publish_date>2001-03-10</publish_date>
      <description>In post-apocalypse England, the mysterious 
      agent known only as Oberon helps to create a new life 
      for the inhabitants of London. Sequel to Maeve 
      Ascendant.</description>
   </book>
</catalog>"""

xml_data = et.fromstring(xml_raw_data)
#Reading the xml from the string vairable

xml_data_root = xml_data[0].attrib
#accessing the first child of xml

heading_list = []
#creating a epty list to get the header values for the final dataframe

for x in xml_data[0]:
    heading_list.append(x.tag)
#extracting the tag to assign the headers to the dataframe
    
#xml_dataframe = pd.DataFrame(columns = [''])
xml_dataframe = pd.DataFrame(columns = heading_list)
#Creating a dataframe with headers from xml tags

for xml in xml_data:
    print(xml.tag)
    print(xml.find('author').text)
#To access every child from the xml and to acces childs content indivudially
    
for xml in xml_data:
    for x in xml:
        print(x.tag)
#To access the rooted tags
        
"""for xml in xml_data:
    author = 
    title = """
i=0
for xml in xml_data:
    xml_dataframe.loc[i] = [xml.find('author').text]+[xml.find('title').text]+[xml.find('genre').text]+[xml.find('publish_date').text]+[xml.find('price').text]+[xml.find('description').text]
    i=i+1
#to append a row into the dataframe with 6 columns