import pytest

from django.shortcuts import reverse
from django.test import Client


@pytest.mark.django_db
@pytest.mark.parametrize('view_name', [
    'person_list',
    'missing_doc',
])
def test_list_views(view_name):
    url = reverse(view_name)
    c = Client()
    response = c.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
@pytest.mark.parametrize('url', [
    '/webapp/login/',
    '/webapp/home/',
    # '/webapp/new-member/',
    # '/webapp/new-family/',
    # '/webapp/list/',
])
def test_views_exist(url):
    c = Client()
    response = c.get(url)
    assert response.status_code == 200
