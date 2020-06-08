@echo off
setlocal
set ANDREW_TARGET=C:\perf
set ANDREW_RUNTIME=C:\dev\runtime
robocopy /mir /z c:\dev\performance\src\benchmarks\gc %ANDREW_TARGET%\performance\src\benchmarks\gc
robocopy /mir /z c:\dev\performance\artifacts %ANDREW_TARGET%\performance\artifacts
robocopy /mir /z %ANDREW_RUNTIME%\artifacts\tests\coreclr\Windows.x64.Release\Tests\Core_Root %ANDREW_TARGET%\performance\artifacts\tests\coreclr\Windows.x64.Release\Tests\Core_Root
pushd %ANDREW_TARGET%\performance\src\benchmarks\gc
py . suite-create bench/suite --coreclrs %ANDREW_TARGET%\performance\artifacts\tests\coreclr\Windows.x64.Release\Tests\Core_Root %ANDREW_TARGET%\performance\artifacts\tests\coreclr\Windows.x64.Release\Tests\Core_Root --overwrite
popd
endlocal