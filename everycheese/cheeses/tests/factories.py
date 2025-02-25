import factory
import factory.fuzzy
import pytest
from django.template.defaultfilters import slugify

from everycheese.users.tests.factories import UserFactory

from ..models import Cheese


class CheeseFactory(factory.django.DjangoModelFactory):
    name = factory.fuzzy.FuzzyText()
    slug = factory.LazyAttribute(lambda obj: slugify(obj.name))
    description = factory.Faker('paragraph', nb_sentences=3, variable_nb_sentences=True)
    firmness = factory.fuzzy.FuzzyChoice([x[0] for x in Cheese.Firmness.choices])
    country_of_origin = factory.Faker('country_code')

    creator = factory.SubFactory(UserFactory) #associate cheese with a creator~user

    class Meta:
        model = Cheese

''' 
To test the factory:
In the shell, type this:
    
    from everycheese.cheeses.tests.factories import CheeseFactory
    cheese = CheeseFactory()
    cheese 
            -> <Cheese: sGwDovpLpggc>

'''

@pytest.fixture
def cheese():
    return CheeseFactory()