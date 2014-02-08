%define upstream_name    Filesys-Df
%define upstream_version 0.92

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    13

Summary:    Disk free based on Filesys::Statvfs
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Filesys/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module provides a way to obtain filesystem disk space information.
This is a Unix only distribution. If you want to gather this information
for Unix and Windows, use 'Filesys::DfPortable'. The only major benefit of
using 'Filesys::Df' over 'Filesys::DfPortable', is that 'Filesys::Df'
supports the use of open filehandles as arguments.

The module should work with all flavors of Unix that implement the
'statvfs()' and 'fstatvfs()' calls, or the 'statfs()' and 'fstatfs()'
calls. This would include Linux, *BSD, HP-UX, AIX, Solaris, Mac OS X, Irix,
Cygwin, etc ...

'df()' requires a argument that represents the filesystem you want to
query. The argument can be either a scalar directory/file name or a open
filehandle. There is also an optional block size argument so you can tailor
the size of the values returned. The default block size is 1024. This will
cause the function to return the values in 1k blocks. If you want bytes,
set the block size to 1.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*



%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.920.0-10mdv2012.0
+ Revision: 765266
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.920.0-9
+ Revision: 763766
- rebuilt for perl-5.14.x
- cleanup temporary deps, this was added in perl-devel instead

* Fri Jan 20 2012 Oden Eriksson <oeriksson@mandriva.com> 0.920.0-8
+ Revision: 763246
- force it
- rebuild

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.920.0-7
+ Revision: 667149
- mass rebuild

* Sun Apr 03 2011 Funda Wang <fwang@mandriva.org> 0.920.0-6
+ Revision: 650048
- rebuild

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 0.920.0-5mdv2011.0
+ Revision: 564437
- rebuild for perl 5.12.1

* Tue Jul 20 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.920.0-4mdv2011.0
+ Revision: 555285
- rebuild

  + Jérôme Quelin <jquelin@mandriva.org>
    - rebuild for 5.12

* Tue Oct 20 2009 Thierry Vignaud <tv@mandriva.org> 0.920.0-2mdv2010.1
+ Revision: 458326
- do not package debug files

* Sun Jul 12 2009 Jérôme Quelin <jquelin@mandriva.org> 0.920.0-1mdv2010.0
+ Revision: 395199
- removing file already packaged
- package is arch-dependant
- import perl-Filesys-Df


* Sun Jul 12 2009 cpan2dist 0.92-1mdv
- initial mdv release, generated with cpan2dist
