del *out*txt
REM c:\dev\runtime\artifacts\tests\coreclr\Windows.x64.Release\Tests\Core_Root\CoreRun.exe C:\dev\performance\artifacts\bin\GCPerfSim\Release\netcoreapp5.0\GCPerfSim.dll -tc 6 -tagb 100.0 -tlgb 2.0 -lohar 0 -pohar 0 -sohsi 10 -lohsi 0 -pohsi 0 -sohsr 100-4000 -lohsr 102400-204800 -pohsr 100-4000 -sohpi 10 -lohpi 0 -sohfi 0 -lohfi 0 -pohfi 0 -allocType reference -testKind time
c:\toolssw\debuggers\amd64\windbg.exe -c $$^>a^<autodbg.script c:\dev\runtime\artifacts\tests\coreclr\Windows.x64.Debug\Tests\Core_Root\CoreRun.exe C:\dev\performance\artifacts\bin\GCPerfSim\release\netcoreapp5.0\GCPerfSim.dll -tc 6 -tagb 100.0 -tlgb 2.0 -lohar 0 -pohar 0 -sohsi 10 -lohsi 0 -pohsi 0 -sohsr 100-4000 -lohsr 102400-204800 -pohsr 100-4000 -sohpi 10 -lohpi 0 -sohfi 0 -lohfi 0 -pohfi 0 -allocType reference -testKind time
