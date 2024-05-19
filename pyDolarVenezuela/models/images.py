from dataclasses import dataclass

@dataclass
class Image:
    """
    Image instance
    """
    title: str
    image: str
    provider: str

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(title={self.title!r}, provider={self.provider!r}, image={self.image!r})'