# Fetching Research Papers 

A Python CLI tool to fetch and filter research papers from **PubMed** and **Semantic Scholar** based on user-defined queries. Designed to assist researchers and developers in retrieving relevant scientific literature efficiently



<img width="960" height="540" alt="image" src="https://github.com/user-attachments/assets/c815e16e-94a0-4b60-ade7-ddf6f7698d1a" />


##  Features

- Fetch papers using PubMed and Semantic Scholar APIs
- Filter results by keyword, year, or author
- Export metadata to JSON or CSV
- CLI tool built with **Typer**
- Modular codebase for easy extension

## Tech Stack

- Python 3.10+
- Typer (CLI)
- Requests (for API calls)
- Poetry (for dependency management)

##  Installation

## CSV Output Sample


Sure thing, Shruti! Here's your CSV data beautifully formatted into a markdown table:

---

### Research Paper Metadata (Sample Output)

| PubmedID | Title                                       | Publication Date | Non-academic Author(s) | Company Affiliation(s) | Corresponding Author Email       |
|----------|---------------------------------------------|------------------|--------------------------|--------------------------|----------------------------------|
| 38712945 | Deep Learning for Oncology Biomarkers       | 2025-05-12       | Dr. Maya Reddy           | Novartis                 | maya.reddy@novartis.com          |
| 38679120 | MicroRNA Signatures in Rare Diseases        | 2024-11-22       | Rajiv Menon              | BioGenix                 | rajiv.menon@biogenix.com         |
| 38702566 | AI-Driven Clinical Trials Optimization       | 2025-01-19       | Neha Kapoor              | AstraZeneca              | neha.kapoor@astrazeneca.com      |
| 38693288 | Real-world Impact of Genomic Profiling      | 2023-09-03       | Jason Li                 | Pfizer                   | jason.li@pfizer.com              |
| 38681050 | Digital Twins in Drug Development           | 2024-03-27       | Dr. Aditi Rao            | GSK                      | aditi.rao@gsk.com                |

---

```bash
# Clone the repository
git clone https://github.com/SHRU2501/Fecthing-Research-Paper-.git
cd Fecthing-Research-Paper-

# Install dependencies via Poetry
poetry install

# Run CLI tool
python main.py --query "bioinformatics" --limit 10 --source "pubmed"


Parameter	Description
--query	Keyword to search for
--source	"pubmed" or "semantic"
--limit	Number of results to fetch
--year	Filter by publication year
--author	Search papers by author name

Results are saved in:-
output.json or output.csv
Contains: Title, Abstract, Authors, Year, Journal info

This project is licensed under the MIT License.

Acknowledgments
PubMed API

Semantic Scholar API
