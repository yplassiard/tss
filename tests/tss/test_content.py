from src.tss.content import *

def test_content_init():
    c = StationContent(StationContentType.LINE)
    assert c.getContentType() == StationContentType.LINE
