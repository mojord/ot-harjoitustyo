class Bone:
    """Class for storing the information of bone finds.
    Attributes:
        nisp: Number of fragments
        weight: Fragment weight
        classis: Animal class
        species: Animal species
        ossum: Name of bone
        element: Name of bone element
        side: Body side
        fragment: Whole or fragment
        comment: Comments about the find
        sizeclass: Sizeclass number relating to areas defined in sq cm
        part: Body part
        burndegree: Degree of burn for burned bone
        iuv: Juvenile individual
        cut: Presence of cutmarks
        findnr: Find number in excavation catalogue
        x: Excavation x coordinate
        y: Excavation y coordinate
        context: Context specification
        layer: Excavation layer
    """

    def __init__(self, nisp: int, weight: float, classis: str, species: str, ossum: str, element: str, side: str, fragment: str, comment: str, sizeclass: int, part: str, burndegree: str, iuv: str, cut: str, findnr: int, x: float, y: float, context: str, layer: int):
        """Constructor for creating a new bone
        Args:
            as Attributes.
        """
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
        self.x = x # pylint: disable=invalid-name
        self.y = y # pylint: disable=invalid-name
        self.context = context
        self.layer = layer

    def __str__(self):
        """Returns:
            bone in string format.
        """
        return f"bone: {self.nisp}, {self.weight}, {self.classis}, {self.species}, {self.ossum}, {self.element} {self.side}, {self.fragment}, {self.comment}, {self.sizeclass}, {self.part}, {self.burndegree}, {self.iuv}, {self.cut}, {self.findnr}, {self.x}, {self.y}, {self.context}, {self.layer}"