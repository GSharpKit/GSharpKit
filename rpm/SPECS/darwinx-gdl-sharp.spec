Name:           darwinx-gdl-sharp
Version:        3.14.0
Release:        1%{?dist}
Summary:        Max OS X GDL library

License:        LGPLv2+
Group:          Development/Libraries
URL:            https://github.com/openmedicus/gdl-sharp
Source0:        gdl-sharp-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  darwinx-filesystem >= 15
BuildRequires:  darwinx-mono
BuildRequires:  darwinx-gdl >= %{version}

%description
GTK+ is a multi-platform toolkit for creating graphical user
interfaces. Offering a complete set of widgets, GTK+ is suitable for
projects ranging from small one-off tools to complete application
suites.

%prep
%setup -q -n gdl-sharp-%{version}

%build
%{_darwinx_configure}

sed -i '' "s!libgdl-3.so.5!libgdl-3.5.dylib!" out/gdl-sharp.dll.config

%{_darwinx_make} %{?_smp_mflags} V=1


%install
%{_darwinx_make} install DESTDIR=$RPM_BUILD_ROOT

%files -n darwinx-gdl-sharp
%{_darwinx_libdir}/mono
%{_darwinx_libdir}/pkgconfig/gdl-sharp-3.pc

%changelog
* Tue Nov 04 2014 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 3.12.0-1
- Initial RPM release
