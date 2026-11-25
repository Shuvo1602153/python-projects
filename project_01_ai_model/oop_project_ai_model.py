
ai_Models={
        "gemini-flash": 0.002, 
        "claude-sonnet": 0.005, 
        "llama-4": 0.003
    }


print("Available AI Models: ")
for key,value in ai_Models.items():
    print(f"{key:<15} : ${value}")
    

class AiModels:
    def __init__(self,name,rate_per_1k):
        self.name = name
        self.rate_per_1k = rate_per_1k
    def estimated_tokens(self, message):
        tokens = int(round(len(message.split()* 1.3))) 
        return tokens
    def calculated_cost(self, tokens):
        cost = (tokens/1000) * self.rate_per_1k
        return cost
    def __str__(self):
        return (f"Model: {self.name} | Cost per 1000 k tokens: {self.rate_per_1k}\n")

if __name__ == "__main__":
    ai_model_name = input("Please select a model from the list above : ")

    if ai_model_name in ai_Models:
        tokens_rate = ai_Models[ai_model_name]

    ai= AiModels(ai_model_name,tokens_rate)
    prompt = input("Enter your Prompt : ")
    tokens = ai.estimated_tokens(prompt)
    cost = ai.calculated_cost(tokens)

    print("\n ------------result------------")
    print(ai)



        