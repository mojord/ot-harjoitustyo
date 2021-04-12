
class Bone:
    def __init__(self, nisp: int, weight: float, classis: str, species: str, ossum: str, element: str, side: str, fragment: str, comment: str, sizeclass: int, part: str, burndegree: str, iuv: str, cut: str, findnr: int, x: float, y: float, context: str, layer: int):
        self.nisp = nisp
        self.weight = weight
        self.classis = classis
        self.species = species
        self.ossum = ossum
        self.element = element
        self.side = side
        self.fragment = fragment
        self.comment = comment
        self.sizeclass = sizeclass
        self.part = part
        self.burndegree = burndegree
        self.iuv = iuv
        self.cut = cut
        self.findnr = findnr
        self.x = x
        self.y = y
        self.context = context
        self.layer = layer

    def __str__(self):
        return f"bone: {self.nisp}, {self.weight}, {self.classis}, {self.species}, {self.ossum}, {self.element} {self.side}, {self.fragment}, {self.comment}, {self.sizeclass}, {self.part}, {self.burndegree}, {self.iuv}, {self.cut}, {self.findnr}, {self.x}, {self.y}, {self.context}, {self.layer}"
