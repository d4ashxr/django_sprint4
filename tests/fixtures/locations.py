import pytest
<<<<<<< HEAD
from mixer.backend.django import Mixer

from conftest import N_PER_FIXTURE
=======
from conftest import N_PER_FIXTURE
from mixer.backend.django import Mixer
>>>>>>> 7b47681 (Initial commit)


@pytest.fixture
def published_locations(mixer: Mixer):
    return mixer.cycle(N_PER_FIXTURE).blend("blog.Location")


@pytest.fixture
def published_location(mixer: Mixer):
    return mixer.blend("blog.Location", is_published=True)
