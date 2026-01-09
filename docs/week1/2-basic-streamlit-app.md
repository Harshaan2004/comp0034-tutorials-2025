# Basic Streamlit app using the paralympics data

[Streamlit reference](https://docs.streamlit.io/get-started/fundamentals/main-concepts)

[Streamlit create your first app tutorial](https://docs.streamlit.io/get-started/tutorials/create-an-app)

## Run a streamlit app

[src/streamlit_app/streamlit_demo_app.py](../../src/streamlit_app/streamlit_demo_app.py) contains a
completed example of the above tutorial.

Have a look at the code and then run the app by entering
`streamlit run src/streamlit_app/streamlit_demo_app.py` in the terminal.

The app runs by default on http://localhost:8501

Use Ctrl + C to stop the running app.

## Create a basic streamlit app

Create a new streamlit_app.py file in the streamlit_app directory.

Add imports:

```python
import streamlit as st
from src.data.mock_api import get_event_data
```

Load the data into a pandas DataFrame. The data will be in JSON format.

```python
df = 
```

Streamlit changes can be dynamically seen in the browser. Run the app. 

Every time you want to update your app, save the source file. When you do
that, Streamlit detects if there is a change and asks you whether you want to rerun your app.
Choose "Always rerun" at the top-right of your screen to automatically update your app every time
you change its source code.

You can then quickly see changes in your app as you make them.





Spare
Unlike the other web frameworks that typically expect a modular type structure that you have been
working with, Streamlit will work with a plain Python script. You should still consider the
principles of design and structure the code where possible.