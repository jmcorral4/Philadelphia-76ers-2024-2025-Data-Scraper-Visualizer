# Philadelphia-76ers-2024-2025-Data-Scraper-Visualizer
This project is a Python script that scrapes, processes, and visualizes data for the Philadelphia 76ers’ 2024-25 NBA season. It uses web scraping to collect roster, game results, and player stats, then creates visualizations to help analyze the team’s performance.

# 🏀 Project Overview & Learning Journey
This project is my first major step beyond basic Python scripting.
Previously, I built simple scripts like intro_script.py (for basic Python practice) and calculator_script.py (a command-line calculator).
Those projects focused on learning syntax, user input, and basic logic.

With this NBA data project, I challenged myself to:

Work with real-world, messy data from the web
Use multiple third-party libraries
Parse, clean, and visualize complex datasets
Debug and adapt my code to changing data formats

# My Approach
1. Define the goal: Automate the collection and visualization of NBA data.
2. Use AI to guide each step: From web scraping to data cleaning to plotting.
3. Debug and adapt: Print outputs, adjust regex, and refine logic based on real data.
4. Document and reflect: Capture what I learned and how I solved problems.

# How This Project Differs from My Previous Scripts
| Aspect |	Simple Scripts (intro_script.py, calculator_script.py) |	NBA Data Project (this repo) |
| --- | --- | --- |
| Input	| User/console input	| Live web data (HTML tables) |
| Data Handling	| Basic variables, lists	| DataFrames, regex, data cleaning |
| Dependencies	| None or standard library	| requests, bs4, pandas, lxml, matplotlib, seaborn |
| Debugging	| Minimal, easy to trace	| Extensive, with print/debugging |
| Output	| Console text	| Console + visual charts |
| Error Handling	| Basic	| Must handle missing/changed data |
| Documentation	| Minimal	| Essential for reproducibility | <br>
# What I Tried To Do
1. <ins>Scrape the Roster Table<ins>
  - Goal: Automatically fetch and display the current 76ers roster.
  - What I learned:
      - How to use requests and BeautifulSoup to fetch and parse HTML.
      - How to use pandas.read_html to extract tables.
      - The importance of checking for missing or changed tables.<br>
![image](https://github.com/user-attachments/assets/5d238d2f-b569-4de5-80c7-a2659ceeab2b)
2. <ins>Scrape and Visualize Game Results<ins>
  - Goal: Analyze and visualize the team’s win/loss record and home/away performance.
  - What I learned:
      - How to clean up web-scraped tables (removing repeated headers, finding the right columns).
      - How to use matplotlib and seaborn for pie and bar charts.
      - How to debug by printing intermediate results and confirming calculations.<br>
 ![image](https://github.com/user-attachments/assets/609fa67d-b47c-49cb-b5c3-b5f9ac1977d7)
     
3. <ins>Scrape and Visualize Player Stats from the Depth Chart<ins>
  - Goal: Extract and visualize individual player stats (points, rebounds, assists, win shares).
  - What I learned:
      - How to handle inconsistent data (player names with/without position labels).
      - How to use regular expressions to match and extract stats.
      - The importance of printing every line being parsed to debug regex issues.
      - How to build a DataFrame for plotting, and dynamically adjust chart size for readability.
      - How grouping by position could make charts more readable (future improvement). <br>
# What’s Required to Succeed in a Project Like This
- Patience and persistence: Real-world data is messy and web pages change.
- Debugging skills: Print statements and DataFrame inspection are essential.
- Regex and string manipulation: For extracting data from inconsistent formats.
- Understanding of libraries: Knowing what tools are available and how to use them together.
- Visualization: Making results clear and meaningful with charts. <br>
# What’s Next
- Improve parsing to group players by position for clearer charts.
- Generalize the script for other teams or seasons.
- Add error handling and logging for robustness. <br>
# Leveraging AI to Accelerate Learning and Problem Solving
Although my Python skills are still developing, this project demonstrates how I can apply minimal coding knowledge—augmented by AI tools—to build practical, real-world solutions. By using AI (like GitHub Copilot or ChatGPT), I was able to:

- Break down complex problems into manageable steps, even when I didn’t know the exact syntax or libraries to use.
- Quickly research and implement best practices for web scraping, data cleaning, and visualization.
- Troubleshoot and debug issues by asking targeted questions and iteratively refining my code.
- Learn new libraries and techniques (requests, BeautifulSoup, pandas, matplotlib, seaborn, regex) on the fly, guided by AI suggestions and explanations.
# This project is proof that, with the help of AI, I can take initiative, learn new skills rapidly, and deliver real-world results—even with a basic starting point. This mindset and workflow are directly transferable to IT security, where adaptability and problem-solving are essential.
