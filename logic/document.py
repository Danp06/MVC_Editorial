from datetime import date


class Document(object):
    """
    Class used to represent an document
    """

    def __init__(
            self, tittle: str, authors: str = "Autor",
            pub_date: date = date.today(), id_document: int = 000,
            edition: int = 000, nropag: int = 000):
        """ Document constructor object.

        :param tittle: name of document.
        :type tittle: str
        :param pub_date: date of publication of document.
        :type pub_date: date
        :param id_document: id of document.
        :type id_document: int
        :param edition: edition of document.
        :type: int
        :param nropag: number of pages of document.
        :type: int
        """
        self._tittle = tittle
        self._id_document = id_document
        self._pub_date = pub_date
        self._edition = edition
        self.nropag = nropag

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
        :param tittle: name of document.
        :type: str
        """
        self._tittle = tittle

    @property
    def pub_date(self) -> date:
        """ Returns the name of the document.
          :returns: date of publication of document.
          :rtype: date
        """
        return self._pub_date

    @pub_date.setter
    def pub_date(self, pub_date: date):
        """ The name of the document.
        :param pub_date: name of document.
        :type: date
        """
        self._pub_date = pub_date

    @property
    def id_document(self) -> int:
        """ Returns id document of the document.
          :returns: id of document.
          :rtype: int
        """
        return self._id_document

    @id_document.setter
    def id_document(self, id_document: int):
        """ The id of the document.
        :param id_document: id of document.
        :type: int
        """
        self._id_document = id_document

    @property
    def edition(self) -> int:
        """ Returns edition of the document.
          :returns: edition of document.
          :rtype: int
        """
        return self._edition

    @edition.setter
    def edition(self, edition: int):
        """ The edition of the document.
        :param edition: edition of document.
        :type: int
        """
        self._edition = edition

    @property
    def nropag(self) -> int:
        """ Returns number of pages of the document.
          :returns: number of pages of document.
          :rtype: int
        """
        return self._nropag

    @nropag.setter
    def nropag(self, nropag: int):
        """ The number of pages of the document.
        :param nropag: number of pages of document.
        :type: int
        """
        self._nropag = nropag

    def __str__(self):
        """ Returns str of document.
          :returns: sting document
          :rtype: str
        """
        return '({0}, {1}, {2}, {3} edition, {4} pag)'.format(self.tittle, self.id_document,
                                                              self.pub_date, self.edition, self.nropag)


if __name__ == '__main__':

    d = Document(tittle="El Principito", id_document=341, pub_date=date.today(), edition=3, nropag=70)
    d.tittle = "Primer Libro"
    print(d)
