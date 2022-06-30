Name:           darwinx-gettext
Version:        0.21
Release:        1%{?dist}
Summary:        Darwin Gettext library

License:        LGPLv2+
Group:          Development/Libraries
URL:            http://www.gnu.org/software/gettext/
Source0:        http://ftp.gnu.org/pub/gnu/gettext/gettext-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

%description
The GNU gettext package provides a set of tools and documentation for
producing multi-lingual messages in programs. Tools include a set of
conventions about how programs should be written to support message
catalogs, a directory and file naming organization for the message
catalogs, a runtime library which supports the retrieval of translated
messages, and stand-alone programs for handling the translatable and
the already translated strings. Gettext provides an easy to use
library and tools for creating, using, and modifying natural language
catalogs and is a powerful and simple method for internationalizing
programs.

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
%{_darwinx_libdir}/libtextstyle.a

%changelog
* Wed Jul 20 2016 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 0.19.7-1
- Updated to 0.19.7
* Fri Jan 24 2014 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 0.19.4-1
- Initial RPM release
