%{?ucrt_package_header}

%global debug_package %{nil}

Name:           ucrt-libMonoPosixHelper
Version:        1.0.0
Release:        1%{?dist}
Summary:        MonoPosixHelpoer from the official mono

License:        LGPLv2+
Group:          Development/Libraries
URL:            http://github.com/mono
Source0:        Mono.Posix-%{version}.tar.xz
Patch0:		Mono.Posix-iconv-ucrt.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  ucrt64-filesystem
BuildRequires:  ucrt64-gcc
BuildRequires:  ucrt64-gettext
BuildRequires:  ucrt64-zlib
BuildRequires:  ucrt64-win-iconv

Requires:       ucrt64-filesystem >= 18

%description
MonoPosixHelpoer from the official mono

%package -n ucrt64-libMonoPosixHelper
Summary:        MinGW Windows libepoxy library

%description -n ucrt64-libMonoPosixHelper
MonoPosixHelpoer from the official mono

%prep
%setup -q -n Mono.Posix-%{version}
%patch 0 -p1

%build
%{ucrt64_configure}

pushd mono/eglib
%{ucrt64_make}
popd
pushd mono/zlib
%{ucrt64_make}
popd
pushd support
%{ucrt64_make}
popd

%install
rm -rf $RPM_BUILD_ROOT
pushd support
DESTDIR=$RPM_BUILD_ROOT %{ucrt64_make} install
popd

mv $RPM_BUILD_ROOT%{ucrt64_bindir}/libMonoPosixHelper.dll $RPM_BUILD_ROOT%{ucrt64_bindir}/MonoPosixHelper.dll

rm -f $RPM_BUILD_ROOT%{ucrt64_libdir}/libMonoPosixHelper.a
rm -f $RPM_BUILD_ROOT%{ucrt64_libdir}/libMonoPosixHelper.la
rm -rf $RPM_BUILD_ROOT%{ucrt64_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files -n ucrt64-libMonoPosixHelper
%defattr(-,root,wheel)
%{ucrt64_bindir}/MonoPosixHelper.dll

%changelog
* Thu Feb 27 2014 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 2.9.2-1
- Initial RPM release
