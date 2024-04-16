"""Test my garden functions."""

__author__ = "730559378"

from lessons.garden.garden_helpers import add_by_kind, add_by_date, lookup_by_kind_and_date

#  Tests for add_by_kind function


def test_add_by_kind_use() -> None:
    """Tests if new plant was added under its kind."""
    by_kind: dict[str, list[str]] = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}
    new_plant_kind: str = "flower"
    new_plant: str = "daisy"
    add_by_kind(by_kind, new_plant_kind, new_plant)
    assert by_kind == {new_plant_kind: ["marigold", "zinnia", "daisy"], "vegetable": ["carrots"]}

  
def test_add_by_kind_edge() -> None:
    """Tests if the dictionary is empty."""
    by_kind: dict[str, list[str]] = dict()
    new_plant_kind: str = "fruit"
    new_plant: str = "watermelon"
    add_by_kind(by_kind, new_plant_kind, new_plant)
    assert by_kind == {"fruit": ["watermelon"]} 


#  Test for add_by_date function


def test_add_by_date_use() -> None:
    """Tests if plant is added under date."""
    by_date: dict[str, list[str]] = {"March": ["tulips"], "October": ["pumpkin"]}
    month: str = "May"
    plant: str = "squash"
    add_by_date(by_date, month, plant)
    assert by_date == {"March": ["tulips"], "October": ["pumpkin"], "May": ["squash"]}
  

def test_add_by_date_edge() -> None:
    """Tests if dictionary is empty."""
    by_date: dict[str, list[str]] = dict()
    month: str = "April"
    plant: str = "daisy"
    add_by_date(by_date, month, plant)
    assert by_date == {"April": ["daisy"]}

#  Tests for lookup_by_kind_and_date


def test_lookup_use() -> str:
    """Tests that a plant that appears in both lists is added to the combined list."""
    plants_by_kind: dict[str, list[str]] = {"flower": ["rose"], "vegetable": ["tomato"]}
    plants_by_date: dict[str, list[str]] = {"March": ["rose", "tulips"], "July": ["carrots"]}
    kind: str = "flower"
    month: str = "March"
    return_statement: str = lookup_by_kind_and_date(plants_by_kind, plants_by_date, kind, month)
    assert return_statement == "flowers to plant in March: ['rose']"


def test_lookup_edge() -> str:
    """Should return else statement when list is empty."""
    plants_by_kind: dict[str, list[str]] = {"flower": ["rose"], "vegetable": ["tomato"]}
    plants_by_date: dict[str, list[str]] = {"March": ["sunflowers", "tulips"], "July": ["carrots"]}
    kind: str = "flower"
    month: str = "March"
    return_statement: str = lookup_by_kind_and_date(plants_by_kind, plants_by_date, kind, month)
    assert return_statement == "No flowers to plant in March."