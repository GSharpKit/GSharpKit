Name:           darwinx-gettext
Version:        0.19.4
Release:        1%{?dist}
Summary:        Darwin Gettext library

License:        LGPLv2+
Group:          Development/Libraries
URL:            http://www.gnu.org/software/gettext/
Source0:        http://ftp.gnu.org/pub/gnu/gettext/gettext-%{version}.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

%description
Darwin Glib2 library

%package static
Summary:        Static version of the Darwin Gettext library
Requires:       %{name} = %{version}-%{release}
Group:          Development/Libraries

%description static
Static version of the Darwin Gettext library.

%prep
%setup -q -n gettext-%{version}

%build
%{_darwinx_configure}
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

rm -f $RPM_BUILD_ROOT/%{_darwinx_libdir}/GNU.Gettext.dll
rm -rf $RPM_BUILD_ROOT/%{_darwinx_datadir}/doc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_darwinx_bindir}
%{_darwinx_libdir}/*.la
%{_darwinx_libdir}/*.dylib
%{_darwinx_libdir}/gettext/
%{_darwinx_includedir}
%{_darwinx_datadir}

%files static
%defattr(-,root,root,-)
%{_darwinx_libdir}/libasprintf.a
%{_darwinx_libdir}/libgettextpo.a
%{_darwinx_libdir}/libintl.a


%changelog
* Fri Jan 24 2014 Mikkel Kruse Johnsen <mikkel@structura-it.dk> - 0.18.3.1-1
- Initial RPM release
