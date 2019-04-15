# Web-Scrapping

This project is an exercise project of the Python Course from The Shortcut. The purpose is to let participants to learn and practise Python and web scrapping.

- This project uses BeautifulSoup4
- Data is collected from Gigantti website with search keyword "puhelin" and Oikotie
- As Gigantti is using infinite scrolling effect, and Oikotie is built with React, we use [Selenium] to automatically open the page, wait for it to render and collect to source HTML
- Later, the data collected will be save in a .csv file
