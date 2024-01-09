Summary:	Circular Intrusive Double Linked List Collection
Name:		c-list
Version:	3.1.0
Release:	1
License:	Apache 2.0 or LGPL v2.1+
Group:		Libraries
Source0:	https://github.com/c-util/c-list/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	363d7ef1c1f477625896d07d52940195
URL:		https://c-util.github.io/c-list/
BuildRequires:	meson >= 0.60.0
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The c-list project implements an intrusive collection based on
circular double linked lists in ISO-C11. It aims for minimal API
constraints, leaving maximum control over the data-structures to the
API consumer.

%package devel
Summary:	Circular Intrusive Double Linked List Collection
Group:		Development/Libraries

%description devel
The c-list project implements an intrusive collection based on
circular double linked lists in ISO-C11. It aims for minimal API
constraints, leaving maximum control over the data-structures to the
API consumer.

%prep
%setup -q

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_npkgconfigdir}

%ninja_install -C build

%{__mv} $RPM_BUILD_ROOT%{_pkgconfigdir}/*.pc $RPM_BUILD_ROOT%{_npkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc AUTHORS NEWS.md README.md
%{_includedir}/c-list.h
%{_npkgconfigdir}/libclist-3.pc
