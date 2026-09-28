Name:           libMonoPosixHelper
Version:        1.0.0
Release:        1%{?dist}
Summary:        MonoPosixHelpoer from the official mono

License:        LGPLv2+
Group:          Development/Libraries
URL:            http://github.com/mono
Source0:        Mono.Posix-%{version}.tar.xz
#Patch0:		Mono.Posix-iconv-ucrt.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  zlib
#BuildRequires:  iconv

%description
MonoPosixHelpoer from the official mono

%prep
%setup -q -n Mono.Posix-%{version}
#patch 0 -p1

%build
./configure --prefix=/usr --libdir=/usr/lib64

pushd mono/eglib
make
popd
pushd support
make
popd

%install
rm -rf $RPM_BUILD_ROOT
pushd support
DESTDIR=$RPM_BUILD_ROOT make install
popd

rm -f $RPM_BUILD_ROOT%{_libdir}/libMonoPosixHelper.a
rm -f $RPM_BUILD_ROOT%{_libdir}/libMonoPosixHelper.la
rm -f $RPM_BUILD_ROOT%{_libdir}/libMonoSupportW.a
rm -f $RPM_BUILD_ROOT%{_libdir}/libMonoSupportW.so


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,wheel)
%{_libdir}/libMonoPosixHelper.so

%changelog
* Thu Feb 27 2014 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 2.9.2-1
- Initial RPM release
