import pytest
from ..models import Cheese
from .factories import CheeseFactory

#Connects our tests to database
pytestmark = pytest.mark.django_db

'''OLD WAY:
def test___str__():
    cheese = Cheese.objects.create(name="Stracchino",description="Semi-sweet cheese that goes well with starches",firmness=Cheese.Firmness.SOFT,)
    assert cheese.__str__()=="Stracchino"
    assert str(cheese)=="Stracchino"
'''

# NEW WAY
def test___str__():
    cheese = CheeseFactory()
    assert cheese.__str__() == cheese.name
    assert str(cheese) == cheese.name

    