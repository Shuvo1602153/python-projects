class SessionTracker:
    def __init__(self,session= "default session"):
        self.session = session
        self.total_message = 0
        self.total_tokens = 0
        self.total_cost = 0.0
        self.records = []
    def record_usage (self,model,prompt,tokens,cost,):
        self.total_message +=1
        self.total_tokens += tokens
        self.total_cost += cost
        entry = {
            "model" : model, 
            "prompt" : prompt,
            "tokens":tokens,
            "cost": cost
        } 
        self.records.append(entry)
    def get_summary(self):
        return {
            "session_name" : self.session,
            "Total_message" : self.total_message,
            "Total_tokens" : self.total_tokens,
            "Total_cost" : round(self.total_cost, 6)
        }
    def __str__(self):
        summary  = self.get_summary()
        return (f"Session: {summary['session_name']} | "
            f"Messages: {summary['total_messages']} | "
            f"Tokens: {summary['total_tokens']} | "
            f"Total Cost: ${summary['total_cost']:.6f}"
            )
if __name__ == "__main__":
    tracker = SessionTracker("Study Session")

    # উদাহরণ হিসেবে দুটি প্রম্পটের হিসাব রেকর্ড করা হলো
    tracker.record_usage("gemini-flash", "Explain OOP", 10, 0.00002)
    tracker.record_usage("claude-sonnet", "Give a Python example", 25, 0.000125)

    print(tracker)
    print("Total stored records:", len(tracker.records))