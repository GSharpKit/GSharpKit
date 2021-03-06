Name:           darwinx-GdlSharp
Version:        3.34.0
Release:        2%{?dist}
Summary:        Max OS X GDL library

License:        LGPLv2+
Group:          Development/Libraries
URL:            https://github.com/GSharpKit/GdlSharp/releases
Source0:        GdlSharp-%{version}.tar.xz
Patch0:         gdl-sharp-ref.patch

BuildArch:      noarch

BuildRequires:  darwinx-filesystem-base >= 18
BuildRequires:  darwinx-libgdl >= %{version}

Requires:  	darwinx-filesystem >= 18
Requires:  	darwinx-libgdl >= %{version}

%description
GTK+ is a multi-platform toolkit for creating graphical user
interfaces. Offering a complete set of widgets, GTK+ is suitable for
projects ranging from small one-off tools to complete application
suites.

%prep
%setup -q -n GdlSharp-%{version}

sed -i '' 's!${NETSTANDARD_REFERENCE_DIR}!/Library/Frameworks/GSharpKit/lib/mono/xbuild-frameworks/.NETStandard/netstandard2.0!g' configure.ac

%build
mkdir -p m4
autoreconf  -i --force --warnings=none -I . -I m4
%{_darwinx_configure}
%{_darwinx_make} %{?_smp_mflags} V=1

rm out/gdl-sharp.dll
pushd sources/generated/Gdl
patch -p0 Dock.cs < %{PATCH0}
popd
%{_darwinx_make} %{?_smp_mflags} V=1


%install
rm -rf $RPM_BUILD_ROOT
#{_darwinx_make} install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_darwinx_libdir}
cp out/gdl-sharp.dll $RPM_BUILD_ROOT%{_darwinx_libdir}/
cp out/gdl-sharp.dll.config $RPM_BUILD_ROOT%{_darwinx_libdir}/
sed -i '' 's!libgdl-3.so.5!libgdl-3.5.dylib!' $RPM_BUILD_ROOT%{_darwinx_libdir}/gdl-sharp.dll.config

mkdir -p $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/
cp gdl-sharp-3.pc $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/
sed -i '' 's!mono/gdl-sharp/!!g' $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/gdl-sharp-3.pc

%files -n darwinx-GdlSharp
%{_darwinx_libdir}/gdl-sharp.dll
%{_darwinx_libdir}/gdl-sharp.dll.config
%{_darwinx_datadir}/pkgconfig/gdl-sharp-3.pc

%changelog
* Tue Nov 04 2014 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 3.12.0-1
- Initial RPM release
