%define modname	Filesys-Df
%define modver	0.92

Summary:	Disk free based on Filesys::Statvfs
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	26
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Filesys/%{modname}-%{modver}.tar.gz
BuildRequires:	perl-devel

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
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorarch}/*
%{_mandir}/man3/*
