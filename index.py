import requests as req
import tkinter as tk
from tkinter import messagebox

def get_weather(city):
    text = city
    API_TOKEN = "5dfac86ff36fdc0a5506a69ae0fbe7f4"
    URL = "http://api.openweathermap.org/data/2.5/weather?"
    COMPLETE_URL = f"{URL}q={text}&appid={API_TOKEN}&units=metric"

    response = req.get(COMPLETE_URL)
    results = response.json()


    if results['cod'] == 200:
        weather_info = f"city: {text}\ndescription: {results['weather'][0]['description']}\ntemp: {results['main']['temp']}\nhumidity: {results['main']['humidity']}"
    else:
        weather_info = "error in request"
    return weather_info

app = tk.Tk()
app.title("برنامه آب و هوا")
app.geometry("300x300")

lable = tk.Label(app, text="Please enter city name for sub box")
lable.pack(padx=10,pady=10)

En = tk.Entry(app)
En.pack(padx=10, pady=10)

def get_weather_defs():
    city = En.get()
    if city:
        weather = get_weather(city=city)
        messagebox.showinfo(f"{city}اطلاعات هواشناسی شهر",weather)
    else:
        messagebox.showwarning(f"{city}اطلاعات هواشناسی شهر",weather)

button = tk.Button(app, text="click", command=get_weather_defs)
button.pack(padx=10, pady=10)

app.mainloop()