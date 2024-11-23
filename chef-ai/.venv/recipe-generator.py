from transformers import pipeline

pipe = pipeline("text-generation", model="pratultandon/recipe-nlg-gpt2-train11_15")

#Input ingredients
ingredients = "chicken, rice, broccoli"
prompt = ingredients

#Generate the recipe
result = pipe(prompt, max_length=200, num_return_sequences=1)

#Print the generated recipe
print("Generated Recipe:")
print(result[0]["generated_text"])