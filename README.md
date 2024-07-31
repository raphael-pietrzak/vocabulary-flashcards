
# Vocabulary Flash Card Generator

## Overview

The Vocabulary Flash Card Generator is an application that utilizes AI to generate vocabulary flashcards. The application takes a theme as input, generates a list of 10 vocabulary words related to that theme using Ollama AI, creates images associated with each word, and saves the vocabulary words, their translations, and associated images to a database. The primary goal is to create personalized flashcards for vocabulary learning.

## Features

-	Generate Vocabulary Words: The app generates 10 vocabulary words based on a given theme using Ollama AI.
-	Create Images: For each vocabulary word, the app generates an associated image, using limewire AI.
-	Database Storage: The app saves the vocabulary words, their translations, image paths, and theme into a database for future reference.

## Requirements

- Python 3.6 or higher (https://www.python.org/)
- LimeWire API key  (https://limewire.com/) + add to `src/config.py`

```python
API_KEY = 'YOUR API KEY'
```

- Ollama run model (https://ollama.com/) 

```bash
ollama pull mistral
```

- SQLite3 

(Mac) 
```bash
brew install sqlite3
```

or 

(Linux)
```bash
sudo apt-get install sqlite3
```



## Installation

Follow these steps to set up and run the Vocabulary Flash Card Generator:

```bash
git clone 'https://github.com/raphael-pietrzak/vocabulary-flashcards.git'
cd vocabulary-flashcards
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python main.py
```

## Usage

1.	Provide a Theme:
When you run the application, it will prompt you to enter a theme. This theme is used to generate a list of vocabulary words.
2.	Vocabulary Generation:
The application uses Ollama AI to generate a list of 10 vocabulary words related to the provided theme.
3.	Image Generation:
For each vocabulary word, an image is generated and saved.
4.	Database Storage:
The application saves the following details into a database:
- Vocabulary word
- Translation of the word
- Path to the associated image
- Theme used for generation



## Example

1.	Start the application:
```bash
python main.py
```
2.	Enter a theme when prompted, e.g., “Travel”.
3.	The application will generate 10 vocabulary words related to “Travel”, create images for each word, and save all relevant information to the database.


## Troubleshooting

If you encounter this error: `AttributeError: module 'httpcore' has no attribute 'SyncHTTPTransport`

In the file client.py, fix 'httpcore.SyncHTTPTransport' to 'httpcore.AsyncHTTPProxy'