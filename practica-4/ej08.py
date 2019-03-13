import json
import csv
import os

class Exportar():

    def setear_formatos(self, *formato):
        self._entrada = formato[0].lower()
        self._salida = formato[1].lower()

    def _jsonToCsv(self, archivo):
        archivo_csv = open(os.path.join("archivos", "generado.csv"), "w")     # Creo el archivo a generar
        contenido_json = json.load(archivo)    # Cargo el contenido del json
        fieldnames = list(contenido_json[0].keys())  # Obtengo la cabecera
        writer = csv.DictWriter(archivo_csv, fieldnames=fieldnames)
        writer.writeheader()    # Escribo la cabecera
        for dicc_json in contenido_json[1:]:  # Comienzo a escribir el contenido
            writer.writerow(dicc_json)  # Escribo el contenido
        archivo_csv.close()

    def _csvToJson(self, archivo):
        archivo_json = open(os.path.join("archivos", "generado.json"), "w")
        dicc_csv = list(csv.DictReader(archivo))
        json.dump(dicc_csv, archivo_json, ensure_ascii=False)
        archivo_json.close()

    def exportar(self, archivo):
        if self._entrada == "json":
            self._jsonToCsv(archivo)
            return True
        elif self._entrada == "csv":
            self._csvToJson(archivo)
            return True
        else:
            return False

# Testing
if __name__ == "__main__":
    archivo_csv = open(os.path.join("archivos", "csvtest.csv"), "r")
    archivo_json = open(os.path.join("archivos", "generado.json"), "r")
    exp = Exportar()
    exp.setear_formatos("json", "csv")
    exp.exportar(archivo_json)
    archivo_csv.close()
    archivo_json.close()
