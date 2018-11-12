%global debug_package %{nil}

%define libdir /lib

Name:           MailKit
Version:        2.0.7
Release:        1%{?dist}
Summary:        MailKit is an Open Source cross-platform .NET mail-client library.

Group:          Development/Languages
License:        MIT
URL:            https://github.com/jstedfast/MailKit
Prefix:		/usr

BuildArch:	noarch

BuildRequires:  nuget

Requires:	mono-core >= 5.14.0
Requires:	BouncyCastle >= 1.8.2
Requires:	MimeKit >= %{version}

%description
MailKit is an Open Source cross-platform .NET mail-client library that is based on MimeKit and optimized for mobile devices.

Features include:
* SASL Authentication via SCRAM-SHA-256, SCRAM-SHA-1, NTLM, DIGEST-MD5, CRAM-MD5, LOGIN, PLAIN, and XOAUTH2.
* A fully-cancellable SmtpClient with support for STARTTLS, 8BITMIME, BINARYMIME, ENHANCEDSTATUSCODES, SIZE, DSN, PIPELINING and SMTPUTF8.
* A fully-cancellable Pop3Client with support for STLS, UIDL, APOP, PIPELINING, UTF8, and LANG.
* A fully-cancellable ImapClient with support for ACL, QUOTA, LITERAL+, IDLE, NAMESPACE, ID, CHILDREN, LOGINDISABLED, STARTTLS, MULTIAPPEND, UNSELECT, UIDPLUS, CONDSTORE, ESEARCH, SASL-IR, COMPRESS, WITHIN, ENABLE, QRESYNC, SORT, THREAD, ESORT, METADATA, FILTERS, LIST-STATUS, SORT=DISPLAY, SPECIAL-USE, CREATE-SPECIAL-USE, MOVE, SEARCH=FUZZY, UTF8=ACCEPT, UTF8=ONLY, LITERAL-, APPENDLIMIT, XLIST, and X-GM-EXT1.
* Client-side sorting and threading of messages (the Ordinal Subject and the Jamie Zawinski threading algorithms are supported).
* Asynchronous versions of all methods that hit the network.
* S/MIME, OpenPGP and DKIM signature support via MimeKit.
* Microsoft TNEF support via MimeKit.

%prep
%setup -c %{name}-%{version} -T
nuget install %{name} -Version %{version}

cat > %{name}.pc << \EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{_prefix}%{libdir}/mono

Name: %{name}
Description: %{name} - %{summary}
Requires: MimeKit
Version: %{version}
Libs: -r:${libdir}/%{name}/MailKit.dll
Cflags:
EOF

%build

%install
%{__rm} -rf %{buildroot}

install -d -m 755 $RPM_BUILD_ROOT%{_prefix}%{libdir}/mono/gac
gacutil -i MailKit.%{version}/lib/netstandard2.0/MailKit.dll -package %{name} -root $RPM_BUILD_ROOT%{_prefix}%{libdir} -gacdir mono/gac

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/pkgconfig/
install -m 644 %{name}.pc $RPM_BUILD_ROOT%{_datadir}/pkgconfig/

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_prefix}%{libdir}/mono/gac
%{_prefix}%{libdir}/mono/%{name}/MailKit.dll
%{_datadir}/pkgconfig/%{name}.pc

%changelog
* Fri Aug 17 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 2.0.6-1
- Update to 2.0.6
* Thu Aug 02 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 2.0.5-1
- Update to 2.0.5
* Mon Aug 18 2017 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 1.18.0-1
- Initial version
