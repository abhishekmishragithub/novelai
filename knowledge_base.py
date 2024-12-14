from langchain_community.document_loaders import DirectoryLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.docstore.document import Document

def create_embeddings(directory: str, glob: str = "**/*.txt") -> FAISS:
    """
    Creates embeddings from text files in a directory using Sentence Transformers and FAISS.

    Args:
        directory (str): The path to the directory containing the text files.
        glob (str): Pattern used to find files

    Returns:
        FAISS: A FAISS index containing the embeddings.
    """

    # Load documents from the directory
    loader = DirectoryLoader(directory, glob=glob)
    documents = loader.load()

    # Split documents into chunks
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    texts = text_splitter.split_documents(documents)

    # Create embeddings using Sentence Transformers
    embeddings = HuggingFaceEmbeddings(model_name="all-mpnet-base-v2")
    db = FAISS.from_documents(texts, embeddings)

    return db
