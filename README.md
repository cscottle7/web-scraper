# Web Scraper

This is a web scraping tool built with Scrapy that can scrape a single page or a full website and provide the data in a structured format.

## Requirements

*   Python 3.x
*   Scrapy

## Installation

1.  Clone this repository or download the source code.
2.  Install the required Python packages using pip and the `requirements.txt` file:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the scraper, navigate to the project's root directory (`Web Scraper`) in your terminal and use the following command:

```powershell
cd web_scraper; python -m scrapy crawl scraper -a url=<target_url> -o <output_file>
```

### Arguments

*   `url`: (Required) The URL of the website you want to scrape.
*   `output_file`: (Required) The name of the file to save the scraped data to. The file extension determines the format (e.g., `.json`, `.csv`, `.xml`).

### Example

To scrape the website `https://quotes.toscrape.com` and save the data to a JSON file named `quotes.json`, run the following command:

```powershell
cd web_scraper; python -m scrapy crawl scraper -a url=https://quotes.toscrape.com -o quotes.json
```

The output file will be saved in the `web_scraper` directory.
