import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QPushButton, QTextEdit, QLineEdit, QLabel, QMessageBox
)
from sdkFP.Guardar import Guardar
from sdkFP.Consultar import Consultar


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestor de Libros")
        self.setGeometry(100, 100, 400, 400)

        # Instancias de manejo de datos
        self.guardar = Guardar()
        self.consultar = Consultar()

        # Layout principal
        layout = QVBoxLayout()

        # Campos de entrada
        self.titulo = QLineEdit()
        self.autor = QLineEdit()

        # Área de resultado (solo lectura)
        self.resultado = QTextEdit()
        self.resultado.setReadOnly(True)

        # Etiquetas y campos
        layout.addWidget(QLabel("Título"))
        layout.addWidget(self.titulo)
        layout.addWidget(QLabel("Autor"))
        layout.addWidget(self.autor)

        # Botones
        boton_agregar = QPushButton("Agregar libro")
        boton_agregar.clicked.connect(self.accion_agregar_libro)

        boton_consultar = QPushButton("Consultar libros")
        boton_consultar.clicked.connect(self.accion_consultar_libros)

        # Añadir botones y resultados al layout
        layout.addWidget(boton_agregar)
        layout.addWidget(boton_consultar)
        layout.addWidget(self.resultado)

        self.setLayout(layout)

    def accion_agregar_libro(self):
        """Agrega un libro usando la clase Guardar."""
        titulo = self.titulo.text().strip()
        autor = self.autor.text().strip()

        # Validar campos vacíos
        if not titulo or not autor:
            QMessageBox.warning(self, "Campos vacíos", "Por favor, ingresa título y autor.")
            return

        # Guardar libro y mostrar mensaje
        try:
            mensaje = self.guardar.agregar(titulo, autor)
        except Exception as e:
            mensaje = f"Error al guardar el libro: {e}"

        self.resultado.setText(mensaje)

        # Limpiar campos
        self.titulo.clear()
        self.autor.clear()

    def accion_consultar_libros(self):
        """Consulta los libros registrados."""
        try:
            libros = self.consultar.consultar_libros()
        except Exception as e:
            self.resultado.setText(f"Error al consultar los libros: {e}")
            return

        if libros:
            # Mostrar libros con formato legible
            texto = "\n".join(libros)
            self.resultado.setText(texto)
        else:
            self.resultado.setText("No hay libros registrados.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = App()
    ventana.show()
    sys.exit(app.exec())
