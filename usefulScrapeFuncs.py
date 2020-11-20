import re


def remove_html_tag(texte):
    """
    This function only returns the text content inside an HTML tag.
    :param texte: str. The full HTML tag.
    :return: The text content of a HTML tag.
    """
    texte = str(texte)

    if rep := re.match('(.*?)(<.*?>)(.*?)', texte):
        texte = texte.replace(rep.group(2), '')
    if '<' in texte and '>' in texte:
        return remove_html_tag(texte)
    if texte == '':
        return 'empty'

    return texte


def find_thing_in_tag(texte, what_we_are_looking_4):
    """
    This function returns the content of a choosen attribute (class, id, href...).
    :param texte: str. The full HTML tag.
    :param what_we_are_looking_4: An attibute.
    :return: The text content of the attibute.
    """
    texte = str(texte)

    if rep := re.match(f'(<.*?{what_we_are_looking_4}=")(.*?)(".*)', texte):
        return rep.group(2)
    return f"{what_we_are_looking_4} attibute not in {texte}"


if __name__ == '__main__':
    a = '<p class="dansPetitTitre" id="scrapeTorrent">Scrape des derniers torrents proposés par un site, ' \
        '<a class="lien" href="https://github.com/TomPlanche/torrentScrape">lien GitHub</a>.</p>'

    print(find_thing_in_tag(a, 'class'))
    print(find_thing_in_tag(a, 'id'))
    print(remove_html_tag(a))
