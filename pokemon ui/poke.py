
search_button = tk.Button(root, text="search", command=search_pokemon)
search_button.pack(anchor="w", padx="20")

image_label = tk.Label(root, bg="#ee1515")
image_label.pack(pady=20)

result_label = tk.Label(root, text="", bg="#ee1515", justify="left", font=("Impact", 12), width=30)
result_label.pack(anchor="nw")



image_label = tk.Label(root, bg="#FFFFFF")
image_label.pack(pady=20)

info_frame = tk.Frame(root, bg="#333333", padx=20, pady=20)
info_frame.pack(pady=20)

result_label = tk.Label(info_frame, text="", font=("Impact", 13), fg="white", bg="#333333", justify="left", width=30)
result_label.pack(anchor="nw")