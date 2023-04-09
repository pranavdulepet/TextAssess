# What is our project?
This NLP architecture takes in user input of a prompt and a response. Then, using common Language models, the user's response to their prompt is rated on similarity to the context of the question (judging how 'well' the user answers the question). Then, using an alternative (generative) model, a ML-generated response is concocted. At this point, we have two possible outputs to the same prompt. Therefore, using language models, responses can be compared, and better sentences can be chosen at each stage (between the user's sentences and the computer generated sentence).

Models used are Google's BERT model and OpenAI's GPT-2, hosted on HuggingFace and fine-tuned with AWS SageMaker.


# How Does it Work?
<!-- Architectural diagram -->
To demonstrate how this model works, refer to the following architectural diagram. It incorporates our future plans in addition to what is currently implemented. At the moment, our output represents how well a user answered a prompt with the metric being a similarity score between their response and a generated response. We are using cosine similarity to accomplish this by passing embeddings of the responses into the scikit-learn cosine similarity function. Then, we are identifying which parts of the user's response are not good enough. 
<br></br>
<img src="https://github.com/pranavdulepet/bitcamp-23/blob/main/flowchart.jpeg">

# Examples
<!-- Input-output examples -->
```python
# Given prompt/response pair and generated outputs
prompt = 'How are clouds formed?'

user_response = 'Clouds form when the invisible water vapor in the air condenses into visible water droplets or ice crystals. For this to happen, the parcel of air must be saturated, i.e. unable to hold all the water it contains in vapor form, so it starts to condense into a liquid or solid form.'

generated_response = 'How are clouds formed? We’ve all heard about them before (or maybe not, as we tend to get confused about whether or not the Earth is flat and whether or not we have a moon), but what exactly are clouds and how do they form? First, some words about atmospheric gases:
So here’s a quick overview of the atmospheric elements that make up a cloud. Clouds form when solid particles (typically, rocks and ice) collide with each other. They grow by deposition of water, ice and dust. They grow by condensation, where the water/ice/dust particles are released and collected.'

similarity_score = '0.9271547'
```

# 
