%define api 1.0

Name:           dleyna-core
Version:        0.5.0
Release:        1%{?dist}
Summary:        Utilities for higher level dLeyna libraries

License:        LGPLv2
URL:            https://01.org/dleyna/
Source0:        https://01.org/dleyna/sites/default/files/downloads/%{name}-%{version}.tar.gz

# https://github.com/01org/dleyna-core/pull/48
Patch0:         0001-Don-t-schedule-dleyna_task_processor_t-on_quit_cb-mo.patch
# https://github.com/01org/dleyna-core/pull/49
Patch1:         0002-Remove-all-queues-before-dleyna_task_processor_t-on_.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gupnp-1.0)

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
%patch0 -p1
%patch1 -p1


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
* Fri Mar 03 2017 Debarshi Ray <rishi@fedoraproject.org> - 0.5.0-1
- Update to 0.5.0
Resolves: #1386846

* Wed May 27 2015 Debarshi Ray <rishi@fedoraproject.org> - 0.4.0-1
- Initial RHEL import
Resolves: #1221264
