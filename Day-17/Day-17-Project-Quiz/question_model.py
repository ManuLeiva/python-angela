class Question:
    def __init__(self, q_text, q_answer):
        ### to create the attibute we need to use the
        ### following sintax self. When we will create
        ### a new object we will pass the 2 items, text 
        ### and answer. 
        self.text = q_text
        self.answer = q_answer

### Example:
# new_q = Question("question text", "True")
# print(new_q.text)