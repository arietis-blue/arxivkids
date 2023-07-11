import arxiv
import json
from pathlib import Path

# カテゴリーの対応表のjsonファイルの読み取り
parent = Path(__file__).resolve().parent
with open(parent.joinpath("cat_dic.json")) as f:
    cat_dic = json.load(f)


# 検索文を受け取りjsonのリストを返す
def get_arxiv_data(query):
    max_results = 5
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate,
        sort_order=arxiv.SortOrder.Descending    
        )

    data_list = []
    for result in search.results():
        # Arxivで定義されたAuthor型から名前を取り出しリストにする 
        author_list =[]
        for author in result.authors:
            author_list.append(author.name)
        # Categoryをわかりやすい名前に変えてリスト化 
        category_list = []
        for category in result.categories:
            category_list.append(cat_dic[category])
        # 改行の削除
        title = (result.title).replace('\n','')
        summary = (result.summary).replace('\n','')
        data = {
            'ID': result.entry_id,
            'Title_En': title,
            'Content_En': summary,  #abstract
            'Categories': category_list, # 論文のカテゴリ  
            'authors': author_list, # 著者のリスト
            'Pdf_url': result.pdf_url, # PDFのURL
            'published': result.published #出版された日時の追加(datetime.datetime型で返す)
            }
        data_list.append(data)
    
    return data_list

# # Example usage
# query = 'LLM cat:cs.CL'
# json_list = get_arxiv_data(query)
# print(type(json_list))
# print(json_list)
