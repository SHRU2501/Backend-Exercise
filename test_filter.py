def filter_papers(papers, keyword=None, min_year=None):
    filtered = []

    for paper in papers:
        title = paper.get("title", "").lower()
        year = paper.get("year", 0)

        if keyword and keyword.lower() not in title:
            continue
        if min_year and year < min_year:
            continue

        filtered.append(paper)

    return filtered