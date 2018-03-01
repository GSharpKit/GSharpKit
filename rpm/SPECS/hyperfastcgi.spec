Name:           hyperfastcgi
Url:            https://github.com/xplicit/HyperFastCgi
License:        MIT
Group:          Productivity/Networking/Web/Servers
Version:        0.4
Release:        4%{?dist}
Summary:        HyperFastCgi hosts mono web applications with nginx
Source0:        %{name}-%{version}.tar.xz
Source1:	hfc.config
Source2:	hyperfastcgi.service
Source3:	hyperfastcgi.initd
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      x86_64
Prefix:		/usr

BuildRequires:  mono-devel
Requires:	mono-core nginx
BuildRequires:  libevent-devel
Requires:       libevent

%description
HyperFastCgi hosts mono web applications with nginx. It's a primary replacement of mono-server-fastcgi for linux platform.
Key features:
    Does not leak memory
    Serves requests much faster. See performance comparison
    Open architecture allows developers to write their own extensions or replacements of HyperFastCgi components

%package devel
Group: 		Development/Libraries
Requires: 	%{name} = %{version}-%{release}
Summary: 	Development files for hyperfastcgi

%description devel
HyperFastCgi hosts mono web applications with nginx. It's a primary replacement of mono-server-fastcgi for linux platform.
Key features:
    Does not leak memory
    Serves requests much faster. See performance comparison
    Open architecture allows developers to write their own extensions or replacements of HyperFastCgi components


%prep
%setup -q

%build
sh autogen.sh --prefix=%{_prefix} --sysconfdir=%{_sysconfdir} --libdir=%{_prefix}/lib
make

%install
make DESTDIR=%{buildroot} pkglibdir=%{buildroot}%{_prefix}/lib/mono install

install -d -m 755 %{buildroot}%{_sysconfdir}/hyperfastcgi
install -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/hyperfastcgi/

install -d -m 755 %{buildroot}%{_prefix}/lib/systemd/system/
install -m 644 %{SOURCE2} %{buildroot}%{_prefix}/lib/systemd/system/

install -d -m 755 %{buildroot}/var/log/hyperfastcgi

#install -d -m 755 %{buildroot}%{_prefix}/lib64
#mv %{buildroot}%{_prefix}/lib/libhfc-* %{buildroot}%{_prefix}/lib64

install -d -m 755 %{buildroot}%{_prefix}/lib/hyperfastcgi/4.0
cp -r %{buildroot}%{_prefix}/lib/mono/gac/HyperFastCgi/*/*.exe* %{buildroot}%{_prefix}/lib/hyperfastcgi/4.0

rm -rf %{buildroot}/home

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE README.md
%config %{_sysconfdir}/hyperfastcgi/hfc.config
%config %{_prefix}/lib/systemd/system/hyperfastcgi.service
%{_bindir}/hyperfastcgi4
%{_prefix}/lib/mono/4.5
%{_prefix}/lib/mono/gac
%{_prefix}/lib/hyperfastcgi/4.0/HyperFastCgi.exe
%{_prefix}/lib/libhfc-native.so
%{_prefix}/lib/libhfc-native.so.1
%{_prefix}/lib/libhfc-native.so.1.0.0
%attr(0775,nginx,nginx)/var/log/hyperfastcgi

%files devel
%{_prefix}/lib/mono/4.0
%{_prefix}/lib/hyperfastcgi/4.0/HyperFastCgi.exe.mdb
%{_prefix}/lib/libhfc-native.la
%{_prefix}/lib/libhfc-native.a

%changelog
* Mon Jun 20 2016 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 0.4-1
- Initial RPM release

