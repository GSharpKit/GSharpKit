Name:           GdlSharp
Version:        3.26.0
Release:        3%{?dist}
Summary:        GDL library

License:        LGPLv2+
Group:          Development/Libraries
URL:            https://github.com/openmedicus/gdl-sharp
Source0:        GdlSharp-%{version}.tar.gz

BuildArch:      noarch

Requires:	libgdl >= %{version}

BuildRequires:  mono-core
BuildRequires:  libgdl-devel >= %{version}

Obsoletes:	gdl-sharp
Provides:	gdl-sharp

%description
GTK+ is a multi-platform toolkit for creating graphical user
interfaces. Offering a complete set of widgets, GTK+ is suitable for
projects ranging from small one-off tools to complete application
suites.

%prep
%setup -q

%build
sh autogen.sh --prefix=/usr
make clean
make %{?_smp_mflags} V=1

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%{_prefix}/lib/mono
%{_datadir}/pkgconfig/gdl-sharp-3.pc

%changelog
* Fri Nov 17 2017 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 3.26.0-1
- Renamed to GdlSharp
- Updated to 3.26.0

* Tue Nov 10 2015 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 3.18.0-1
- Updated to 3.18.0

* Tue Jan 20 2015 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 3.14.0-1
- Updated to 3.14.0

* Tue Nov 04 2014 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 3.12.0-1
- Initial RPM release
