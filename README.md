# AI in Healthcare Homework 4 dependencies, for Mac ARM computers
I had a difficult time trying to install [SciSpacy](https://allenai.github.io/scispacy/) 
on my Mac M1 ARM computer. I finally got it working by building [NMSlib](https://github.com/nmslib/nmslib) from source first. Then I fought for a while to install SciSpacy 
and compatible models. I don't think anyone else should have to do that again. So... here's what I did, with instructions so that things should go more smoothly for you.
Let me know if you run into problems. 

Note that this **WILL NOT** work on anything besides an Arm Mac running MacOS and Python 3.12. For that... good luck. 
Write to me at jonese@utexas.edu if you have questions.

Cheers,
Evan


## Installation
1. Install [`uv`](https://astral.sh/uv/), which is a Python package manager. 
   Really you should [read about](https://docs.astral.sh/uv/getting-started/) it first, but you'll end up doing this:

   `curl -LsSf https://astral.sh/uv/install.sh | sh`
2. Clone this project: 
   
   `git clone https://github.com/etjones/aihc_hw4_mac_arm.git`
3. Create a Python 3.12 virtual environment.
   
   `uv venv --python 3.12`
4. Activate the virtual environment.
   
   `source ./.venv/bin/activate`
5. Install all dependencies
   
   `uv sync`
6. ???
7. Profit

### All steps together
```
git clone https://github.com/etjones/aihc_hw4_mac_arm_deps.git
cd aihc_hw4_mac_arm_deps
uv venv --python 3.12
source ./.venv/bin/activate
uv sync
# Verify it's working
python -c "import spacy; nlp = spacy.load('en_core_web_sm'); print(nlp)"
```

