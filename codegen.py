from transformers import AutoModelForCausalLM, AutoTokenizer

checkpoint = "model/"

model = AutoModelForCausalLM.from_pretrained(checkpoint, local_files_only=True)

tokenizer = AutoTokenizer.from_pretrained(checkpoint)

def generate_code(text, max_tokens, temperature):
    completion = model.generate(**tokenizer(text, return_tensors="pt"),
                                max_new_tokens=max_tokens,
                                do_sample=True,
                                top_k=0,
                                temperature=temperature)              
    return tokenizer.decode(completion[0])