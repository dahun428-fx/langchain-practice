import json
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_KEY"),
)

chat_completion = client.chat.completions.create(
    #
    # Required parameters
    #
    messages=[
        # # Set an optional system message. This sets the behavior of the
        # # assistant and can be used to provide specific instructions for
        # # how it should behave throughout the conversation.
        # {
        #     "role": "system",
        #     "content": "you are a helpful assistant."
        # },
        # Set a user message for the assistant to respond to.
        {
            "role": "user",
            "content": "아이폰 13 출시일이 언제야?",
        }
    ],

    # The language model which will generate the completion.
    # model="llama3-8b-8192",
    model="llama-3.2-90b-text-preview",
    #
    # Optional parameters
    #

    # Controls randomness: lowering results in less random completions.
    # As the temperature approaches zero, the model will become deterministic
    # and repetitive.
    temperature=0.5,

    # The maximum number of tokens to generate. Requests can use up to
    # 2048 tokens shared between prompt and completion.
    max_tokens=1024,

    # Controls diversity via nucleus sampling: 0.5 means half of all
    # likelihood-weighted options are considered.
    top_p=1,

    # A stop sequence is a predefined or user-specified text string that
    # signals an AI to stop generating content, ensuring its responses
    # remain focused and concise. Examples include punctuation marks and
    # markers like "[end]".
    # For this example, we will use ", 6" so that the llm stops counting at 5.
    # If multiple stop values are needed, an array of string may be passed,
    # stop=[", 6", ", six", ", Six"]
    stop=", 6",

    # If set, partial message deltas will be sent.
    stream=False,
)

print(json.dumps(chat_completion.choices[0].message.content, indent=2, ensure_ascii=False))