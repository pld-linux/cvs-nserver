Summary: Concurrent Versions System
Name: cvs-nserver
Version: 1.10.8.1
Release: 1
Copyright: GPL
Group: Development/Version Control
Source: http://alexm.here.ru/cvs-nserver/download/cvs-nserver-1.10.8.1.tar.gz
Packager: Alexey Mahotkin <alexm@hsys.msk.ru>
Prefix: /usr
BuildRoot: /var/tmp/cvs-nserver

%description
CVS is a version control system, which allows you to keep old versions
of files (usually source code), keep a log of who, when, and why
changes occurred, etc., like RCS or SCCS.  Unlike the simpler systems,
CVS does not just operate on one file at a time or one directory at a
time, but operates on hierarchical collections of directories
consisting of version controlled files.  CVS helps to manage releases
and to control the concurrent editing of source files among multiple
authors.  CVS allows triggers to enable/log/control various
operations and works well over a wide area network.

%prep
%setup

%build
./configure --prefix=$RPM_BUILD_ROOT/usr --enable-pam
make CFLAGS="$RPM_OPT_FLAGS" LDFLAGS=-s 

%install
make installdirs
make PAMDIR=$RPM_BUILD_ROOT/etc/pam.d install
rm -f $RPM_BUILD_ROOT/usr/info/cvs*
make install-info
gzip -9nf $RPM_BUILD_ROOT/usr/info/cvs*

%files
%defattr(-, root, root)
%doc BUGS COPYING COPYING.LIB FAQ HACKING
%doc INSTALL MINOR-BUGS NEWS PROJECTS README TESTS TODO
/usr/bin/cvs
/usr/bin/cvschkpw
/usr/bin/cvs-pserver
/usr/bin/cvs-nserver
/usr/bin/checkpassword
/usr/bin/checkpassword-pam
/usr/bin/cvsbug
/usr/bin/rcs2log
/etc/pam.d/cvspserver
/usr/man/man1/cvs.1
/usr/man/man5/cvs.5
/usr/man/man8/cvsbug.8
/usr/man/man8/cvs-nserver.8
/usr/man/man8/cvs-pserver.8
/usr/man/man8/cvs-server.8
/usr/info/cvs*
/usr/lib/cvs
