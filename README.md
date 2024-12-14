# NovelAI: Multi-agent Collaborative Novel Writing

## Overview

NovelCraft is a multi-agent system that leverages the power of Agentic Retrieval-Augmented Generation (RAG) to collaboratively write a fantasy novel. It consists of four specialized agents:

*   **Worldbuilder:** Creates and maintains the fantasy world, including its history, geography, cultures, and magic systems.
*   **Plotter:** Develops the overall plot of the novel, including the main conflict, key events, and character arcs.
*   **Character Agent:** Creates and develops detailed characters with unique personalities, motivations, and backstories.
*   **Chapter Writer:** Writes individual chapters of the novel, taking into account the world, plot, and characters created by the other agents.

Each agent is equipped with RAG capabilities, allowing it to access and utilize information from a specialized knowledge base to enhance its creative output.

## Workflow

The system follows a sequential collaborative architecture:

1. The user provides an initial prompt to start the novel creation.
2. The **Worldbuilder** generates the initial world context based on the prompt and its knowledge base.
3. The **Plotter** takes the prompt and world context to develop the plot outline.
4. The **Character Agent** uses the prompt, world context, and plot outline to create characters.
5. The **Chapter Writer** combines all the information (prompt, world, plot, characters) to write a chapter.

Agents also have a basic form of short-term memory by passing their output as context to the next agent in the sequence.

## Technology Stack

*   **LangChain:** Framework for building applications with large language models.
*   **Hugging Face Sentence Transformers:** For creating text embeddings (using the `all-mpnet-base-v2` model).
*   **FAISS (Facebook AI Similarity Search):** For efficient similarity search in vector databases.
*   **OpenAI API (GPT-3.5 Turbo):** Large Language Model for text generation.
*   **Streamlit:** Framework for building the user interface.

## Getting Started

### Prerequisites

*   Python 3.11+
*   pip
*   A virtual environment (recommended, e.g., using `venv` or `conda`)
*   Tune AI API key

### Installation

1. **Clone the repository:**

    ```bash
    git clone <your_repository_url>
    cd novelai
    ```

2. **Create and activate a virtual environment (optional but recommended):**

    *   **Using `venv`:**

        ```bash
        python3 -m venv .venv
        source .venv/bin/activate  # On Linux/macOS
        .venv\Scripts\activate  # On Windows
        ```

    *   **Using `conda`:**

        ```bash
        conda create -n novelai python=3.11
        conda activate novelai_env
        ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```
    Install `libmagic`

    *   **macOS (using Homebrew):**

      ```bash
        brew install libmagic
      ```

   *   **Debian/Ubuntu (using apt):**

       ```bash
       sudo apt-get install libmagic-dev
       ```

   *   **Fedora/CentOS/RHEL (using dnf/yum):**

       ```bash
       sudo dnf install file-devel  # Or yum install file-devel
       ```

4. **Set your TUNE AI API key:**
    *   **EITHER:** Set it as an environment variable:

        ```bash
        export TUNE_API_KEY="your_api_key"
        ```

    *   **OR:** Replace `"YOUR_API_KEY"`  in  `novelcraft_streamlit.py`  with your actual key (less secure).

### Usage

1. **Run the Streamlit app:**

    ```bash
    streamlit run novelcraft_streamlit.py
    ```

2. **Open your web browser and go to the URL provided by Streamlit (usually `http://localhost:8501`).**

3. **Enter an initial prompt to start the novel creation process.**

4. **Interact with individual agents using the dropdown menu and text input fields.**
