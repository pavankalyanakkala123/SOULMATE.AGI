from core.chatbot import chat_with_soulmate
from core.journal import journal_entry
from core.memory import recall_memory
from core.summary import generate_daily_summary
from models.trainer import simulate_lora_training

def main():
    print("🌟 Welcome to SoulMate.AGI (CLI Mode)")
    print("1. Chat with SoulMate")
    print("2. Journal Entry")
    print("3. Recall Memory")
    print("4. Generate Summary")
    print("5. Run Nightly Training")
    print("0. Exit")

    while True:
        choice = input("\nChoose an option: ")

        if choice == "1":
            chat_with_soulmate()
        elif choice == "2":
            journal_entry()
        elif choice == "3":
            print(recall_memory())
        elif choice == "4":
            print(generate_daily_summary())
        elif choice == "5":
            simulate_lora_training()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
