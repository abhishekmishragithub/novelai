import os

from agents import (
    ChapterWriterAgent,
    CharacterAgent,
    PlotterAgent,
    WorldbuilderAgent,
)

os.environ["TUNE_API_KEY"] = "YOUR_TUNE_KEY"

def main():
    worldbuilder = WorldbuilderAgent()
    plotter = PlotterAgent()
    character_agent = CharacterAgent()
    chapter_writer = ChapterWriterAgent()

    user_input = input("Enter a prompt to start the novel creation: ")


    # worldbuilding
    world_context = worldbuilder.generate_response(user_input, "")
    print(f"\n{worldbuilder.name}:\n{world_context}")

    # write plot
    plot_context = plotter.generate_response(user_input, world_context)
    print(f"\n{plotter.name}:\n{plot_context}")

    # make character
    character_context = character_agent.generate_response(user_input, world_context + plot_context)
    print(f"\n{character_agent.name}:\n{character_context}")

    # write chapter
    chapter_text = chapter_writer.generate_response(
        user_input, world_context + plot_context + character_context
    )
    print(f"\n{chapter_writer.name}:\n{chapter_text}")


if __name__ == "__main__":
    main()
