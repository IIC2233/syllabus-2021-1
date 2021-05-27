from copy import copy


class IterableDescuentos:
    # NO MODIFICAR
    def __init__(self, mascotas):
        self.mascotas = mascotas

    def __iter__(self):
        return IteradorDescuentos(self)


class IteradorDescuentos:
    def __init__(self, iterable):
        # NO MODIFICAR
        self.iterable = copy(iterable)

    def __iter__(self):
        # Debes completar este método
        pass

    def __next__(self):
        # Debes completar este método
        pass
