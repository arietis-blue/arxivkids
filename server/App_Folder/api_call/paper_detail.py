from .gpt_api.gpt_getkeywords import keywords
from .gpt_api.gpt_paraphrase import paraphrase
from .deepl_api.deepl import translate_ja_list
from .deepl_api.deepl import translate_ja

# 論文のjsonを受け取り、Content_Ja, (Keywords)を追加
def main(paper_json):
    # 要約の日本語訳
    content_ja = translate_ja(paper_json["Content_En"])
    paper_json["Content_Ja"] = content_ja
    # 平易な言葉に言い換え
    plain_content = paraphrase(content_ja)
    paper_json["Content_plain"] = plain_content
    # # キーワードの取得
    keywords_json = keywords(plain_content)
    keyword_list = keywords_json["list"]
    paper_json["Keywords"] = keyword_list
    return paper_json

# papers = search_paper.main('LLM cat:cs.CL')
# print(papers[0])
# added_papers = main(papers[0])
# print(added_papers)