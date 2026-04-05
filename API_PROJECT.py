import tkinter as tk
import requests
import matplotlib.pyplot as plt
def get_health_data():
    country = entry.get()

    url = f"https://disease.sh/v3/covid-19/countries/{country}"

    response = requests.get(url)
    data = response.json()

    cases = data["cases"]
    deaths = data["deaths"]
    recovered = data["recovered"]

    result_label.config(text=
        f"Country: {country}\n"
        f"Cases: {cases}\n"
        f"Deaths: {deaths}\n"
        f"Recovered: {recovered}"
    )

    show_graph(cases, deaths, recovered)

def show_graph(cases, deaths, recovered):
    labels = ["Cases", "Deaths", "Recovered"]
    values = [cases, deaths, recovered]

    plt.bar(labels, values)
    plt.title("Health Statistics")
    plt.show()

def get_war_news():
    country = entry.get()
    url = f"https://newsapi.org/v2/everything?q={country}&sortBy=publishedAt&language=en&apiKey=053db978e7c24c9f8119ce9fcaef6d09"

    response = requests.get(url)
    data = response.json()

    articles = data["articles"][:3]

    news_text = "Latest News:\n\n"

    for article in articles:
        news_text += "• " + article["title"] + "\n\n"

    news_label.config(text=news_text)

window = tk.Tk()

window.title("Global War & Health Dashboard")

window.geometry("450x400")

title = tk.Label(window,text="Global Crisis Monitoring System",font=("Arial",16))
title.pack(pady=10)

entry = tk.Entry(window,width=30)
entry.pack(pady=10)

health_button = tk.Button(window,text="Get Health Data",command=get_health_data)
health_button.pack(pady=5)

war_button = tk.Button(window,text="Get War News",command=get_war_news)
war_button.pack(pady=5)

result_label = tk.Label(window,text="")
result_label.pack(pady=10)

news_label = tk.Label(window,text="",wraplength=400)
news_label.pack(pady=10)

window.mainloop()