Summary:	Concurrent Versions System
Name:		cvs-nserver
Version:	1.10.8.3
Release:	1
License:	GPL
Group:		Development/Version Control
Group(pl):	Programowanie/Zarz±dzanie wersjami
Source0:	http://alexm.here.ru/cvs-nserver/download/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CVS is a version control system, which allows you to keep old versions
of files (usually source code), keep a log of who, when, and why
changes occurred, etc., like RCS or SCCS. Unlike the simpler systems,
CVS does not just operate on one file at a time or one directory at a
time, but operates on hierarchical collections of directories
consisting of version controlled files. CVS helps to manage releases
and to control the concurrent editing of source files among multiple
authors. CVS allows triggers to enable/log/control various operations
and works well over a wide area network.

%prep
%setup -q

%build
LDFLAGS="-s"; export LDFLAGS
%configure \
	--enable-pam
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} installdirs
%{__make} PAMDIR=$RPM_BUILD_ROOT/etc/pam.d install
%{__make} install-setuid
rm -f $RPM_BUILD_ROOT%{_prefix}/info/cvs*
%{__make} install-info

gzip -9nf $RPM_BUILD_ROOT{%{_infodir}/*,%{_mandir}/man?/*} \
	BUGS FAQ HACKING MINOR-BUGS NEWS PROJECTS README TESTS TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/cvs
%attr(755,root,root) %{_bindir}/cvschkpw
%attr(755,root,root) %{_bindir}/cvspasswd
%attr(755,root,root) %{_bindir}/cvs-pserver
%attr(755,root,root) %{_bindir}/cvs-nserver
%attr(755,root,root) %{_bindir}/checkpassword
%attr(755,root,root) %{_bindir}/checkpassword-pam
%attr(755,root,root) %{_bindir}/cvsbug
%attr(755,root,root) %{_bindir}/rcs2log
/etc/pam.d/cvspserver
%{_mandir}/man1/cvs.1
%{_mandir}/man5/cvs.5
%{_mandir}/man8/cvsbug.8
%{_mandir}/man8/cvs-nserver.8
%{_mandir}/man8/cvs-pserver.8
%{_mandir}/man8/cvs-server.8
%{_infodir}/cvs*
%{_libdir}/cvs
