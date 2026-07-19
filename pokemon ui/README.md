# Pokémon UI

A simple desktop app built with **Tkinter** that lets you search for any Pokémon by name and view its stats, type, ability, height, and weight — pulled live from [PokeAPI](https://pokeapi.co/).

<!-- Add a screenshot or GIF here, e.g. -->
<!-- ![screenshot](assets/screenshot.png) -->

## Features

- 🔍 Search any Pokémon by name
- 📛 Displays name, Pokédex ID, type, and primary ability
- ❤️ Shows HP, Attack, and Defense base stats
- 📏 Shows height and weight
- 🖼️ Fetches and displays the official sprite image

## Requirements

- Python 3.8+
- Dependencies listed in `requirements.txt`

## Installation

```bash
git clone https://github.com/<your-username>/pokemon-ui.git
cd pokemon-ui
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

Type a Pokémon's name (e.g. `pikachu`) into the search box and hit **Search**.

## How it works

The app calls the PokeAPI endpoint `https://pokeapi.co/api/v2/pokemon/{name}` and parses the JSON response for sprite, stats, type, and ability data. The sprite image is fetched separately and rendered using Pillow (`PIL`).

## Known limitations

- Only shows the Pokémon's **primary** type and ability (some Pokémon have more than one of each)
- Requires an internet connection — no offline/cached mode
- Case-insensitive, but doesn't currently handle typos or suggest corrections

## License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.

Pokémon and PokeAPI data are property of their respective owners; this project is an unofficial fan tool for educational purposes.
