## Source: https://github.com/huggingface/transformers?tab=readme-ov-file
## pip install "transformers[torch]"
## BlipImageProcessor requires the PIL library but it was not found in your environment. You can install it with pip:
## pip install pillow
## Please note that you may need to restart your runtime after installation.

from transformers import pipeline

pipeline = pipeline(task="visual-question-answering", model="Salesforce/blip-vqa-base")
result = pipeline(
    # image="https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/idefics-few-shot.jpg",
    image = "https://media.architecturaldigest.com/photos/66a951edce728792a48166e6/16:9/w_2240,c_limit/GettyImages-955441104.jpg",
    question="What is in the image?",
)
print(result)
#[{'answer': 'statue of liberty'}]