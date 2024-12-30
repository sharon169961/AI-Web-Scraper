# AI Web Scraper

An AI-powered web scraping tool that combines Python, Streamlit, Selenium, and AI models to extract and parse specific content from websites. This project is designed to make web scraping intuitive, flexible, and robust for all users.

## Features

- **Website Scraping**: Fetch website data efficiently using Selenium.
- **Content Cleaning**: Process raw HTML to extract and clean the main content.
- **AI-Powered Parsing**: Use the Llama3 AI model to parse and extract relevant information based on custom descriptions.
- **User-Friendly Interface**: A simple, interactive interface built with Streamlit.

## How It Works

1. **Input URL**: Enter the website URL in the Streamlit app.
2. **Scrape Content**: Fetch and clean the HTML content of the page.
3. **Parse Data**: Use the integrated AI to extract specific information based on your instructions.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ai-web-scraper.git
   cd ai-web-scraper
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download ChromeDriver:
   - Place the ChromeDriver executable in the root folder.
   - Ensure the ChromeDriver version matches your Chrome browser version. [Download here](https://chromedriver.chromium.org/).

4. Run the application:
   ```bash
   streamlit run main.py
   ```

## Technologies Used

- **Python**: The core programming language.
- **Streamlit**: For building the interactive web interface.
- **Selenium**: For web scraping and DOM extraction.
- **BeautifulSoup**: For cleaning and processing HTML.
- **LangChain**: To integrate with the Llama3 AI model for parsing.

## Contributing

Contributions are welcome! If you'd like to improve this project, feel free to fork the repository, open an issue, or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- **OpenAI**: For providing insights into AI-driven solutions.
- **Streamlit and Selenium**: For making web scraping accessible and user-friendly.

