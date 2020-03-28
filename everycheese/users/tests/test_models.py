import pytest                               
    #Import testing framework

from everycheese.users.models import User   
    #Import user model from Users

pytestmark = pytest.mark.django_db          
    #Drives the test database system


def test_user_get_absolute_url(user: User):
    assert user.get_absolute_url() == f"/users/{user.username}/"
