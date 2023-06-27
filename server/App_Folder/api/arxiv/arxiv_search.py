import arxiv
import pandas as pd
from pathlib import Path

# 検索文を受け取りjsonのリストを返す
def get_arxiv_data(query):
    max_results = 3
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate,
        sort_order=arxiv.SortOrder.Descending    
        )

    data_list = []
    for result in search.results():
        data = {
            'ID': result.entry_id,
            'Title_En': result.title,
            'Content_En': result.summary,  
            # 'Categories': result.categories, # 論文のカテゴリ     
            # 'Pdf_url': result.pdf_url # PDFのURL 
            }
        data_list.append(data)
    
    return data_list

# Example usage
# query = 'cat:cs.CL'
# json_list = get_arxiv_data(query)
# print(type(json_list))
# print(json_list)
