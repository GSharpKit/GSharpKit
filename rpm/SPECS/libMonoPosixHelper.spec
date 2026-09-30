%define debug_package %{nil}

Name:           libMonoPosixHelper
Version:        1.0.0
Release:        1%{?dist}
Summary:        MonoPosixHelpoer from the official mono

License:        LGPLv2+
Group:          Development/Libraries
URL:            http://github.com/mono
#Source0:        Mono.Posix-%{version}.tar.xz
#Source1:	glibc-2.39.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  zlib
#BuildRequires:  iconv

%description
MonoPosixHelpoer from the official mono

%prep
#setup -q -n Mono.Posix-%{version} 
%setup -c %{name} -T
#tar xfJ %{SOURCE1}

%build
#pushd glibc-2.39
#mkdir build
#pushd build
#../configure --prefix=/usr --disable-werror 
#make
#popd
#popd

#export LDFLAGS="$LDFLAGS -L"
#./configure --prefix=/usr --libdir=/usr/lib64

#pushd mono/eglib
#make
#popd
#pushd support
#make
#popd

dotnet new console
dotnet add package Mono.Posix.NETStandard --version 5.20.1-preview

dotnet publish --force --runtime linux-x64 -o lin
 
%install
rm -rf $RPM_BUILD_ROOT
#pushd support
#DESTDIR=$RPM_BUILD_ROOT make install
#popd

#rm -f $RPM_BUILD_ROOT%{_libdir}/libMonoPosixHelper.a
#rm -f $RPM_BUILD_ROOT%{_libdir}/libMonoPosixHelper.la
#rm -f $RPM_BUILD_ROOT%{_libdir}/libMonoSupportW.a
#rm -f $RPM_BUILD_ROOT%{_libdir}/libMonoSupportW.so

install -d -m 755 $RPM_BUILD_ROOT/usr/lib64
install -m 644 lin/libMonoPosixHelper.so $RPM_BUILD_ROOT/usr/lib64


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,wheel)
%{_libdir}/libMonoPosixHelper.so

%changelog
* Thu Feb 27 2014 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 2.9.2-1
- Initial RPM release
