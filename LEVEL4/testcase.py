import pytest
from level3.demooops import SystemDrive
from level3.demo_exception import FileSearcher
class Test_Drive:
    def test_drivecase(self):
        obj=SystemDrive()
        self.expected=obj.find_drive()
        self.actual=['C']
        assert self.expected==self.actual
    def test_searchfile(self):
        obj=FileSearcher()
        d=obj.search('C','pdf.txt')
        self.expected_filename=d[0]
        self.actual_res='C:\\Capstronproject\\level1\\pdf.txt'
        assert self.expected_filename==self.actual_res