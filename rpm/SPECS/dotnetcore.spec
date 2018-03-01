# Some BUILD ID's are missing, which prevents us from building a debug package. This fixes that.
# Reference: https://github.com/tpokorra/lbs-mono-fedora/issues/3#issuecomment-219857688
%undefine _missing_build_ids_terminate_build

Name:		dotnetcore
Summary:	.NET Core CLI tools and run-time
Version:	1.1.0
Release:	7%{?dist}
URL:		https://github.com/dotnet/

License:	MIT and ASL 2.0

ExclusiveArch:	x86_64

Requires:	bash
Requires:	libcurl
Requires:	libunwind
Requires:	libuv

BuildRequires:	automake
BuildRequires:	clang
BuildRequires:	cmake
BuildRequires:	krb5-devel
BuildRequires:	libcurl-devel
BuildRequires:	libicu-devel
BuildRequires:	libtool
BuildRequires:	libunwind-devel
BuildRequires:	libuuid-devel
BuildRequires:	lldb-devel
BuildRequires:	llvm
BuildRequires:	lttng-ust-devel
BuildRequires:	python
BuildRequires:	zlib-devel

%if %{fedora} >= 26
BuildRequires:	compat-openssl10-devel
%else
BuildRequires:	openssl-devel
%endif

# Trustworthy SRPM from RHEL which contains the payload
# Current version: https://access.redhat.com/errata/RHEA-2016:2827
Source0: 	dotnetcore.tar.gz
%global		rhel_srpm 		rh-dotnetcore11-dotnetcore-1.1-3.el7.src.rpm
%global		payload_tarball 	dotnet-dev-rhel-x64.1.0.0-preview2-1-003175.tar.gz
%global		srpm_sha256 		514a5b36e777172965aed9c3575abaf26f61feec22bf771075abde9878b75436

# Use the upstream license file.
# https://github.com/dotnet/core-setup/issues/676
Source1: 	https://raw.githubusercontent.com/dotnet/core-setup/release/%{version}/LICENSE

%global 	bootstrap_commit 	c5b6d002c1b3c9466041c3491ea04c83b7349cf8
%global 	coreclr_commit 		1735a1d453677717e68803da6a85284d15dca891
%global 	corefx_commit 		e02adc60844d53991bfba296b738d2e007f470f7
%global 	core_setup_commit 	928f77c4bc3f49d892459992fb6e1d5542cb5e86

Source2: 	%{url}core/archive/%{bootstrap_commit}.tar.gz#/%{name}-%{version}-bootstrap.tar.gz
Source3:	%{url}coreclr/archive/%{coreclr_commit}.tar.gz#/%{name}-%{version}-coreclr.tar.gz
Source4:	%{url}corefx/archive/%{corefx_commit}.tar.gz#/%{name}-%{version}-corefx.tar.gz
Source5:	%{url}core-setup/archive/%{core_setup_commit}.tar.gz#/%{name}-%{version}-core-setup.tar.gz

# https://github.com/dotnet/core/blob/bootstrap/tools/dotnet-bootstrap/dotnet.bootstrap.py#L363
%global		libuv_version 		1.9.0
%global		libuv_commit 		229b3a4cc150aebd6561e6bd43076eafa7a03756
Source6:	https://github.com/libuv/libuv/archive/%{libuv_commit}.tar.gz#/%{name}-%{version}-libuv.tar.gz

# This patch fixes wrong corefx path in the rover tool
# Not in the upstream yet
Patch0: dotnetcore-1.1-rover.patch
# This patch is for adding Fedora 25 and Fedora 26 to Microsoft.NETCore.App supported runtimes in the payload
# Upstream: Not in the upstream yet
Patch1: dotnetcore-1.1-RIL-payload.patch
# This patch is for including debug info into shared object files. That info is then stripped into a separate package.
# Upstream: Not in the upstream yet
Patch2: dotnetcore-1.1-debuginfo-fix.patch
# This patch is for adding Fedora 25 and Fedora 26 to corefx platform runtimes.json
# Upstream: Not in the upstream yet
Patch3: dotnetcore-1.1-RIL-fix.patch
# https://github.com/dotnet/coreclr/pull/8470
Patch4: dotnetcore-1.1-lttng-ust-header.patch
# https://github.com/dotnet/coreclr/pull/8311
Patch5: dotnetcore-1.1-clang3.9.patch
# https://github.com/dotnet/coreclr/pull/7865
Patch6: dotnetcore-1.1-ex.patch

%description
.NET Core is a fast, lightweight and modular platform for creating
cross platform applications that work on Linux, Mac and Windows.

.NET Core contains a run-time conforming to the .NET standards, a set
of framework libraries, an SDK containing compilers and a 'dotnet'
application to drive everything.

%prep
%setup

# Unpack rover script and patch it
tar xf %SOURCE2 && mv core-%{bootstrap_commit} core-bootstrap
cd core-bootstrap/tools/dotnet-bootstrap
%patch0

# SRPM check against the known checksum / unpack it for patching
echo "%{srpm_sha256}  %{_builddir}/%{name}-%{version}/%{rhel_srpm}" | sha256sum -c
rpm2cpio %{_builddir}/%{name}-%{version}/%{rhel_srpm} | cpio -idm

# Patch the payload (Microsoft.NETCore.App supported runtimes are carried over...) and repack it
tar xf %{payload_tarball} && rm %{payload_tarball} 
%patch1
tar czf %{payload_tarball} LICENSE.txt ThirdPartyNotices.txt dotnet host sdk shared

# Setup the Fedora 25/26 target for dotnet.bootstrap.py
mkdir -p fedora.%{fedora}-x64-dotnet/src && cd fedora.%{fedora}-x64-dotnet/src

tar xf %SOURCE3 && mv coreclr-%{coreclr_commit} coreclr
tar xf %SOURCE4 && mv corefx-%{corefx_commit} corefx
tar xf %SOURCE5 && mv core-setup-%{core_setup_commit} core-setup
tar xf %SOURCE6 && mv libuv-%{libuv_commit} libuv

%patch2
%patch3
%patch4
%patch5
%patch6

%build
# export CFLAGS=${RPM_OPT_FLAGS} - Fedora/RH enforced compiler flags (build fails with them...)
cd core-bootstrap/tools/dotnet-bootstrap/
./dotnet.bootstrap.py -payload %{payload_tarball}

%install
install -d -m 0755 %{buildroot}%{_libdir}/%{name}/
cp -arf core-bootstrap/tools/dotnet-bootstrap/fedora.%{fedora}-x64-dotnet/bin/* %{buildroot}%{_libdir}/%{name}/
install -m 0644 %SOURCE1 %{buildroot}%{_libdir}/%{name}/

install -d -m 0755 %{buildroot}%{_bindir}
ln -s %{_libdir}/%{name}/dotnet %{buildroot}/%{_bindir}/

%files
%{_libdir}/%{name}
%{_bindir}/dotnet
%license %{_libdir}/%{name}/LICENSE
%license %{_libdir}/%{name}/ThirdPartyNotices.txt

%changelog
* Thu Mar 16 2017 Nemanja Milošević <nmilosevnm@gmail.com> - 1.1.0-7
- rebuilt with latest libldb
* Wed Feb 22 2017 Nemanja Milosevic <nmilosev@fedoraproject.org> - 1.1.0-6
- compat-openssl 1.0 for F26 for now
* Sun Feb 19 2017 Nemanja Milosevic <nmilosev@fedoraproject.org> - 1.1.0-5
- Fix wrong commit id's
* Sat Feb 18 2017 Nemanja Milosevic <nmilosev@fedoraproject.org> - 1.1.0-4
- Use commit id's instead of branch names
* Sat Feb 18 2017 Nemanja Milosevic <nmilosev@fedoraproject.org> - 1.1.0-3
- Improper patch5 fix
* Sat Feb 18 2017 Nemanja Milosevic <nmilosev@fedoraproject.org> - 1.1.0-2
- SPEC cleanup
- git removal (using all tarballs for reproducible builds)
- more reasonable versioning
* Thu Feb 09 2017 Nemanja Milosevic <nmilosev@fedoraproject.org> - 1.1.0-1
- Fixed debuginfo going to separate package (Patch1)
- Added F25/F26 RIL and fixed the version info (Patch2)
- Added F25/F26 RIL in Microsoft.NETCore.App suported runtime graph (Patch3)
- SPEC file cleanup
* Wed Jan 11 2017 Nemanja Milosevic <nmilosev@fedoraproject.org> - 1.1.0-0
- Initial RPM for Fedora 25/26.

