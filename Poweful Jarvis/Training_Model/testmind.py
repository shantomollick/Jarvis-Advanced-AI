# from transformers import GPT2LMHeadModel, GPT2Tokenizer
# from FRIDAY.FSpeak import fspeak
#
# # Load the GPT-2 model and tokenizer for text generation
# tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
# model = GPT2LMHeadModel.from_pretrained("gpt2")
#
# def generate_fallback_answer(prompt):
#     inputs = tokenizer.encode(prompt, return_tensors="pt")
#     outputs = model.generate(inputs, max_length=50, num_return_sequences=1, no_repeat_ngram_size=2, top_p=0.95, temperature=0.7)
#     generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
#     return generated_text.strip()
#
#
# prompt = input("enter: ")
# generated_answer = generate_fallback_answer(prompt)
# fspeak(generated_answer)
# print(generated_answer)
