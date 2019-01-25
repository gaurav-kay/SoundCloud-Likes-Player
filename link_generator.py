from bs4 import BeautifulSoup

with open('likes.txt', 'r', encoding='utf-8') as f:
    file = f.read()

file_soup = BeautifulSoup(file, 'lxml')

likes_select = file_soup.select('a.playableTile__artworkLink.audibleTile__artworkLink')  # https://stackoverflow.com/questions/40305678/beautifulsoup-multiple-class-selector

likes_select = [str(i) for i in likes_select]  # .join() requires string

likes_select_string = " ".join(likes_select)

likes_select_string_soup = BeautifulSoup(likes_select_string, 'lxml')  # .find_all requires soup

all_links = [i['href'] for i in likes_select_string_soup.find_all('a', href=True)]

with open('likes_links.txt', 'w') as f:
    for i in all_links:
        f.write("https://soundcloud.com" + i)
        f.write('\n')


"""

one line implementation
with open('likes_links.txt', 'w') as f:
    for i in [i['href'] for i in BeautifulSoup(" ".join([str(i) for i in BeautifulSoup(file, 'lxml').select('a.playableTile__artworkLink.audibleTile__artworkLink')]), 'lxml').find_all('a', href=True)]:
        f.write("https://soundcloud.com" + i)
        f.write('\n')

"""
