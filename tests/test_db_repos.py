import pytest

from personal_website.db_repos import create_initial_database, MinifiedRepo


class TestDatabaseRepos:
    @pytest.yield_fixture(autouse=True)
    def before_and_after(self):
        create_initial_database()  # before
        yield
        # wipe_database()  # after

    def test_initial_default_max_for_minified_table_is_1(self):
        assert MinifiedRepo.get_max_id() == 1
