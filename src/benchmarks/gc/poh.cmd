del *out*txt
REM Good boy
c:\dev\runtime\artifacts\tests\coreclr\Windows.x64.Release\Tests\Core_Root\CoreRun.exe C:\dev\performance\artifacts\bin\GCPerfSim\release\netcoreapp5.0\GCPerfSim.dll -tc 6 -tagb 100.0 -tlgb 2.0 -lohar 0 -pohar 1 -sohsi 52 -lohsi 0 -pohsi 1 -sohsr 100-4000 -lohsr 102400-204800 -pohsr 100-4000 -sohpi 0 -lohpi 0 -sohfi 0 -lohfi 0 -pohfi 0 -allocType reference -testKind time
REM copy /y C:\Garbage\gc.log C:\Garbage\good.log
REM Bad boy
REM c:\dev\runtime\artifacts\tests\coreclr\Windows.x64.Release\Tests\Core_Root\CoreRun.exe C:\dev\performance\artifacts\bin\GCPerfSim\release\netcoreapp5.0\GCPerfSim.dll -tc 6 -tagb 100.0 -tlgb 2.0 -lohar 0 -pohar 1 -sohsi 142 -lohsi 0 -pohsi 1 -sohsr 100-4000 -lohsr 102400-204800 -pohsr 100-4000 -sohpi 0 -lohpi 0 -sohfi 0 -lohfi 0 -pohfi 0 -allocType reference -testKind time
REM copy /y C:\Garbage\gc.log C:\Garbage\bad.log
