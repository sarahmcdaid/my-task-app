import streamlit as st
import functions

tasks = functions.get_tasks()

st.set_page_config(layout="wide")

def add_task():
    task = st.session_state["new_task"] + "\n"
    tasks.append(task)
    functions.write_tasks(tasks)


st.title("My To-Do List App")
st.write("This app is to increase <b>productivity</b>",
         unsafe_allow_html=True)
st.subheader("Tasks: ")

for index, task in enumerate(tasks):
    checkbox = st.checkbox(task, key=task)
    if checkbox:
        tasks.pop(index)
        functions.write_tasks(tasks)
        del st.session_state[task]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add a new task...",
              on_change=add_task, key='new_task')
