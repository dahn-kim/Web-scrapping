from bs4 import BeautifulSoup

with open('gigantti_laptop.html', encoding="utf8") as html_file: #default reading mode.
    soup = BeautifulSoup(html_file, 'html.parser')

containers = soup.findAll('div', class_="mini-product") # 'class_' = class keyword is reserved to create a Class. but 'mini-product' is a class for html css # beautiful soup is going to find all divs with a class 'mini-product'
#everything will be saved in containers


csv_file = "gigantti_laptop.csv"
file = open(csv_file, 'w') #writing mode
headers = "Product Name, Product  Number, Product Price\n"
file.write(headers)

for cont in containers:
    product_number = cont.findChild('div', class_="product-number").text
    product_name = cont.findChild('span',class_="table-cell").text
    product_price = cont.findChild('div', class_="product-price").text

    file.write("{},{},{}\n".format(product_name.replace(",","."), product_number, product_price)) #a new raw added with \n
        # because product name already contains coma ',' we will replace with a dot

file.close()
print("done!")


# print(len(containers))

# container_1 = containers[200]
# # print(container_1)
# product_1_number = container_1.findChild('div', class_="product-number")
# print(product_1_number)
# product_1_number = product_1_number.texts
#
# prod_name = container_1.findChild('span',class_="table-cell").text #just to get the product name deleting all html code
# # print(prod_name)
#
# prod_price = container_1.findChild('div', class_="product-price").text
# print(prod_price + "euros")
