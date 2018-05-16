Name:           darwinx-GdlSharp
Version:        3.26.0
Release:        1%{?dist}
Summary:        Max OS X GDL library

License:        LGPLv2+
Group:          Development/Libraries
URL:            https://github.com/GSharpKit/GdlSharp/releases
Source0:        GdlSharp-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  darwinx-filesystem-base >= 18
BuildRequires:  darwinx-mono-core
BuildRequires:  darwinx-libgdl >= %{version}

Requires:  	darwinx-filesystem >= 18
Requires:  	darwinx-libgdl >= %{version}
Requires:	darwinx-mono-core

%description
GTK+ is a multi-platform toolkit for creating graphical user
interfaces. Offering a complete set of widgets, GTK+ is suitable for
projects ranging from small one-off tools to complete application
suites.

%prep
%setup -q -n GdlSharp-%{version}

%build
mkdir -p m4
autoreconf  -i --force --warnings=none -I . -I m4
%{_darwinx_configure}

sed -i '' "s!libgdl-3.so.5!libgdl-3.5.dylib!" out/gdl-sharp.dll.config

%{_darwinx_make} %{?_smp_mflags} V=1


%install
%{_darwinx_make} install DESTDIR=$RPM_BUILD_ROOT

%files -n darwinx-GdlSharp
%{_darwinx_libdir}/mono
%{_darwinx_datadir}/pkgconfig/gdl-sharp-3.pc

%changelog
* Tue Nov 04 2014 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 3.12.0-1
- Initial RPM release