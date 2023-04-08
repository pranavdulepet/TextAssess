# What is our project?
This NLP architecture takes in user input of a prompt and a response. Then, using common Language models, the user's response to their prompt is rated on similarity to the context of the question (judging how 'well' the user answers the question). Then, using an alternative (generative) model, a ML-generated response is concocted. At this point, we have two possible outputs to the same prompt. Therefore, using language models, responses can be compared, and better sentences can be chosen at each stage (between the user's sentences and the computer generated sentence).

Models used are Google's BERT model and OpenAI's GPT-2, hosted on HuggingFace and trained on AWS's SageMaker platform.
