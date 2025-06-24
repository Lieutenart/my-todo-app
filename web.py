import streamlit as st
from modules import function


app_container = function.read_txt()


def add_input():
    new_todo = st.session_state["new_input"] + "\n"
    app_container.append(new_todo)
    function.write_txt(app_container_loc_arg=app_container)


st.title("My Todo App")
st.subheader("This is my first application")

for numerate, list_items in enumerate(app_container):
    check_box = st.checkbox(list_items, key=list_items)
    if check_box is True:
        app_container.pop(numerate)
        function.write_txt(app_container_loc_arg=app_container)
        del st.session_state[list_items]
        st.rerun()

st.text_input(label="", placeholder="Add new Task",
              on_change=add_input, key="new_input")

