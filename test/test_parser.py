from pathlib import Path
from pprint import pprint

from app import app
from app.db import Db
from app.parser import (feature_index, find_co_path, get_feature_record,
                        parse_surfaces_csv)


def test_connection_to_godzilla():
    """Load and return the feature index."""
    conn = Db()
    res = conn.get_query("Select 1 as idx;")
    print(res)
    assert res[0][0] == 1


def test_feature_index():
    """Load and return the feature index."""
    conn = Db(dbfile=app.config["FEATURE_INDEX_GPKG_STORAGE"])
    fi = feature_index(conn)
    assert len(fi) > 1


def test_parse_surfaces_csv():
    p = Path("test/resources/997_lod2_surface_areas.csv")
    res = parse_surfaces_csv(p)


def test_get_feature_surfaces():
    p = Path("test/resources/997_lod2_surface_areas.csv")
    surfaces_gen = parse_surfaces_csv(p)
    rec = get_feature_record("NL.IMBAG.Pand.1655100000488643-0", surfaces_gen)
    pprint(rec)


def test_find_co_path():
    res = find_co_path("/data", "NL.IMBAG.Pand.1655100000548671", "997")
    print(res)
