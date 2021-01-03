import requests

def bourse_maroc(company):
    s = requests.Session()
    response = s.get(f'http://www.casablanca-bourse.com/bourseweb/Societe-Cote.aspx?codeValeur={str(company)}')
    cookies = response.cookies.get_dict()

    source = s.get('http://www.casablanca-bourse.com/BourseWeb/Telechargement/Telechargement-Histo-Valeur.aspx', cookies=cookies)
    if source.status_code == 200:
        with open(f"{str(company)}.aspx", 'wb') as f:
            f.write(source.content)

