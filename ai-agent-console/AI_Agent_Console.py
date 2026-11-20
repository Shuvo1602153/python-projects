def token_calculate(message):
    tokens =int(round(len(message.split())*1.3))
    return tokens
def token_cost_calculate(token,rate_per_1_k):
    return ((token / 1000) * rate_per_1_k )
def save_to_log_file(file_name,log_lines):
    with open(file_name, "a", encoding="utf-8") as file:
        file.write(log_lines)

def read_chat_history(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return "file is not found yet"
    
    
print("Hello! Here is our service of AI models and cost per 1000 Tokens:")
aiModels={
        "gemini-flash": 0.002, 
        "claude-sonnet": 0.005, 
        "llama-4": 0.003
    }
# Models and rate per 1000 Tokens    
print(f"\n")
for key,value in aiModels.items():
    print(f"{key:<15} : $ {value}")
print(f"\n")
# Model input 

is_model = True

while is_model:
    model =input("Please choose a model from the screen: ").strip().lower()
    try:
        if not model:
            print(f" Please select a available model {' , '.join(aiModels)} ")
        elif model in aiModels:
            token_cost_per_1k = aiModels[model]
            break
        else:
            print(f" Please select a available model {' , '.join(aiModels)}")
    except ValueError as e:
        print(f"Input error: {e}")
log_file = "chat_history.txt"
is_running = True
total_tokens = 0
total_cost = 0
session_status =["exit","quit"]

while is_running:
    user_message = input("Please type your prompt/message or type 'exit' or 'quit' to stop: ")
    if user_message.strip().lower() in session_status:
        is_running = False
        print("...Your session is closing... \n" 
        f"Your session token is : {total_tokens} | cost is : {total_cost:.5f} \n" 
        "----- Saving chat history ----- \n" 
        ".....Good Bye....."
        )
        print( read_chat_history(log_file))
    else:
        try:
            if not user_message.strip():
                print("Message cannot be empty!")
                continue
            current_tokens = token_calculate(user_message)
            if current_tokens < 0 :
                print("Tokens cannot be negative.")
            total_tokens += current_tokens
            current_cost = token_cost_calculate(current_tokens,token_cost_per_1k)
            total_cost += current_cost 

            log_entry = (
                f"Prompt: {user_message}\n"
                f"Current Tokens : {current_tokens} and Current Cost : {current_cost:.5f}\n"
                f"Total Tokens : {total_tokens} and Total Cost : {total_cost:.5f}\n"
                "----------------------------------------\n"
            )
            save_to_log_file(log_file,log_entry)
            print(log_entry)
        except ValueError as e:
            print(f"Invalid Input : {e}")
        



    



