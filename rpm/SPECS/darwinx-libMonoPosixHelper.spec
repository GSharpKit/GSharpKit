Name:           darwinx-libMonoPosixHelper
Version:        1.0.0
Release:        1%{?dist}
Summary:        MonoPosixHelpoer from the official mono

License:        LGPLv2+
Group:          Development/Libraries
URL:            http://github.com/mono
Source0:        Mono.Posix-%{version}.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  darwinx-filesystem-base >= 18
BuildRequires:  darwinx-gcc
BuildRequires:  darwinx-gettext
BuildRequires:  darwinx-zlib
BuildRequires:  darwinx-libiconv

Requires:       darwinx-filesystem >= 18

%description
MonoPosixHelpoer from the official mono

%prep
%setup -q -n Mono.Posix-%{version}

%build
%{_darwinx_configure}

pushd mono/eglib
make
popd
pushd support
make
popd

%install
rm -rf $RPM_BUILD_ROOT
pushd support
make DESTDIR=$RPM_BUILD_ROOT install
popd

rm -f $RPM_BUILD_ROOT%{_darwinx_libdir}/libMonoPosixHelper.a
rm -f $RPM_BUILD_ROOT%{_darwinx_libdir}/libMonoPosixHelper.la
rm -f $RPM_BUILD_ROOT%{_darwinx_libdir}/libMonoSupportW.a
rm -f $RPM_BUILD_ROOT%{_darwinx_libdir}/libMonoSupportW.dylib

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,wheel)
%{_darwinx_libdir}/libMonoPosixHelper.dylib

%changelog
* Thu Feb 27 2014 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 2.9.2-1
- Initial RPM release
