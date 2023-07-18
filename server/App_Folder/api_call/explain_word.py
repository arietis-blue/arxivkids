from .gpt_api.gpt_getkeywords import keywords
from .gpt_api.gpt_word_explain import explain_by_ja
from .deepl_api.deepl import translate_ja

# ユーザから指定された用語を解説
def explain_ja(paper_json,query_word_ja):
    # カテゴリを考慮して
    explanation = explain_by_ja(query_word_ja,paper_json["Categories"],paper_json["Content_Ja"])
    return explanation
    
import search_paper, paper_detail
papers = search_paper.main('LLM cat:cs.CL')
print(papers[0])
paper = paper_detail(papers[0])
new_paper = explain_ja(paper,"大規模言語モデル")
print(new_paper)
