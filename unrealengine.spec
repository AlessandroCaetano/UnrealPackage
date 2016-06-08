%define debug_package %{nil}

Name: UnrealEngine	
Version: 4.11.2
Release: 1
Summary: UnrealEngine	

Group: Application/Tools
License: Unreal Engine License
URL: https://unrealengine.com
Source0: %{name}-%{version}.tar.gz
BuildRequires: mono-core mono-devel dos2unix cmake gcc-c++ gtk3-devel clang qt qt-creator
Requires: mono-core cmake gcc-c++

%description


%prep
%setup -q


%build
./Setup.sh
find Engine/Source/Programs/AutomationTool -name "*Automation.csproj" -exec sed -i "s/ToolsVersion=\"11.0\"/ToolsVersion=\"4.0\"/g" "{}" \;
./GenerateProjectFiles.sh
make UE4Client SlateViewer ShaderCompileWorker UnrealLightmass UnrealPak UE4Editor

%install
mkdir -p %{buildroot}/usr/bin/

install -m755 %{_builddir}/UnrealEngine-4.11.2/Engine/Binaries/Linux/UE4Editor %{buildroot}/usr/bin/
install -m755 %{_builddir}/UnrealEngine-4.11.2/Engine/Binaries/Linux/SlateViewer %{buildroot}/usr/bin/
install -m755 %{_builddir}/UnrealEngine-4.11.2/Engine/Binaries/Linux/ShaderCompileWorker %{buildroot}/usr/bin/
install -m755 %{_builddir}/UnrealEngine-4.11.2/Engine/Binaries/Linux/UnrealLightmass %{buildroot}/usr/bin/
install -m755 %{_builddir}/UnrealEngine-4.11.2/Engine/Binaries/Linux/UnrealPak %{buildroot}/usr/bin/
install -m755 %{_builddir}/UnrealEngine-4.11.2/Engine/Binaries/Linux/UE4Client %{buildroot}/usr/bin/

%files
%doc
/usr/bin/UE4Editor
/usr/bin/SlateViewer
/usr/bin/ShaderCompileWorker
/usr/bin/UnrealLightmass
/usr/bin/UnrealPak
/usr/bin/UE4Client

%changelog

