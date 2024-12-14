import os
import streamlit as st
from agents import (
    ChapterWriterAgent,
    CharacterAgent,
    PlotterAgent,
    WorldbuilderAgent,
)


st.title("NovelAI: Novel Co-Creation Agent")

if "worldbuilder" not in st.session_state:
    st.session_state.worldbuilder = WorldbuilderAgent()
    st.session_state.plotter = PlotterAgent()
    st.session_state.character_agent = CharacterAgent()
    st.session_state.chapter_writer = ChapterWriterAgent()

initial_prompt = st.text_input("Enter a prompt to start the novel creation:")

if st.button("Create"):
    # worldbuilding
    st.session_state.world_context = st.session_state.worldbuilder.generate_response(
        initial_prompt, ""
    )
    st.markdown(f"**Worldbuilder:**\n\n{st.session_state.world_context}")

    # write plot
    st.session_state.plot_context = st.session_state.plotter.generate_response(
        initial_prompt, st.session_state.world_context
    )
    st.markdown(f"**Plotter:**\n\n{st.session_state.plot_context}")

    # make character
    st.session_state.character_context = st.session_state.character_agent.generate_response(
        initial_prompt, st.session_state.world_context + st.session_state.plot_context
    )
    st.markdown(f"**Character Agent:**\n\n{st.session_state.character_context}")

    # write chapter
    st.session_state.chapter_text = st.session_state.chapter_writer.generate_response(
        initial_prompt,
        st.session_state.world_context
        + st.session_state.plot_context
        + st.session_state.character_context,
    )
    st.markdown(f"**Chapter Writer:**\n\n{st.session_state.chapter_text}")


agent_options = ["Worldbuilder", "Plotter", "Character Agent", "Chapter Writer"]
selected_agent = st.selectbox("Select an agent to interact with:", agent_options)

prompt = st.text_input(f"Enter a prompt for the {selected_agent}:")

if st.button("Generate"):
    if selected_agent == "Worldbuilder":
        st.session_state.world_context = st.session_state.worldbuilder.generate_response(
            prompt, st.session_state.world_context
        )
        st.markdown(f"**Worldbuilder:**\n\n{st.session_state.world_context}")
    elif selected_agent == "Plotter":
        st.session_state.plot_context = st.session_state.plotter.generate_response(
            prompt, st.session_state.world_context + st.session_state.plot_context
        )
        st.markdown(f"**Plotter:**\n\n{st.session_state.plot_context}")
    elif selected_agent == "Character Agent":
        st.session_state.character_context = (
            st.session_state.character_agent.generate_response(
                prompt,
                st.session_state.world_context
                + st.session_state.plot_context
                + st.session_state.character_context,
            )
        )
        st.markdown(f"**Character Agent:**\n\n{st.session_state.character_context}")
    elif selected_agent == "Chapter Writer":
        st.session_state.chapter_text = (
            st.session_state.chapter_writer.generate_response(
                prompt,
                st.session_state.world_context
                + st.session_state.plot_context
                + st.session_state.character_context,
            )
        )
        st.markdown(f"**Chapter Writer:**\n\n{st.session_state.chapter_text}")
