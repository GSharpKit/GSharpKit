Name:           darwinx-gettext
Version:        0.22.4
Release:        1%{?dist}
Summary:        Darwin Gettext library

License:        LGPLv2+
Group:          Development/Libraries
URL:            http://www.gnu.org/software/gettext/
Source0:        http://ftp.gnu.org/pub/gnu/gettext/gettext-%{version}.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	darwinx-libiconv

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

%prep
%setup -q -n gettext-%{version}

%build
%{_darwinx_configure} \
	--disable-dependency-tracking \
	--disable-static \
	--without-git \
	--disable-java \
	--disable-c++ \
	--disable-libasprintf \
	--with-included-libxml

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

rm -rf $RPM_BUILD_ROOT%{_darwinx_libdir}/GNU.Gettext.dll
rm -rf $RPM_BUILD_ROOT%{_darwinx_datadir}/doc
rm -rf $RPM_BUILD_ROOT%{_darwinx_datadir}/info
rm -rf $RPM_BUILD_ROOT%{_darwinx_datadir}/man

%find_lang gettext --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f gettext.lang
%defattr(-,root,wheel,-)
%{_darwinx_bindir}
%{_darwinx_libdir}/*.dylib
%{_darwinx_libdir}/gettext/
%{_darwinx_datadir}/gettext/
%{_darwinx_datadir}/gettext-%{version}/
%{_darwinx_datadir}/aclocal/
%{_darwinx_datadir}/locale/locale.alias
%{_darwinx_includedir}

%changelog
* Wed Jul 20 2016 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 0.19.7-1
- Updated to 0.19.7
* Fri Jan 24 2014 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 0.19.4-1
- Initial RPM release
