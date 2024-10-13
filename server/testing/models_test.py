import pytest
from models import db, Earthquake

def test_new_earthquake():
    earthquake = Earthquake(magnitude=5.5, latitude=40.7128, longitude=-74.0060, depth=10.5)
    assert earthquake.magnitude == 5.5
    assert earthquake.latitude == 40.7128
    assert earthquake.longitude == -74.0060
    assert earthquake.depth == 10.5

class TestEarthquake:
    def test_can_be_instantiated(self):
        earthquake = Earthquake()
        assert isinstance(earthquake, Earthquake)

    def test_has_attributes(self):
        attributes = ['id', 'magnitude', 'latitude', 'longitude', 'depth']
        for attr in attributes:
            assert hasattr(Earthquake, attr)

    def test_superclasses(self):
        assert issubclass(Earthquake, db.Model)

    def test_dictionary(self):
        earthquake = Earthquake(magnitude=5.5, latitude=40.7128, longitude=-74.0060, depth=10.5)
        assert earthquake.to_dict() == {
            'id': None,
            'magnitude': 5.5,
            'latitude': 40.7128,
            'longitude': -74.0060,
            'depth': 10.5
        }
