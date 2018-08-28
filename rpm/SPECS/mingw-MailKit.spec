%?mingw_package_header

%global __strip /bin/true

%global mingw_pkg_name MailKit
%global mingw_build_win32 1
%global mingw_build_win64 1

%define debug_package %{nil}

%define libdir /lib

Name:           mingw-MailKit
Version:        2.0.6
Release:        1%{?dist}
Summary:        MailKit is an Open Source cross-platform .NET mail-client library.

Group:          Development/Languages
License:        MIT
URL:            https://github.com/jstedfast/MailKit

Prefix:		/usr
BuildArch:	noarch

BuildRequires:  mono-devel
BuildRequires:  nuget


%description
* SASL Authentication via SCRAM-SHA-256, SCRAM-SHA-1, NTLM, DIGEST-MD5, CRAM-MD5, LOGIN, PLAIN, and XOAUTH2.
* A fully-cancellable SmtpClient with support for STARTTLS, 8BITMIME, BINARYMIME, ENHANCEDSTATUSCODES, SIZE, DSN, PIPELINING and SMTPUTF8.
* A fully-cancellable Pop3Client with support for STLS, UIDL, APOP, PIPELINING, UTF8, and LANG.
* A fully-cancellable ImapClient with support for ACL, QUOTA, LITERAL+, IDLE, NAMESPACE, ID, CHILDREN, LOGINDISABLED, STARTTLS, MULTIAPPEND, UNSELECT, UIDPLUS, CONDSTORE, ESEARCH, SASL-IR, COMPRESS, WITHIN, ENABLE, QRESYNC, SORT, THREAD, ESORT, METADATA, FILTERS, LIST-STATUS, SORT=DISPLAY, SPECIAL-USE, CREATE-SPECIAL-USE, MOVE, SEARCH=FUZZY, UTF8=ACCEPT, UTF8=ONLY, LITERAL-, APPENDLIMIT, XLIST, and X-GM-EXT1.
* Client-side sorting and threading of messages (the Ordinal Subject and the Jamie Zawinski threading algorithms are supported).
* Asynchronous versions of all methods that hit the network.
* S/MIME, OpenPGP and DKIM signature support via MimeKit.
* Microsoft TNEF support via MimeKit.


# Mingw32
%package -n mingw32-%{mingw_pkg_name}
Summary:       %{summary}
Requires:       mingw32-mono
Requires:       mingw32-BouncyCastle
Requires:       mingw32-MimeKit

%description -n mingw32-%{mingw_pkg_name}
* SASL Authentication via SCRAM-SHA-256, SCRAM-SHA-1, NTLM, DIGEST-MD5, CRAM-MD5, LOGIN, PLAIN, and XOAUTH2.
* A fully-cancellable SmtpClient with support for STARTTLS, 8BITMIME, BINARYMIME, ENHANCEDSTATUSCODES, SIZE, DSN, PIPELINING and SMTPUTF8.
* A fully-cancellable Pop3Client with support for STLS, UIDL, APOP, PIPELINING, UTF8, and LANG.
* A fully-cancellable ImapClient with support for ACL, QUOTA, LITERAL+, IDLE, NAMESPACE, ID, CHILDREN, LOGINDISABLED, STARTTLS, MULTIAPPEND, UNSELECT, UIDPLUS, CONDSTORE, ESEARCH, SASL-IR, COMPRESS, WITHIN, ENABLE, QRESYNC, SORT, THREAD, ESORT, METADATA, FILTERS, LIST-STATUS, SORT=DISPLAY, SPECIAL-USE, CREATE-SPECIAL-USE, MOVE, SEARCH=FUZZY, UTF8=ACCEPT, UTF8=ONLY, LITERAL-, APPENDLIMIT, XLIST, and X-GM-EXT1.
* Client-side sorting and threading of messages (the Ordinal Subject and the Jamie Zawinski threading algorithms are supported).
* Asynchronous versions of all methods that hit the network.
* S/MIME, OpenPGP and DKIM signature support via MimeKit.
* Microsoft TNEF support via MimeKit.

# Mingw64
%package -n mingw64-%{mingw_pkg_name}
Summary:       %{summary}
Requires:       mingw64-mono
Requires:       mingw64-BouncyCastle
Requires:       mingw64-MimeKit

%description -n mingw64-%{mingw_pkg_name}
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
nuget install %{mingw_pkg_name} -Version %{version}

cat > MailKit32.pc << \EOF
prefix=%{mingw32_prefix}
exec_prefix=${prefix}
libdir=%{mingw32_prefix}%{libdir}/mono

Name: MailKit
Description: %{name} - %{summary}
Requires: MimeKit
Version: %{version}
Libs: -r:Facades/netstandard.dll -r:${libdir}/MailKit/MailKit.dll
Cflags:
EOF

cat > MailKit64.pc << \EOF
prefix=%{mingw64_prefix}
exec_prefix=${prefix}
libdir=%{mingw64_prefix}%{libdir}/mono

Name: MailKit
Description: %{name} - %{summary}
Requires: MimeKit
Version: %{version}
Libs: -r:Facades/netstandard.dll -r:${libdir}/MailKit/MailKit.dll
Cflags:
EOF


%build

%install
%{__rm} -rf %{buildroot}

# Mingw32
install -d -m 755 $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}/mono/gac
gacutil -i MailKit.%{version}/lib/netstandard2.0/MailKit.dll -package %{mingw_pkg_name} -root $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir} -gacdir mono/gac

install -d -m 755 $RPM_BUILD_ROOT%{mingw32_datadir}/pkgconfig/
install -m 644 MailKit32.pc $RPM_BUILD_ROOT%{mingw32_datadir}/pkgconfig/MailKit.pc

# Mingw64
install -d -m 755 $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}/mono/gac
gacutil -i MailKit.%{version}/lib/netstandard2.0/MailKit.dll -package %{mingw_pkg_name} -root $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir} -gacdir mono/gac

install -d -m 755 $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/
install -m 644 MailKit64.pc $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/MailKit.pc


%clean
#%{__rm} -rf %{buildroot}

%files -n mingw32-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw32_prefix}%{libdir}/mono/gac
%{mingw32_prefix}%{libdir}/mono/MailKit/MailKit.dll
%{mingw32_datadir}/pkgconfig/MailKit.pc

%files -n mingw64-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw64_prefix}%{libdir}/mono/gac
%{mingw64_prefix}%{libdir}/mono/MailKit/MailKit.dll
%{mingw64_datadir}/pkgconfig/MailKit.pc


%changelog
* Fri Aug 17 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 2.0.6-1
- Update to 2.0.6

* Fri Aug 03 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 2.0.5-1
- Update to 2.0.5

* Thu Sep 7 2017 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 1.18.0-1
- Initial version
