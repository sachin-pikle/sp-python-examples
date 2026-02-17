## Source: https://github.com/huggingface/transformers?tab=readme-ov-file
## pip install "transformers[torch]"

from transformers import pipeline

classifier = pipeline("sentiment-analysis")
result = classifier("I love using Hugging Face Transformers!")
print(result)