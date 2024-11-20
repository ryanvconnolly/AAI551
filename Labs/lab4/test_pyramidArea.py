import pytest
import pyramidArea

def test_calcBaseArea():
    assert pyramidArea.calcBaseArea(15) == 225
    

@pytest.mark.xfail(reason="passing incompatible type")    
def test_calcBaseArea2():
    assert pyramidArea.calcBaseArea("5") == 25
    
def test_calcSideArea():
    result = pyramidArea.calcSideArea(15, 5)
    assert 270.41 <= result <= 270.42
    
def test_calcSideArea2():
    result = round(pyramidArea.calcSideArea(10,3), 2)
    assert result == 116.62

@pytest.mark.skip(reason="function prints text")   
def test_prntSurfArea():
    pyramidArea.prntSurfArea(15,10)
