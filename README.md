# Personality chatbot with Langchain + LangSmith.

## Requirement

- Python version >= 3.9. Because langchainhub package require it

## Description

- This is a chatbot implementation with Langchain framework.
  - Base LLM: Vertex AI
  - Memory: MongoDB
  - UI:
    - Gradio
    - Langchain UI: [Chat Langchain](https://github.com/langchain-ai/chat-langchain)
      - Use it to leverages LangChain's streaming support.
  - Prompt versioning and LLM tracing: LangSmith
- User can custom bot's personality by setting bot information like gender, age, ...
- Demo UI:
  ![Demo UI](/assets/demo_ui.png)

## How to use

- You need Google Cloud credentials to call Vertex API
- You need create mongoDB database and collection to use as Langchain memory

### Setup tracing with Langsmith

- Langsmith docs: [LangSmith](https://docs.smith.langchain.com/)
- Configure environment to connect to LangSmith.
  ```commandline
  export LANGCHAIN_TRACING_V2=true
  export LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
  export LANGCHAIN_API_KEY="<your-api-key>"
  export LANGCHAIN_PROJECT="chatbot-with-langchain"
  ```

### Development

0.  Download the models for the languages to use in anonymizer. PII support.
    1. `python -m spacy download en_core_web_md`
    2. `python -m spacy download vi_core_web_md`
1.  RUN backend
    1. Clone repo: `git clone https://github.com/btrcm00/chatbot-with-langchain.git`
    2. Add google-cloud-platform credential file to `secure/vertexai.json`
    3. `cd chatbot`
    4. Install required packages: `pip install -r requirements.txt`
    5. Create MongoDB database and config environment variables to connect Mongo.
    6. Run: `python app.py`
2.  RUN frontend
    1. `cd chatbot_frontend`
    2. Install packages: `npm i`
    3. Start frontend: `npm start dev`
