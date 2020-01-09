%define api 1.0

Name:           dleyna-core
Version:        0.4.0
Release:        1%{?dist}
Summary:        Utilities for higher level dLeyna libraries

License:        LGPLv2
URL:            https://01.org/dleyna/
Source0:        https://01.org/dleyna/sites/default/files/downloads/%{name}-%{version}.tar.gz

BuildRequires:  glib2-devel >= 2.28
BuildRequires:  gupnp-devel >= 0.19.1
BuildRequires:  pkgconfig autoconf automake libtool

%description
A set of utility functions that are used by the higher level dLeyna libraries
to communicate with DLNA devices. It provides APIs for logging, error, settings
and task management, and an IPC abstraction.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
autoreconf -f -i
%configure \
  --disable-silent-rules \
  --disable-static

make %{?_smp_mflags}


%install
make install INSTALL="%{__install} -p" DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -delete

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc AUTHORS
%doc COPYING
%doc ChangeLog
%doc README
%{_libdir}/libdleyna-core-%{api}.so.*

%files devel
%{_libdir}/libdleyna-core-%{api}.so
%{_libdir}/pkgconfig/%{name}-%{api}.pc

%dir %{_includedir}/dleyna-%{api}
%dir %{_includedir}/dleyna-%{api}/libdleyna
%{_includedir}/dleyna-%{api}/libdleyna/core


%changelog
* Wed May 27 2015 Debarshi Ray <rishi@fedoraproject.org> - 0.4.0-1
- Initial RHEL import
Resolves: #1221264
