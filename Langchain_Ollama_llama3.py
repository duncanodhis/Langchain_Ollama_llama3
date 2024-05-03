from langchain.llms import Ollama
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate

# Initialize the Ollama LLM pointing to the correct endpoint and model
ollama = Ollama(
    endpoint="http://localhost:11434",  # Ollama server endpoint
    model_name="llama3",  #model name
)

# Create a memory object to retain conversational context
memory = ConversationBufferMemory()

# Define a simple conversational chain with the Ollama model and memory
conversation_chain = ConversationChain(
    llm=ollama,
    memory=memory,
    input_key="input",  # The input key for user input
    output_key="response",  # The key for the model's response
    verbose=True,  # Optional: outputs intermediate steps for debugging
)

# Interact with the chatbot
print("Starting chatbot. Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    response = conversation_chain.predict(input=user_input)
    print(f"Chatbot: {response['response']}")
