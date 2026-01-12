from tkinter import *
from tkinter import ttk
import requests



def get_data():
    city = city_name.get()
    key = "bcf87f2767b9837b4e3b041285303e7a"
    url = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+key
    data = requests.get(url).json()
    climate_o.config(text=data["weather"][0]["main"])
    description_o.config(text=data["weather"][0]["description"])
    temp_o.config(text=str(data["main"]["temp"]-273.15))
    pressure_o.config(text=data["main"]["pressure"])

win = Tk()
win.title("JD WEATHER App")
win.config(bg="#DEF112")
win.geometry("500x500")
name_lable = Label(win,text= "Jaydip's Weather App 🌞", font= ("Times New Roman",30,"bold"))
name_lable.place(x=25 , y=50 , height= 50 , width= 450)  

list_name = [
    "Andhra Pradesh",
    "Arunachal Pradesh",
    "Assam",
    "Bihar",
    "Chhattisgarh",
    "Goa",
    "Gujarat",
    "Haryana",
    "Himachal Pradesh",
    "Jharkhand",
    "Karnataka",
    "Kerala",
    "Madhya Pradesh",
    "Maharashtra",
    "Manipur",
    "Meghalaya",
    "Mizoram",
    "Nagaland",
    "Odisha",
    "Punjab",
    "Rajasthan",
    "Sikkim",
    "Tamil Nadu",
    "Telangana",
    "Tripura",
    "Uttar Pradesh",
    "Uttarakhand",
    "West Bengal"
]

city_name = StringVar()
comm = ttk.Combobox(win,text= "Jaydip's Weather App 🌞",values=list_name, font= ("Times New Roman",20,"bold"),textvariable=city_name)
comm.place(x=25 , y=120 , height= 50 , width= 450)  

#Description labels
climate = Label(win,text= "Climate", font= ("Times New Roman",20,"bold"))
climate.place(x=25 , y=260 , height= 50 , width= 200)  

description = Label(win,text= "Description", font= ("Times New Roman",20,"bold"))
description.place(x=25 , y=320 , height= 50 , width= 200)  

temp = Label(win,text= "Temperature", font= ("Times New Roman",20,"bold"))
temp.place(x=25 , y=380 , height= 50 , width= 200)  

pressure = Label(win,text= "Pressure", font= ("Times New Roman",20,"bold"))
pressure.place(x=25 , y=440 , height= 50 , width= 200) 

#Output labels
climate_o = Label(win,text= "", font= ("Times New Roman",20,"bold"))
climate_o.place(x=250 , y=260 , height= 50 , width= 200)  

description_o = Label(win,text= "", font= ("Times New Roman",20,"bold"))
description_o.place(x=250 , y=320 , height= 50 , width= 200)  

temp_o = Label(win,text= "", font= ("Times New Roman",20,"bold"))
temp_o.place(x=250 , y=380 , height= 50 , width= 200)  

pressure_o = Label(win,text= "", font= ("Times New Roman",20,"bold"))
pressure_o.place(x=250 , y=440 , height= 50 , width= 200) 

done_button = Button(win,text= "Done", font= ("Times New Roman",20,"bold"),command=get_data)
done_button.place(x=180 , y=190 , height= 50 , width= 150)  
win.mainloop()