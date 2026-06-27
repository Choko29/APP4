# teacher_quiz.py
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from config import DB_PATH, EMBEDDING_MODEL, LLM_MODEL, SEARCH_RESULTS_COUNT

def generate_questions():
    embeddings = OllamaEmbeddings(model=EMBEDDING_MODEL)
    vectorstore = Chroma(persist_directory=DB_PATH, embedding_function=embeddings)
    docs = vectorstore.similarity_search("ძირითადი ცნებები, განმარტებები, მნიშვნელოვანი საკითხები და სასწავლო თემები", k=SEARCH_RESULTS_COUNT)
    context = "\n\n".join([doc.page_content for doc in docs])
    
    template = """შენ ხარ Teacher Assistant სისტემა. მოცემული ტექსტის მიხედვით დააგენერირე 5 სასწავლო კითხვა.
    წესები:
      - კითხვები უნდა შეიქმნას მხოლოდ მოცემული კონტექსტიდან.
      - კითხვები უნდა იყოს ქართულად.
      - კითხვები უნდა იყოს გასაგები სტუდენტებისთვის.
      - არ დაწერო პასუხები, დაწერე მხოლოდ კითხვები.
      - კითხვები დანომრე 1-დან 5-მდე.

    კონტექსტი: {context}
    5 კითხვა: """
    
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | ChatOllama(model=LLM_MODEL, temperature=0.2) | StrOutputParser()
    return chain.invoke({"context": context})
