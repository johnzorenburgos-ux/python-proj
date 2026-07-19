import tkinter as tk
from tkinter import ttk
import requests
from PIL import Image, ImageTk
from io import BytesIO

root = tk.Tk()

icon = tk.PhotoImage(file="pokeball.png")
pokeball = tk.PhotoImage(file="pokeball2.png")
root.iconphoto(True, icon)
root.title("Pokemon ui")
root.geometry("600x800")
root.config(bg="#222224")

pokeball_label = tk.Label(
    root,
    image=pokeball,
    bg="#222224"
)

pokeball_label.place(
    relx=0.5,
    rely=0.5,
    anchor="center"
)


            #label or header
title_label = tk.Label(root, text=" Pokemon UI", font=("Impact", 20), fg="#ee1515", bg="#222224")
title_label.pack(pady=25)

            #input
pokemon_name = tk.Entry(root, width=20, font=("Impact", 14))
pokemon_name.pack(anchor="w", padx="20", pady="10")

def search_pokemon():
                pokemon_mane = pokemon_name.get().lower()

                url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_mane}"

                response =requests.get(url)

                if response.status_code == 200:

                    data = response.json()
                    image_url = data["sprites"]["front_default"]
                    image_response = requests.get(image_url)

                    image = Image.open(BytesIO(image_response.content))
                    image = image.resize((250, 250))
                    pokemon_image = ImageTk.PhotoImage(image)
                    image_label.config(image=pokemon_image)
                    image_label.image = pokemon_image
                    


                    name = data["name"].title()
                    pokemon_id = data["id"]
                    height = data["height"] / 10
                    weight = data["weight"] / 10
                    pokemon_type = data["types"][0] ["type"]["name"].title()
                    ability = data["abilities"][0]  ["ability"]["name"].title()
                    hp = data["stats"][0]["base_stat"]
                    attack = data["stats"][1]["base_stat"]
                    defense = data["stats"][2]["base_stat"]
                
                

                    result_label.config(
                    text=(
                    
                    f"📛Name: {name}\n"
                    f"🆔 ID: #{pokemon_id}\n\n"
                    f"⚡Type: {pokemon_type}\n"
                    f"✨Ability: {ability}\n\n"
                    f"❤️HP: {hp}\n"
                    f"⚔️Attack: {attack}\n"
                    f"🧱Defense:{defense}\n\n"
                    f"📏Height: {height} m\n"
                    f"⚖️Weight: {weight} kg"))

         
                    
                else:
                    result_label.config(text="pokemon not found")


search_button = tk.Button(root, text="🔍 Search", font=("Impact",10), bg="#3B4CCA",
    fg="white",
    relief="flat",
    cursor="hand2", command=search_pokemon)
search_button.pack(anchor="w", padx=20)


card_frame = tk.Frame(
    root,
    bg= "#ee1515",
    padx=25,
    pady=25,
    relief="groove",
    bd=3,
    highlightbackground="#ee1515", 
    highlightthickness=2
)
card_frame.pack(pady=20)

image_label = tk.Label(
    card_frame,
    bg="#ee1515"
)
image_label.pack(pady=(0, 15))

result_label = tk.Label(
    card_frame,
    text="Search for a Pokémon!",
    font=("Arial", 14),
    fg="white",
    bg="#ee1515",
    justify="left"
)


result_label.pack()
root.mainloop()