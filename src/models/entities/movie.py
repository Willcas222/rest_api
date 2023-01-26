from utils.DateFormat import DateFormat


class Movie():

    def __init__(self, id, titulo=None, duracion=None, fecha_estreno=None) -> None:
        self.id = id
        self.titulo = titulo
        self.duracion = duracion
        self.fecha_estreno = fecha_estreno

    def to_JSON(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'duracion': self.duracion,
            'fecha_estreno': DateFormat.convert_date(self.fecha_estreno)
        }
