from beings import Person

import pytest

@pytest.fixture()
def person():
  return Person("Rick Hoppe", 29, jobs=["Software Engineer"])

# Always good to add a type hint here
def test_init(person: Person):
  assert person.name == "Rick Hoppe"
  assert person.age == 29
  assert person.jobs == ["Software Engineer"]

def test_forename(person: Person):
  assert person.forename == "Rick"

def test_surname(person: Person):
  assert person.surname == "Hoppe"

# Example for how program handle unusual occurrence in data
def test_no_surname(person: Person):
  person.name = "Rick"
  assert not person.surname

def test_celebrate_birthday(person: Person):
  person.celebrate_birthday()
  assert person.age == 30

def test_add_job(person: Person):
  person.add_job("Solutions Architect")
  assert person.jobs == ["Software Engineer", "Solutions Architect"]
