%global tarball xf86-input-mouse
%global moduledir %(pkg-config xorg-server --variable=moduledir )
%global driverdir %{moduledir}/input

Summary:   Xorg X11 mouse input driver
Name:      xorg-x11-drv-mouse
Version:   1.5.0
Release:   4%{?dist}
URL:       http://www.x.org
License:   MIT
Group:     User Interface/X Hardware Support
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:   ftp://ftp.x.org/pub/individual/driver/%{tarball}-%{version}.tar.bz2

Patch1:    mouse-1.5.0-memleak.patch

ExcludeArch: s390 s390x

BuildRequires: autoconf automake libtool
BuildRequires: xorg-x11-server-sdk >= 1.5.99.1
BuildRequires: xorg-x11-util-macros >= 1.3.0

Requires: xorg-x11-server-Xorg >= 1.5.99.1

%description 
X.Org X11 mouse input driver.

%prep
%setup -q -n %{tarball}-%{version}

%patch1 -p1

%build
autoreconf -v --install || exit 1
%configure --disable-static
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

# FIXME: Remove all libtool archives (*.la) from modules directory.  This
# should be fixed in upstream Makefile.am or whatever.
find $RPM_BUILD_ROOT -regex ".*\.la$" | xargs rm -f --

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{driverdir}/mouse_drv.so
%{_mandir}/man4/mousedrv.4*

%changelog
* Mon Feb 08 2010 Peter Hutterer <peter.hutterer@redhat.com> 1.5.0-4
- mouse-1.5.0-memleak.patch: fix memory leak on shutdown.

* Wed Jan 06 2010 Peter Hutterer <peter.hutterer@redhat.com> 1.5.0-3
- Use global instead of define as per Packaging Guidelines
- Remove traces of git build.

* Fri Nov 20 2009 Peter Hutterer <peter.hutterer@redhat.com> 1.5.0-2
- BuildRequires xorg-x11-util-macros 1.3.0

* Fri Nov 20 2009 Peter Hutterer <peter.hutterer@redhat.com> 1.5.0-1
- mouse 1.5.0

* Thu Sep 10 2009 Peter Hutterer <peter.hutterer@redhat.com> 1.4.99.1-2
- Fix spec file, Release was busted.

* Wed Sep 09 2009 Peter Hutterer <peter.hutterer@redhat.com> 1.4.99.1-1
- mouse 1.4.99.1

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.99-3.20090619.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Adam Jackson <ajax@redhat.com> - 1.4.99-2.20090619.1
- ABI bump

* Fri Jun 19 2009 Peter Hutterer <peter.hutterer@redhat.com> - 1.4.99-2.20090619
- rebuild for server ABI 7

* Fri Jun 19 2009 Peter Hutterer <peter.hutterer@redhat.com> - 1.4.99-1.20090619
- Update to today's git master.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jan 12 2009 Peter Hutterer <peter.hutterer@redhat.com> 1.4.0-1
- mouse 1.4.0

* Mon Dec 22 2008 Peter Hutterer <peter.hutterer@redhat.com> 1.3.0-1.20081222
- Today's git snapshot.

* Thu Mar 20 2008 Adam Jackson <ajax@redhat.com> 1.3.0-1
- mouse 1.3.0

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.2.3-4
- Autorebuild for GCC 4.3

* Tue Nov 13 2007 Adam Jackson <ajax@redhat.com> 1.2.3-3
- Require xserver 1.4.99.1

* Fri Nov 09 2007 Adam Jackson <ajax@redhat.com> 1.2.3-2
- mouse-1.2.3-sleep-less.patch: Don't usleep(300000) at exit.

* Wed Oct 17 2007 Adam Jackson <ajax@redhat.com> 1.2.3-1
- xf86-input-mouse 1.2.3

* Mon Sep 24 2007 Adam Jackson <ajax@redhat.com> 1.2.2-1
- xf86-input-mouse 1.2.2

* Wed Aug 22 2007 Adam Jackson <ajax@redhat.com> - 1.2.1-4
- Rebuild for PPC toolchain bug

* Mon Jun 18 2007 Adam Jackson <ajax@redhat.com> 1.2.1-3
- Update Requires and BuildRequires.  Disown the module directories.

* Fri Feb 16 2007 Adam Jackson <ajax@redhat.com> 1.2.1-2
- ExclusiveArch -> ExcludeArch

* Fri Dec 1 2006 Adam Jackson <ajax@redhat.com> 1.2.1-1
- Update to 1.2.1

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - sh: line 0: fg: no job control
- rebuild

* Thu Jun 15 2006 Adam Jackson <ajackson@redhat.com> 1.1.1-1
- Update to 1.1.1

* Tue Jun 13 2006 Adam Jackson <ajackson@redhat.com> 1.1.0-3
- Build on ppc64

* Wed May 17 2006 Kristian Høgsberg <krh@redhat.com> - 1.1.0-2
- Add missing build requires (#192047).

* Sun Apr  9 2006 Adam Jackson <ajackson@redhat.com> 1.1.0-1
- Update to 1.1.0 from 7.1RC1.

* Wed Mar 01 2006 Mike A. Harris <mharris@redhat.com> 1.0.4-1
- Updated to new upstream driver version mouse-1.0.4.

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> 1.0.3.1-1.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> 1.0.3.1-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Wed Jan 18 2006 Mike A. Harris <mharris@redhat.com> 1.0.3.1-1
- Updated xorg-x11-drv-mouse to version 1.0.3.1 from X11R7.0
- Rename temporary name of mouse manpage, to close (#178744)

* Tue Dec 20 2005 Mike A. Harris <mharris@redhat.com> 1.0.3-1
- Updated xorg-x11-drv-mouse to version 1.0.3 from X11R7 RC4
- Removed 'x' suffix from manpage dirs to match RC4 upstream.
- Worked around mouse manpage issue.

* Mon Nov 21 2005 Mike A. Harris <mharris@redhat.com> 1.0.1-2
- Added "alpha sparc sparc64" to ExclusiveArch for AlphaCore, CentOS,
  AuroraLinux distributions, to minimize patching for them.
- Added ">= 0.99.3" dependency on Xorg server and sdk, based on CVS log
  message from Daniel Stone on Nov 21, 2005.

* Wed Nov 16 2005 Mike A. Harris <mharris@redhat.com> 1.0.1-1
- Updated xorg-x11-drv-mouse to version 1.0.1 from X11R7 RC2

* Fri Nov 04 2005 Mike A. Harris <mharris@redhat.com> 1.0.0.1-1
- Updated xorg-x11-drv-mouse to version 1.0.0.1 from X11R7 RC1
- Fix *.la file removal.

* Fri Sep 02 2005 Mike A. Harris <mharris@redhat.com> 1.0.0-0
- Initial spec file for mouse input driver generated automatically
  by my xorg-driverspecgen script.
