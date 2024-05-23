import pytest
import gs_test

class Test_GS:
    def test_Sheet(self):
        sheet = gs_test.sheet
        assert sheet

    def test_Workspace(self):
        workspace = gs_test.worksheet
        assert workspace

    def test_Credentials(self):
        assert gs_test.credentials

    def test_Client(self):
        assert gs_test.client

    def test_Dict(self):
        assert gs_test.filtered_records != {}

    def test_Sort_Dict(self):
        assert gs_test.sorted_records != {}