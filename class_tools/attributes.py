class Organism:
    """
    A class to represent an organism.

    Attributes
    ----------
    domain : str
        The domain of the organism.
    kingdom : str
        The kingdom of the organism.
    phylum : str
        The phylum of the organism.
    class_name : str
        The class of the organism.
    order : str
        The order of the organism.
    family : str
        The family of the organism.
    genus : str
        The genus of the organism.
    species : str
        The species of the organism.
    """
    def __init__(
        self,
        domain: str,
        kingdom: str,
        phylum: str,
        class_name: str,
        order: str,
        family: str,
        genus: str,
        species: str,
    ) -> None:
        """
        Constructs all the necessary attributes for the organism object.

        Parameters
        ----------
        domain : str
            The domain of the organism.
        kingdom : str
            The kingdom of the organism.
        phylum : str
            The phylum of the organism.
        class_name : str
            The class of the organism.
        order : str
            The order of the organism.
        family : str
            The family of the organism.
        genus : str
            The genus of the organism.
        species : str
            The species of the organism.
        """
        self.domain: str = domain
        self.kingdom: str = kingdom
        self.phylum: str = phylum
        self.class_name: str = class_name
        self.order: str = order
        self.family: str = family
        self.genus: str = genus
        self.species: str = species

    def display_info(self) -> None:
        """Displays the organism's information."""
        print(f"\n{self.kingdom=}\t{self.phylum=}\t{self.class_name=}")


# Instantiate Organism classes
human: Organism = Organism(
    "Eukarya",
    "Animalia",
    "Chordata",
    "Mammalia",
    "Primates",
    "Hominidae",
    "Homo",
    "sapiens",
)
housecat: Organism = Organism(
    "Eukarya",
    "Animalia",
    "Chordata",
    "Mammalia",
    "Carnivora",
    "Felidae",
    "Felis",
    "catus",
)
houseplant: Organism = Organism(
    "Eukarya",
    "Plantae",
    "Angiosperms",
    "Eudicots",
    "Rosales",
    "Rosaceae",
    "Rosa",
    "chinensis",
)

# Check if an attribute exists
if hasattr(human, "kingdom"):
    print("The human has a 'kingdom' attribute.")

# Get the value of an attribute
human_kingdom: str = getattr(human, "kingdom", "Unknown")
print(f"The kingdom of the human is: {human_kingdom}")

# Set the value of an attribute
setattr(housecat, "order", "Carnivora")
print(f"The order of the housecat is: {housecat.order}")

# Delete an attribute
delattr(houseplant, "class_name")
if not hasattr(houseplant, "class_name"):
    print("The 'class_name' attribute has been deleted.")

# Display organism information
human.display_info()
housecat.display_info()
if hasattr(houseplant, "class_name"):
    houseplant.display_info()
else:
    print("houseplant does not have a 'class_name' attribute.")
