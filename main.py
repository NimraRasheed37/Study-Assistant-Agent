import os
from dotenv import load_dotenv
from openai import OpenAI 

load_dotenv()

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=os.getenv("OPENROUTER_API_KEY"),
)

# function to ask OpenAI a question
def ask_openai(prompt):
    response = client.chat.completions.create(
    model="openai/gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful study assistant."},
        {"role": "user", "content": prompt}
    ],
    max_tokens=300 
)
    return response.choices[0].message.content

def main():
    print("\n-----------Welcome! I am your Study Helper--------")
    print("\nI can help you with study tips, summarizing text, answering academic questions, and providing motivation.\n")
    print("Commands to enter: \n1.tips \n2.summarize \n3.question \n4.motivate \n5.exit\n")

    while True:
        command = input("\nEnter command: ").strip().lower()

        if command == "tips":
            print(ask_openai("Give me 5 short study tips."))
        elif command == "summarize":
            text = input("\nEnter text to summarize:\n")
            print(ask_openai(f"Summarize this: {text}"))
        elif command == "question":
            q = input("\nAsk your academic question:\n")
            print(ask_openai(f"Answer this academic question briefly: {q}"))
        elif command == "motivate":
            print(ask_openai("\nGive me a short motivational quote for students."))
        elif command == "exit":
            print("Goodbye! keep studying keep growing!")
            break
        else:
            print("Unknown command. Try again.")

if __name__ == "__main__":
    main()