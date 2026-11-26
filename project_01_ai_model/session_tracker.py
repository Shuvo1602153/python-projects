class SessionTracker:
    def __init__(self,session_id: str = "default session", model_name: str = "Unknown")-> None:
        if not session_id or not session_id.strip():
            raise ValueError("Session id can not be empty.")
        self.session_id = session_id.strip()
        self.model_name = model_name if model_name and model_name.strip() else "Unknown"

        self.records:list[dict] = []
        self.total_input_tokens: int = 0
        self.total_output_tokens: int = 0
        self.total_cost: float = 0.0

    def add_turns(self,inpur_tokens: int, output_tokens: int, cost: float, prompt: str)->None:
        if inpur_tokens < 0 or output_tokens < 0 :
            raise ValueError("Tokens cannot be negative.")
        if cost < 0 :
            raise ValueError("Cost cannot be negative.")
        self.total_input_tokens += inpur_tokens
        self.total_output_tokens += output_tokens
        turn_cost = round(cost,6)
        self.total_cost = round(self.total_cost + turn_cost,6)
        self.records.append({
            "turn" : len(self.records) +1,
            "prompt" : prompt.strip(),
            "inpur_tokens" : inpur_tokens,
            "output_tokens" : output_tokens,
            "cost" : turn_cost,
        })

    def get_summary(self)-> dict:
        return({
            "session_id" : self.session_id,
            "model_name" : self.model_name,
            "total_turns" : len(self.records),
            "total_input_tokens" : self.total_input_tokens,
            "total_outpuT tokens" : self.total_output_tokens,
            "total_tokens" : self.total_input_tokens + self.total_output_tokens,
            "total_cost" : self.total_cost,
        })

if __name__ == "__main__":
    tracker = SessionTracker("session-01", "gemini-flash" )
    tracker.add_turns(1000,2000,0.0005,"I am learning object oriented programming from zero. Will you please help me?")

    print(f"Session Summary: {tracker.get_summary()}") 
    print(f"Your turn record: {tracker.records[0]}")     