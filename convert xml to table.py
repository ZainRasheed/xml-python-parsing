# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
for data pre-processing of VHQ data
"""

import pandas as pd
import xml.etree.ElementTree as et



"""VER 1.0"""
#This method iterates through the first child of every first tag ----> WITHOUT FOR LOOP == iteratethroughttagsV1(xml_tag[0])
#This method iterates through all the child of every tag ----> WITH FOR LOOP == iteratethroughttagsV1(xml)
#ERROR : Dosen't acces the initial tag
def iteratethroughttagsV1(xml_tag):
#DOESN'T WORK    if (xml_tag.iter()):
    if(xml_tag.find("./") != None):
        for xml in xml_tag:
            print("tag name>>>> "+ xml_tag.tag+"..... has child")
            print(xml_tag.find("./"))
            iteratethroughttagsV1(xml)
    else:
        print("tag name"+ xml_tag.tag+"..... no child")


"""VER 1.1"""
#This method iterates through the first child of every first tag ----> WITHOUT FOR LOOP == iteratethroughttagsV1(xml_tag[0])
#This method iterates through all the child of every tag ----> WITH FOR LOOP == iteratethroughttagsV1(xml)
#ERROR : Dosen't acces the initial tag
def iteratethroughttagsV2(xml_tag):
#DOESN'T WORK    if (xml_tag.iter()):
    if(xml_tag.find("./") != None):
        for xml in xml_tag:
            print("tag name>>>> "+ xml_tag.tag+"..... has child")
            print(xml_tag.find("./"))
            iteratethroughttagsV2(xml)
    else:
        print("tag name"+ xml_tag.tag+"..... no child")


"""VER 1.3"""
#This method iterates through the first child of every first tag ----> WITHOUT FOR LOOP == iteratethroughttagsV1(xml_tag[0])
#This method iterates through all the child of every tag ----> WITH FOR LOOP == iteratethroughttagsV1(xml)
def iteratethroughttagsV3(xml_tag):
#DOESN'T WORK    if (xml_tag.iter()):
    if(xml_tag.find("./") != None):
        print("tag name>>>> "+ xml_tag.tag+"..... has child")
        print(xml_tag.find("./"))
        for xml in xml_tag:
            iteratethroughttagsV3(xml_tag[0])
    else:
        print("tag name"+ xml_tag.tag+"..... no child")        
        

"""VER 2"""        
#This method iterates through the first child of every first tag ----> WITHOUT FOR LOOP == iteratethroughttagsV1(xml_tag[0])
#This method iterates through all the child of every tag ----> WITH FOR LOOP == iteratethroughttagsV1(xml)
#Reads all the arrtibutes if all the tags
def iteratetagsandgetattr(xml_tag):
    for keyy, vall in xml_tag.items():
        print(keyy, vall)
        print("\n")
    #for xml_key in xml_tag.attrib():
        #print(xml_key, xml_tag.get(xml_key))
        #print("\n")
    #xml_tag.keys()
    #xml_tag.items()
    print("---- ", xml_tag.attrib)
    if(xml_tag.find("./") != None):
        print("-------------------------------------------------\n")
        for xml in xml_tag:
            iteratetagsandgetattr(xml)
    else:
        print("tag name"+ xml_tag.tag+"..... no child")
        print("-------------------------------------------------\n")
        
        
"""VER 3"""        
#This method iterates through the first child of every first tag ----> WITHOUT FOR LOOP == iteratethroughttagsV1(xml_tag[0])
#This method iterates through all the child of every tag ----> WITH FOR LOOP == iteratethroughttagsV1(xml)
#Reads all the arrtibutes if all the tags
#Generates a dataframe of all those attribute tags

vhq_df = pd.DataFrame()
def makedataframeofxml(xml_tag, df_col_name = "ROOT", xml_dictionary = {}):
    df_col_name = df_col_name+"_"+xml_tag.tag
    for keyy, vall in xml_tag.items():
        print(keyy, vall)
        xml_dictionary.update({df_col_name+"_"+str(keyy):vall})
        print(xml_dictionary)
        print("\n")
    if(xml_tag.find("./") != None):
        print("-------------------------------------------------\n")
        for xml in xml_tag:
            makedataframeofxml(xml, df_col_name, xml_dictionary)
    else:
        global vhq_df
        vhq_df = vhq_df.append(xml_dictionary, ignore_index = True)
        print("tag name"+ xml_tag.tag+"..... no child")
        print("-------------------------------------------------\n")
    #POP elements from dict ... list+col_name recursively +pop all
    temp_keys = [df_col_name +"_"+ s for s in xml_tag.keys()]
    [xml_dictionary.pop(key) for key in temp_keys]
    

vhq_raw_xml = """<DeviceMessage mainnnnn="blah">
    <Header MessageType="Status" Version="02.11.0008" CommunicationId="24" MessageId="6" CustomerId="AustraliaPost" IPAddress="192.168.0.15" HBFrequency="300" LocalTime="1518598951" Nonce="1518575661">
        <Initiator Type="Terminal1">
            <Identifier ModelNumber="V200C PLUS" SerialNumber="401-100-328" UniqueDeviceId="488" PartNum="M420-053-04-DMO-4"/>
            <Identifier ModelNumber="V201C PLUS" SerialNumber="401-100-329" UniqueDeviceId="488" PartNum="M420-053-04-DMO-4"/>
        </Initiator>
        <Initiator Type="Terminal2">
            <Identifier ModelNumber="V200C PLUS" SerialNumber="401-100-328"/>
            <Identifier ModelNumber="V201C PLUS" SerialNumber="401-100-329"/>
        </Initiator>
    </Header>
    <Content>
        <OperationsResults ServerMessageType="Event"/>
    </Content>
    </DeviceMessage>"""


dictionary = {}
dictionary.update({'col_a':10, 'col_b':100, 'col_c':1000})
dictionary.update({"var1":222})
dictionary.update({"var2":"333"})
dictionary.update({"var2":"786"})


df = pd.DataFrame()
df = df.append({'col_a':5,'col_b':10}, ignore_index=True)
df = df.append({'col_a':1,'col_b':100}, ignore_index=True)
df = df.append({'col_a':32,'col_b':999}, ignore_index=True)
df = df.append({'col_a':32,'col_b':999,'col_c':9909}, ignore_index=True)
df = df.append({'col_a':320,'col_c':666}, ignore_index=True)
df = df.append(dictionary, ignore_index=True)
df = df.append(dictionary, ignore_index=True)


vhq_xml = et.fromstring(vhq_raw_xml)
#iteratethroughttagsV1(vhq_xml)
#iteratetagsandgetattr(vhq_xml)
makedataframeofxml(vhq_xml)
#print(vhq_df)
#vhq_df.info()
#vhq_df.describe()