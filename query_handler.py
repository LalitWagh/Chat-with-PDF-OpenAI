from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

def handle_query(text, query):
    llm = OpenAI(api_key="your-api-key")
    prompt = PromptTemplate(
        input_variables=["document", "question"],
        template="""
        You are a helpful assistant. Given the document content below, answer the question accurately and concisely.
        Document: {document}
        Question: {question}
        Answer:
        """
    )
    formatted_prompt = prompt.format(document=text, question=query)
    response = llm.predict(formatted_prompt)
    return response
