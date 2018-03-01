%define debug_package %{nil}

%define platform net45
%define libdir /lib

Name:		OAuth2
Version: 	2.1.0
Release: 	1%{?dist}
Summary: 	Allows you to perform user authentication via Facebook, Foursquare, GitHub, Google etc
Group: 		System Environment/Libraries
License: 	MIT License
URL:		https://www.nuget.org/packages/OAuth2/
Source0:	OAuth2-master.zip
Source1:	oauth2.snk
BuildArch:      noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Prefix:		/usr

BuildRequires:	nuget
Requires:	mono-core
Requires:	Newtonsoft.Json >= 7.0.1
Requires:	RestSharp >= 105.2.3

%description
Allows you to perform user authentication via DigitalOcean, Facebook, Foursquare, 
GitHub, Google, Instagram, LinkedIn, MailRu, Odnoklassniki, Salesforce, Twitter, 
VK (Vkontakte), Windows Live, Yandex just in two method calls.

%prep
%setup -n %{name}-master 

#sed -i -e 's!<DefineConstants>FRAMEWORK;NETSTANDARD2_0;</DefineConstants>!<DefineConstants>FRAMEWORK;NETSTANDARD2_0;</DefineConstants><SignAssembly>true</SignAssembly><AssemblyOriginatorKeyFile>oauth2.snk</AssemblyOriginatorKeyFile>!g' OAuth2/OAuth2.csproj

cat > %{name}.pc << \EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{libdir}/mono/%{name}

Name: %{name}
Description: %{summary}
Requires: 
Version: %{version}
Libs: -r:${libdir}/OAuth2.dll
Cflags:
EOF

%build
nuget restore
cd OAuth2
cp %{SOURCE1} .
dotnet build -c Release

%install  
rm -rf $RPM_BUILD_ROOT

install -d -m 755 $RPM_BUILD_ROOT%{_prefix}%{libdir}/mono/gac
#sn -R OAuth2/bin/Release/netstandard2.0/%{name}.dll OAuth2/oauth2.snk
gacutil -i OAuth2/bin/Release/netstandard2.0/%{name}.dll -package %{name} -root $RPM_BUILD_ROOT%{_prefix}%{libdir} -gacdir mono/gac

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/pkgconfig
install -m 644 %{name}.pc $RPM_BUILD_ROOT%{_datadir}/pkgconfig/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root, -)
%{_prefix}%{libdir}/mono/gac
%{_prefix}%{libdir}/mono/%{name}/%{name}.dll
%{_datadir}/pkgconfig/%{name}.pc

%changelog
* Fri Nov 24 2017 Mikkel Kruse Johnsen <mikkel@xmedicus.com>
- first draft of spec file

