from langchain.agents import create_agent
from langchain_core.messages import SystemMessage, HumanMessage
from dotenv import load_dotenv
from flask import Flask, render_template
from vectorstore_search import vector_search
import json

load_dotenv()
agent = create_agent(model="gpt-5.5")


def rag_search(query):
    try:
        vectors = vector_search(query)
        documents = vectors["documents"]
        context = "\n\n".join(documents[0])

        system_message = SystemMessage(
            content="""
        You are a helpful AI assistant.

         Your task is to answer questions using ONLY the
    information provided in the retrieved context.

    Rules:
    1. Do not use external knowledge or assumptions.
    2. Do not invent facts, technologies, features, or numbers.
    3. Every factual claim must be supported by the context.
    4. If the answer is partially available, provide only
       the supported information.
    5. If the answer is not available in the context,
       explicitly say:
       "The provided document does not contain this information."
    6. Preserve the original meaning of the document.
    7. Do not expand answers with general knowledge.


        Context:
        {context}
        """,
        )

        human_message = HumanMessage(content=query)
        result = agent.invoke({"messages": [system_message, human_message]})
        return result["messages"][-1].content
    except Exception as e:
        print(e)


questions = [
    "What are the primary objectives of the E-Medicine Delivery System?",
    "What are the three major research areas discussed in the literature review?",
    "What problems do patients face with traditional methods of obtaining medical consultations and medicines?",
    "How does the Prescription Analysis module improve patient safety?",
    "What technologies are proposed for extracting and validating prescription information?",
    "What is the role of OCR in the Prescription Analysis module, and how does it work with rule-based validation?",
    "How does the proposed system benefit patients in remote or underserved areas?",
    "Explain how live consultation, prescription verification, and medicine delivery are integrated into a single platform.",
    "What security technologies and standards are proposed to protect patient information?",
    "According to the project estimation, how many days are allocated to prescription analysis, video consultation integration, and testing and debugging?",
]


result = []
for question in questions:
    result.append({"question": question, "answer": rag_search(question)})


with open("./day_6/app/output/result2.json", "w", encoding="utf-8") as f:
    json.dump(result, f, indent=3, ensure_ascii=False)
