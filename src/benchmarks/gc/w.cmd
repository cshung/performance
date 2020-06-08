cd   C:\dev\performance\src\benchmarks\gc\src\exec\GCPerfSim
call C:\dev\runtime\dotnet.cmd build -c release
cd   C:\dev\performance\src\benchmarks\gc\src\analysis\managed-lib
call C:\dev\runtime\dotnet.cmd publish
cd   C:\dev\performance\src\benchmarks\gc\src\exec\env
call build.cmd
cd   C:\dev\performance\src\benchmarks\gc
call py . setup
call py . suite-create bench/suite --coreclrs c:\dev\runtime\artifacts\tests\coreclr\Windows.x64.Release\Tests\Core_Root --overwrite
