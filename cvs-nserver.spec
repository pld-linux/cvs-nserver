Summary:	Concurrent Versions System - nserver
Summary(de):	Concurrent-Versioning-System - nserver
Summary(fr):	Un système pour maintenir à jour des fichiers - nserver
Summary(pl):	Concurrent Versions System - nserver
Summary(tr):	Sürüm denetim sistemi - nserver
Name:		cvs-nserver
Version:	1.11.1.4
Release:	1
License:	GPL
Group:		Development/Version Control
Source0:	http://unc.dl.sourceforge.net/sourceforge/cvs-nserver/%{name}-%{version}.tar.gz
Source1:	%{name}.inetd
Source2:	cvs-pserver.inetd
Patch0:		%{name}-cvspasswd.patch
Patch1:		%{name}-info.patch
# outdated, but maybe will be needed for checkpasswd (outside programs):
Patch3:		%{name}-PAM_fix.patch
Patch4:		%{name}-am_ac.patch
Patch5:		%{name}-zlib.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_cvsroot	/home/cvsroot

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

%description -l de
CVS ist ein Frontend für das RCS(1)-Revisionskontrollsystem, das den
Begriff der Revisionskontrolle von einer Sammlung von Dateien in einem
einzelnen Verzeichnis auf eine ganze Hierarchie ausweitet, bestehend
aus revisionskontrollierten Dateien. Diese Verzeichnisse und Dateien
lassen sich zu einer Software-Release kombinieren. CVS bietet die
Funktionen, die zur Verwaltung von Software-Releases und zur
Überwachung der gleichzeitigen Bearbeitung von Quelldateien durch
mehrere Software- Entwickler notwendig sind.

%description -l fr
"CVS" signifie "Concurrent Version System". C'est un système de
comparaison de versions de fichiers, qui peut garder une trace des
changements apportés à des fichiers (le plus souvent, les fichiers des
sources d'un programme). CVS conserve seulement les différences, et
non l'intégralité d'un fichier récent et d'un fichier plus ancien. A
chaque modification d'un fichier, CVS garde (entre autres) le nom de
la personne ayant fait la modification, la raison justifiant cette
modification, et la date à laquelle celle-ci a eu lieu. CVS est très
utile pour gérer la mise en commun des modifications apportées par
plusieurs personnes travaillant en parallèle sur les mêmes fichiers.
Au lieu de garder plusieurs versions des fichiers dans un seul
répertoire, CVS crée une série de répertoires, chacun contenant une
nouvelle version des fichiers. Ces répertoires et ces fichiers peuvent
ensuite être regroupés pour former la version la plus à jour du
logiciel. Installez ce package si vous avez besoin d'utiliser un
système de contrôle de version.

%description -l pl
CVS jest nak³adk± na rcs (Revision Control System, czyli w wolnym
t³umaczeniu system kontroli wersji zasobów), który rozszerza
mo¿liwo¶ci rcs'a z narzêdzia do kontroli zbioru plików w pojedynczym
katalogu o mo¿liwo¶æ kontroli zbioru hierarchicznie u³o¿onych
katalogów z plikami. Z pomoc± CVS w ³atwy sposób mo¿na zarz±dzaæ kodem
¼ród³owym opracowywanym przez nawet bardzo du¿e zespó³y programistów
umo¿liwiaj±c ¶ledzenie i kontrolê wszystkich zmian w trakcie pracy nad
projektami i wypuszczaniem pe³nych wersji oprogramowania (release).

%description -l tr
CVS (Concurrent Versioning System), tek bir dizindeki dosya
topluluðunun sürüm denetimini, denetimi yapýlmýþ dizinlerin hiyerarþik
topluluðuna geniþleten rcs(1) sürüm denetim sisteminin ön yüzüdür. Bu
dizin ve dosyalar, bir yazýlým yayýný oluþturma amacýyla biraraya
getirilebilir. CVS, bu yazýlým yayýnlarýnýn yönetilmesini ve kaynak
dosyalarý bakýmýnýn birden çok yazýlým geliþtiricisi tarafýndan
eþzamanlý olarak yapýlmasýný kontrol etmek için gereken iþlevleri
saðlar.

%package -n cvs-nclient
Summary:	Concurrent Versions System - common
Summary(pl):	Concurrent Versions System - wspólne
Group:		Development/Version Control

%description -n cvs-nclient
Client and some common files.

%description -n cvs-nclient -l pl
Klient CVS i trochê wspólnych plików.

%package -n cvs-npserver
Summary:	Concurrent Versions System - pserver
Summary(pl):	Concurrent Versions System - pserver
Group:		Development/Version Control
Requires:	cvs-nserver-common
Obsoletes:	cvs
Obsoletes:	cvs-nserver

%description -n cvs-npserver
Server - pserver.

%description -n cvs-npserver -l pl
Serwer - pserver.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch4 -p1
%patch5 -p1

%build
aclocal
autoconf
automake -a -c
%configure \
	--enable-encryption \
	--enable-client \
	--enable-server \
	--enable-setuid \
	--without-gssapi
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc/sysconfig/rc-inetd,%{_cvsroot}}

%{__make} DESTDIR=$RPM_BUILD_ROOT install

install %{SOURCE1} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/cvs-nserver
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/cvs-pserver

cat << EOF >$RPM_BUILD_ROOT%{_bindir}/cvs-pserver-script
#!/bin/sh
CVSPASSWD=%{_bindir}/cvspasswd \
exec %{_bindir}/cvs-pserver %{_cvsroot} -- \
%{_bindir}/cvschkpw %{_bindir}/cvs pserver
EOF

cat << EOF >$RPM_BUILD_ROOT%{_bindir}/cvs-nserver-script
#!/bin/sh
CVSPASSWD=%{_bindir}/cvspasswd \
exec %{_bindir}/cvs-nserver %{_cvsroot} -- \
%{_bindir}/cvschkpw %{_bindir}/cvs nserver
EOF

mv -f	$RPM_BUILD_ROOT%{_datadir}/cvs-nserver/contrib/rcs2log \
	$RPM_BUILD_ROOT%{_bindir}

gzip -9nf AUTHORS BUGS NEWS NEWS.nserver PROJECTS TODO FAQ FAQ.nserver

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -n "`getgid cvs`" ]; then
	if [ "`getgid cvs`" != "52" ]; then
		echo "Warning: group cvs haven't gid=52. Correct this before installing cvs-nserver" 1>&2
		exit 1
	fi
else
	echo "Making group cvs GID=52"
	/usr/sbin/groupadd -g 52 -r -f cvs
fi
if [ -n "`getgid cvsadmin`" ]; then
	if [ "`getgid cvsadmin`" != "53" ]; then
		echo "Warning: group cvsadmin haven't gid=53. Correct this before installing cvs-nserver" 1>&2
		exit 1
	fi
else
	echo "Making group cvsadmin GID=53"
	/usr/sbin/groupadd -g 53 -r -f cvsadmin
fi
if [ -n "`id -u cvs 2>/dev/null`" ]; then
	if [ "`id -u cvs`" != "52" ]; then
		echo "Warning: user cvs haven't uid=52. Correct this before installing cvs-nserver" 1>&2
		exit 1
	fi
else
	echo "Making user cvs UID=52"
	/usr/sbin/useradd -u 52 -r -d %{_cvsroot} -s /bin/false -c "CVS user" -g cvs cvs 1>&2
fi
if [ -n "`id -u cvsadmin 2>/dev/null`" ]; then
	if [ "`id -u cvsadmin`" != "53" ]; then
		echo "Warning: user cvsadmin haven't uid=53. Correct this before installing cvs-nserver" 1>&2
		exit 1
	fi
else
	echo "Making user cvsadmin UID=53"
	/usr/sbin/useradd -u 53 -r -d %{_cvsroot} -s /bin/false -c "CVS user" -g cvsadmin -G cvs cvsadmin 1>&2
fi

if [ "$1" = 1 ]; then
	echo "Initialise repository"
	%{_bindir}/cvs -d :local:%{_cvsroot} init
	chown -R cvsadmin.cvsadmin %{_cvsroot}/CVSROOT
fi
if [ -f /var/lock/subsys/rc-inetd ]; then
        /etc/rc.d/init.d/rc-inetd reload
fi

%postun
if [ "$1" = "0" ]; then
	echo "Removing group cvs GID=52"
	/usr/sbin/userdel cvs
	echo "Removing group cvsadmin GID=53"
	/usr/sbin/userdel cvsadmin
	echo "Removing user cvs UID=52"
	/usr/sbin/groupdel cvs
	echo "Removing user cvsadmin UID=53"
	/usr/sbin/groupdel cvsadmin
fi
if [ -f /var/lock/subsys/rc-inetd ]; then
        /etc/rc.d/init.d/rc-inetd reload
fi

%post -n cvs-nclient
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%post -n cvs-npserver
if [ "$1" = 1 ]; then
	echo "Initialise repository"
	%{_bindir}/cvs -d :local:%{_cvsroot} init
	chown -R cvsadmin.cvsadmin %{_cvsroot}/CVSROOT
fi
if [ -f /var/lock/subsys/rc-inetd ]; then
        /etc/rc.d/init.d/rc-inetd reload
fi

%postun -n cvs-npserver
if [ -f /var/lock/subsys/rc-inetd ]; then
        /etc/rc.d/init.d/rc-inetd reload
fi

%postun -n cvs-nclient
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cvs-nserver*
%doc NEWS.nserver.gz FAQ.nserver.gz
/etc/sysconfig/rc-inetd/cvs-nserver
%attr(4754,cvsadmin,cvs) %{_bindir}/cvspasswd
%attr(755,root,root) %{_bindir}/cvschkpw
%attr(755,root,root) %{_bindir}/rcs2log
%dir %{_datadir}/cvs-nserver/contrib/*
%attr(770,cvsadmin,cvs) %dir %{_cvsroot}
%{_mandir}/man8/cvs-server.8*
%{_mandir}/man8/cvs-nserver.8*

%files -n cvs-nclient
%defattr(644,root,root,755)
%doc {AUTHORS,BUGS,NEWS,PROJECTS,TODO,FAQ}.gz
%attr(755,root,root) %{_bindir}/cvs
%attr(755,root,root) %{_bindir}/cvsbug
%{_infodir}/cvs*
%{_mandir}/man[15]/cvs.*
%{_mandir}/man8/cvsbug.8*

%files -n cvs-npserver
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cvs-pserver*
/etc/sysconfig/rc-inetd/cvs-pserver
%{_mandir}/man8/cvs-pserver.8*
