class AIModel :
    def __init__(self,model_name:str,input_token_cost_per_1k:float,output_token_cost_per_1k:float) -> None:
        if not model_name and self.model_name.strip():
            raise ValueError(" Model Name cannot be empty!")
        if input_token_cost_per_1k < 0 or output_token_cost_per_1k < 0 :
            raise ValueError("Token cost cannot be negative!")

        self.model_name = model_name.strip()
        self.input_token_cost_per_1k = input_token_cost_per_1k
        self.output_token_cost_per_1k = output_token_cost_per_1k
    def estimate_tokens(self,message: str) -> int:
        """ Estimate token count from a message by using word coint * 1.3 ."""
        if not isinstance(message, str):
            raise TypeError(" Message must be an string. ")
        if not message.strip():
            return 0
        word_count = len(message.split())
        return int(round( word_count) * 1.3 )
    def calculate_cost(self, input_tokens:int, output_tokens:int = 0) -> float:
        if input_tokens < 0 or output_tokens < 0 :
            raise ValueError ("Tokens can not be negative!")
        input_token_cost = (input_tokens / 1000) * self.input_token_cost_per_1k
        output_token_cost = (output_tokens / 1000) * self.output_token_cost_per_1k
        total_token_cost = input_token_cost + output_token_cost
        return round (total_token_cost, 6)
    def __str__(self):
        return (f" Model : {self.model_name} | "
                f"Input Tokens/1k : {self.input_token_cost_per_1k} |"
                f"Out Tokens/1k : {self.output_token_cost_per_1k} ")

if __name__ == "__main__":
    ai = AIModel("gemini-flash" , .00002,.00010)
    tokens = ai.estimate_tokens("Learning python Object oriented programming.")
    cost = ai.calculate_cost(tokens)

    print(f" Model : {ai.model_name} | Tokens : {tokens} | Cost : {cost:.6f}")
