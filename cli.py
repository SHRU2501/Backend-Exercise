import argparse
from paper_fetcher import fetch_details,filter_papers
fetch_details("deep learning", max_results=5)

def main():
    parser = argparse.ArgumentParser(description="Fetch and filter PubMed papers.")
    parser.add_argument(
        "--ids", nargs="+", required=True,
        help="List of PubMed IDs to fetch papers for"
    )
    parser.add_argument(
        "--keyword", type=str, required=False,
        help="Keyword to filter abstracts"
    )
    
    args = parser.parse_args()

    print("[INFO] Fetching paper details...")
    papers = fetch_details(args.ids)

    if args.keyword:
        print(f"[INFO] Filtering papers by keyword: {args.keyword}")
        papers = filter_papers(papers, args.keyword)

    print(f"\n[RESULT] {len(papers)} paper(s) found:\n")
    for i, paper in enumerate(papers, start=1):
        print(f"{i}. Title: {paper.get('title', 'N/A')}")
        print(f"   Abstract: {paper.get('abstract', 'N/A')}\n")

if __name__ == "__main__":
    main()