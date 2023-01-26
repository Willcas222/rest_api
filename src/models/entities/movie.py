class Movie():

    def __init__(self, id, titulo=None, duracion=None, fecha_sale=None) -> None:
        self.id = id
        self.titulo = titulo
        self.duracion = duracion
        self.fecha_sale = fecha_sale

    def to_JSON(self):
        return {
            'id': self.id,
            'title': self.titulo,
            'duration': self.duracion,
            'released': self.fecha_sale
        }
