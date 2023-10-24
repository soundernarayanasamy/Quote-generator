import tkinter
import requests

def quote():
    response = requests.get(url="https://api.kanye.rest")
    json_quote = (response.json()["quote"])
    canvas.itemconfig(quotes, text=json_quote)

window = tkinter.Tk()
window.title("Kaney Says")
window.config(padx=20, pady=20)
canvas = tkinter.Canvas(width=300, height=414)
background_image = tkinter.PhotoImage(file="background.png")
canvas.create_image(150, 212, image=background_image)
quotes = canvas.create_text(150, 212, text="QUOTES", width=250, font=("Arial", 20, "bold"))
canvas.grid(row=0, column=0)

button_image = tkinter.PhotoImage(file="kanye.png")
button = tkinter.Button(image=button_image, command=quote)
button.grid(row=1, column=0)


window.mainloop()
