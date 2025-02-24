import sys
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QTextDocument, QTextCursor, QTextCharFormat, QFont, QSyntaxHighlighter
from PyQt5.QtCore import Qt, QRegularExpression, QRegularExpressionMatchIterator, QRegularExpressionMatch
from ui_filecontentview import Ui_FileContentView


class QueryHighlighter(QSyntaxHighlighter):
    def __init__(self, parent=None, query=None):
        super(QueryHighlighter, self).__init__(parent)
        self.query = query

    def highlightBlock(self, text):
        highlightFormat = QTextCharFormat()
        highlightFormat.setForeground(Qt.red)
        highlightFormat.setBackground(Qt.black)
        highlightFormat.setFontWeight(QFont.Bold)

        regex = QRegularExpression(self.query)
        it = regex.globalMatch(text)
        while(it.hasNext()):
            match = it.next()
            self.setFormat(match.capturedStart(),
                           match.capturedLength(), highlightFormat)


class FileContentView(QWidget):
    def __init__(self):
        super(FileContentView, self).__init__()

        self.ui = Ui_FileContentView()
        self.ui.setupUi(self)

    def openHighlightedDocument(self, fileContent, query):
        textDocument = QTextDocument()
        textDocument.setPlainText(fileContent)
        highlighter = QueryHighlighter(textDocument, query)

        self.ui.popup_text_box.setDocument(textDocument)
