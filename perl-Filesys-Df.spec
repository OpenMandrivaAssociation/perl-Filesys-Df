%define upstream_name    Filesys-Df
%define upstream_version 0.92

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 7

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

