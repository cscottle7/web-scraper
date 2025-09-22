# Web Scraper

This is a web scraping tool built with Scrapy that can scrape one or more websites and provide the data in a structured format.

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

To run the scraper, you need to provide a text file containing the URLs you want to scrape (one URL per line).

Navigate to the project's root directory (`Web Scraper`) in your terminal and use the following command:

```powershell
cd web_scraper; python -m scrapy crawl scraper -a file=<path_to_your_urls_file> -o <output_file>
```

### Arguments

*   `file`: (Required) The path to the text file containing the URLs to scrape (one URL per line).
*   `output_file`: (Required) The name of the file to save the scraped data to. The file extension determines the format (e.g., `.json`, `.csv`, `.xml`).

### Example

1.  Create a file named `urls.txt` in the `web_scraper` directory with the following content:

    ```
    https://quotes.toscrape.com
    https://alkalined.com.au/
    ```

2.  Run the following command to scrape the websites and save the data to a JSON file named `multi_output.json`:

    ```powershell
    cd web_scraper; python -m scrapy crawl scraper -a file=urls.txt -o multi_output.json
    ```

The output file will be saved in the `web_scraper` directory.
