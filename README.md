# Discord Image Grabber 

Gets all attachments from a users discord profile 

## Getting started 

1. Install `uv` 

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Clone repo 

```sh
git clone https://github.com/Henry-Ash-Williams/discord-image 
cd discord-image
```

3. Install dependencies 

```sh
uv sync
```

4. Point script to extracted discord data 

```py
# In hello.py, Line 10
PATH = "/path/to/discord-data/messages"
```

5. Run script 

```sh 
source .venv/bin/activate 
python hello.py
```