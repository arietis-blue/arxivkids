from .models import Papers, Keywords, Reads, Profile
import json


# Search Translated Title
def search_titles(request_Paper_ID):
    if Papers.objects.filter(Paper_ID = request_Paper_ID).exists():
        content = Papers.objects.get(Paper_ID = request_Paper_ID)
        record = {
            "Paper_ID"   : content.Paper_ID,
            "Title_En"   : content.Title_En,
            "Title_Ja"   : content.Title_Ja,
            "Authors"    : content.Authors,
            "Categories" : content.Categories,
            "Published"  : content.Published,
            "Content_En" : content.Content_En
        }
        return record
    else:
        return {}

# Search Translated Content
def search_papers(request_Paper_ID):
    if not Papers.objects.filter(Paper_ID = request_Paper_ID).first().Content_Ja is None:
        content = Papers.objects.get(Paper_ID = request_Paper_ID)
        # Add 1 to Search_num
        content.Search_num += 1
        content.save()

        record = {
            "Paper_ID"      : content.Paper_ID,
            "Title_En"      : content.Title_En,
            "Title_Ja"      : content.Title_Ja,
            "Authors"       : content.Authors,
            "Categories"    : content.Categories,
            "Published"     : content.Published,
            "Content_En"    : content.Content_En,
            "Content_Ja"    : content.Content_Ja,
            "Content_plain" : content.Content_plain,
            "Pdf_url"       : content.Pdf_url
        }
        return record
    else:
        return {}

# Search extracted keywords and their descriptions
def search_keywords(request_Paper_ID):
    if Keywords.objects.filter(Paper_ID = request_Paper_ID).exists():
        record = Keywords.objects.get(Paper_ID = request_Paper_ID)
        return record
    else:
        return {}

# Add translated title
def add_title(title_data):  
    paper_record = Papers(
        Paper_ID = title_data["Paper_ID"],
        Title_En = title_data["Title_En"],
        Title_Ja = title_data["Title_Ja"],
        Categories = title_data["Categories"],
        Authors = title_data["Authors"],
        Pdf_url = title_data["Pdf_url"],
        Published = title_data["Published"],
        Content_En = title_data["Content_En"],
        Content_Ja = None,
        Content_plain = None,
        Search_num = 0
    )
    paper_record.save()

# Add translated content
def add_content(paper_data):
    paper_record = Papers.objects.get(Paper_ID = paper_data.Paper_ID)
    paper_record.Content_Ja = paper_data["Content_Ja"]
    paper_record.Content_plain = paper_data["Content_plain"]
    paper_record.Search_num = 1
    paper_record.save()


# After User login 

# Register
def add_user(user_data):
    user_record = Profile(
        User_ID = user_data["User_ID"],
        Name = user_data["Name"],
        Pass = user_data["Pass"]
    )
    user_record.save()


# Search User's history
def get_histry(request_User_ID):
    if Reads.objects.filter(Reader_ID = request_User_ID).exists():
        contents = Reads.objects.filter(Reader_ID = request_User_ID)
        records = {
            "Histries" : [{
                "Paper_ID" : content["Paper_ID"],
                "Title_En" : content["Title_En"],
                "Title_Ja" : content["Title_Ja"]
        }
        for content in contents
        ]}
        return records
    else:
        return {}


# def add_histry(read_data):




# delete all data in the database (for supervisor)

def delete():
    Papers.objects.all().delete()
    Keywords.objects.all().delete()
    Profile.objects.all().delete()
    Reads.objects.all().delete()
