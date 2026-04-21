from langchain.chains import RetrievalQA


def build_qa(chunks_list):
    vs = FAISS.from_documents(chunks_list, embeddings)
    return RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vs.as_retriever(search_kwargs={"k": 4}),
        return_source_documents=True,
    )


qa_by_strategy = {
    "1: CharacterTextSplitter, 1000/100": build_qa(chunks_1),
    "2: Recursive, 1000/100": build_qa(chunks_2),
    "3: Recursive, 500/50": build_qa(chunks_3),
}

test_questions = [
    "Опиши історію Чернівецького університету від заснування до сьогодні.",
    "Які твори написала Ольга Кобилянська та про що вони?",
    "Які історичні та природні райони входили до Буковини?",
]

for test_q in test_questions:
    print("\n" + "=" * 70)
    print(f"Q: {test_q}")
    print("=" * 70)
    for name, qa in qa_by_strategy.items():
        result = qa.invoke({"query": test_q})
        print(f"\n[{name}]")
        print(f"Довжина відповіді: {len(result['result'])} симв.")
        print(f"Retrieved chunks: {len(result['source_documents'])}")
        first_chunk = result["source_documents"][0].page_content[:120].replace("\n", " ")
        print(f"Перший chunk починається: «{first_chunk}...»")
        print(f"Відповідь:\n{result['result']}")
