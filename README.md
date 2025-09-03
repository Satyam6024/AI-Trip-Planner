# AI-TRIP-PLANNER USING LANGCHAIN-AGENTIC-AI

## Features:
1. Realtime weather info
2. Tourist places- attraction and activities
3. Hotel cost
4. Currency conversion
5. Itineary Planning
6. Total Expense
7. Generate Summary


# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/Satyam6024/AI-Trip-Planner.git
```
### STEP 01- Install UV

```bash
pip install uv
```
### STEP 02- Check Available Environments

```bash
uv python list
```

### STEP 03- *Install Python for Virtual Environment 
#### Note: This step is only required when no python is available in your local machine

```bash
uv python install <name_and_version>
```
eg. uv python install cpython-3.12.7-windows-x86_64-none

### STEP 04- Create Virtual Environment

```bash
uv venv <virtual_env_name> --python cpython-3.12.7-windows-x86_64-none
```

### STEP 05- Activate the Environment

```bash
source <virtual_env_name>/Scripts/activate
```


### STEP 06- install the requirements
```bash
uv pip sync requirements.txt   
```

```bash
# Finally run the following command
streamlit run streamlit_app.py
```

#### Open a new terminal and activate the same environment and run:
```bash
uvicorn main:app --reload --port 8000

Now,
```bash
open up you local host and port
```


