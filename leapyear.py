# se importan las librerias requests_html la propiedad HTMLSession para crear la session
# pickle Para guardar los datos de la variable en Binario
from requests_html import HTMLSession
import pickle
# se inicialisa HTMLSession y de asigna a una bariable
session = HTMLSession()
URL = "https://www.calendario-365.es/anos-bisiestos.html"


def leap_year(year):
    # se optienen los datos desde la web si no existe el archivo .pkl y si no esta lo crea
    l_year = []
    try:
        print("cargando el Archivo..")
        with open("leapyfile.pkl", "rb") as leapfile:
            l_year = pickle.load(leapfile)
    except FileNotFoundError:
        print("archivo no en contrado")
        for a in year.html.find(".fbold"):
            l_year.append(a.find(".fbold", first=True).text)
        with open("venv/leapyfile.pkl", "wb") as leapfile:
            pickle.dump(l_year, leapfile)
    return l_year


def compare_year(year_comp, years):
    # optiene el año y comprueba si es bisiesto o No
    year_result = ""
    for comp in years:
        if year_comp == comp:
            year_result = comp
    if year_comp == year_result:
        print("{} Es bisiesto".format(year_comp))
    else:
        print("{} No es Bisiesto".format(year_comp))


def loop_year(years):
    #loop para mantener el programa abierto 
    option = "S"
    while option == "S":
        year_comp = input("ingrese el año a comparar: ")
        compare_year(year_comp, years)
        option = input("Desea continuar... [S] o [N]")


def main():
    url = URL
    year = session.get(url)
    years = leap_year(year)
    loop_year(years)


if __name__ == "__main__":
    main()
