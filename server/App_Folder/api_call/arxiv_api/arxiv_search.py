import arxiv
from pathlib import Path

# 検索文を受け取りjsonのリストを返す
def get_arxiv_data(query):
    max_results = 2
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
        data = {
            'ID': result.entry_id,
            'Title_En': result.title,
            'Content_En': result.summary,  #abstract
            'Categories': result.categories, # 論文のカテゴリ  
            'authors': author_list, # 著者のリスト
            'Pdf_url': result.pdf_url # PDFのURL
            }
        data_list.append(data)
    
    return data_list

# # Example usage
# query = 'LLM cat:cs.CL'
# json_list = get_arxiv_data(query)
# print(type(json_list))
# print(json_list)
