from datetime import date
class Document(object):
    """
    Class used to represent an Person
    """

    def __init__(self, tittle: str, authors: str = 'Autor', pub_date: date.today(), id: int = 'Codigo'
                 ,edition: int = 'edicion', nropag: int = 'numeropaginas'):
        """ Person constructor object.

        :param tittle: name of document.
        :type tittle: str
        """
        self._tittle = tittle

    @property
    def tittle(self) -> str:
        """ Returns the name of the document.
          :returns: name of document.
          :rtype: str
        """
        return self._tittle

    @tittle.setter
    def tittle(self, tittle: str):
        """ The name of the document.
        :param name: name of document.
        :type: str
        """
        self._tittle = tittle

    def __str__(self):
        """ Returns str of document.
          :returns: sting document
          :rtype: str
        """
        return '({0})'.format( self.tittle)


if __name__ == '__main__':

    edwin = Document(tittle="El principito")
    edwin.name = "Principito"
    print(Document)

