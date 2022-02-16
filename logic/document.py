class Document(object):
    """
    Class used to represent an Person
    """

    def __init__(self, tittle: str, authors: str = 'Autor', pub_date: int = "Fecha", id: int = 'Codigo'
                 ,edition: int = 'edicion', nropag: int = 'numeropaginas'):
        """ Person constructor object.

        :param id_person: id of person.
        :type id_person: int
        :param name: name of person.
        :type name: str
        :param last_name: last name of person.
        :type last_name: str
        :returns: Person object
        :rtype: object
        """
        self._tittle = tittle

    @property
    def tittle(self) -> str:
        """ Returns the name of the person.
          :returns: name of person.
          :rtype: str
        """
        return self._tittle

    @tittle.setter
    def tittle(self, tittle: str):
        """ The name of the person.
        :param name: name of person.
        :type: str
        """
        self._tittle = tittle

    def __str__(self):
        """ Returns str of person.
          :returns: sting person
          :rtype: str
        """
        return '({0})'.format( self.tittle)


if __name__ == '__main__':

    edwin = Document(tittle="Edwin")
    edwin.name = "Edwin. A"
    print(edwin)

