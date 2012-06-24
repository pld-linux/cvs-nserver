Summary:	Concurrent Versions System - nserver
Summary(de):	Concurrent-Versioning-System - nserver
Summary(fr):	Un syst�me pour maintenir � jour des fichiers - nserver
Summary(pl):	Concurrent Versions System - nserver
Summary(tr):	S�r�m denetim sistemi - nserver
Name:		cvs-nserver
Version:	1.11.1.52
Release:	5
License:	GPL
Group:		Development/Version Control
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	357fb5f37cc556977dad79175e9c2d97
Source1:	%{name}.inetd
Source2:	cvs-pserver.inetd
Patch0:		%{name}-cvspasswd.patch
Patch1:		%{name}-info.patch
Patch2:		%{name}-am_ac.patch
Patch3:		%{name}-cvspass.patch
Patch4:		%{name}-home_etc.patch
Patch5:		%{name}-ssl-link.patch
Patch6:		%{name}-fix_doc_CVSUSER.patch
Patch7:		%{name}-segv.patch
Patch8:		%{name}-initgroups-rootonly.patch
Patch9:		%{name}-zlibfix.patch
Patch10:	%{name}-home_etc2.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	openssl-devel >= 0.9.7c
BuildRequires:	texinfo
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_cvsroot	/home/services/cvsroot

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
CVS ist ein Frontend f�r das RCS(1)-Revisionskontrollsystem, das den
Begriff der Revisionskontrolle von einer Sammlung von Dateien in einem
einzelnen Verzeichnis auf eine ganze Hierarchie ausweitet, bestehend
aus revisionskontrollierten Dateien. Diese Verzeichnisse und Dateien
lassen sich zu einer Software-Release kombinieren. CVS bietet die
Funktionen, die zur Verwaltung von Software-Releases und zur
�berwachung der gleichzeitigen Bearbeitung von Quelldateien durch
mehrere Software- Entwickler notwendig sind.

%description -l fr
"CVS" signifie "Concurrent Version System". C'est un syst�me de
comparaison de versions de fichiers, qui peut garder une trace des
changements apport�s � des fichiers (le plus souvent, les fichiers des
sources d'un programme). CVS conserve seulement les diff�rences, et
non l'int�gralit� d'un fichier r�cent et d'un fichier plus ancien. A
chaque modification d'un fichier, CVS garde (entre autres) le nom de
la personne ayant fait la modification, la raison justifiant cette
modification, et la date � laquelle celle-ci a eu lieu. CVS est tr�s
utile pour g�rer la mise en commun des modifications apport�es par
plusieurs personnes travaillant en parall�le sur les m�mes fichiers.
Au lieu de garder plusieurs versions des fichiers dans un seul
r�pertoire, CVS cr�e une s�rie de r�pertoires, chacun contenant une
nouvelle version des fichiers. Ces r�pertoires et ces fichiers peuvent
ensuite �tre regroup�s pour former la version la plus � jour du
logiciel. Installez ce package si vous avez besoin d'utiliser un
syst�me de contr�le de version.

%description -l pl
CVS jest nak�adk� na rcs (Revision Control System, czyli w wolnym
t�umaczeniu system kontroli wersji zasob�w), kt�ry rozszerza
mo�liwo�ci rcs'a z narz�dzia do kontroli zbioru plik�w w pojedynczym
katalogu o mo�liwo�� kontroli zbioru hierarchicznie u�o�onych
katalog�w z plikami. Z pomoc� CVS w �atwy spos�b mo�na zarz�dza� kodem
�r�d�owym opracowywanym przez nawet bardzo du�e zesp�y programist�w
umo�liwiaj�c �ledzenie i kontrol� wszystkich zmian w trakcie pracy nad
projektami i wypuszczaniem pe�nych wersji oprogramowania (release).

%description -l tr
CVS (Concurrent Versioning System), tek bir dizindeki dosya
toplulu�unun s�r�m denetimini, denetimi yap�lm�� dizinlerin hiyerar�ik
toplulu�una geni�leten rcs(1) s�r�m denetim sisteminin �n y�z�d�r. Bu
dizin ve dosyalar, bir yaz�l�m yay�n� olu�turma amac�yla biraraya
getirilebilir. CVS, bu yaz�l�m yay�nlar�n�n y�netilmesini ve kaynak
dosyalar� bak�m�n�n birden �ok yaz�l�m geli�tiricisi taraf�ndan
e�zamanl� olarak yap�lmas�n� kontrol etmek i�in gereken i�levleri
sa�lar.

%package client
Summary:	Concurrent Versions System - client
Summary(pl):	Concurrent Versions System - klient
Group:		Development/Version Control
Obsoletes:	cvs-npclient
Obsoletes:	cvs
Provides:	cvs = %{version}

%description client
CVS client.

%description client -l pl
Klient CVS.

%package common
Summary:	Concurrent Versions System - common files
Summary(pl):	Concurrent Versions System - wsp�lne pliki
Group:		Development/Version Control
Requires(pre):	/usr/bin/getgid
Requires(pre):	/bin/id
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires(postun):	/usr/sbin/userdel
Requires(postun):	/usr/sbin/groupdel
Requires(pre):	cvs-nserver-client
Requires(pre):	fileutils
Requires:	cvs-nserver-client
Obsoletes:	cvs-nserver

%description common
CVS - common server files.

%description common -l pl
Wsp�lne pliki serwer�w CVS.

%package pserver
Summary:	Concurrent Versions System - pserver
Summary(pl):	Concurrent Versions System - pserver
Group:		Development/Version Control
PreReq:		rc-inetd
Requires:	cvs-nserver-common
Obsoletes:	cvs-npserver
Obsoletes:	cvs-pserver

%description pserver
CVS server - pserver files.

%description pserver -l pl
Serwer CVS - pliki pservera.

%package nserver
Summary:	Concurrent Versions System - nserver
Summary(pl):	Concurrent Versions System - nserver
Group:		Development/Version Control
PreReq:		rc-inetd
Requires:	cvs-nserver-common
Obsoletes:	cvs-nserver

%description nserver
CVS server - nserver files.

%description nserver -l pl
Serwer CVS - pliki nservera.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-encryption \
	--enable-client \
	--enable-server \
	--enable-setuid \
	--with-openssl \
	--without-gssapi
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/sysconfig/rc-inetd,%{_cvsroot}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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

%clean
rm -rf $RPM_BUILD_ROOT

%post client
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun client
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%pre common
if [ -n "`getgid cvs`" ]; then
	if [ "`getgid cvs`" != "52" ]; then
		echo "Error: group cvs doesn't have gid=52. Correct this before installing cvs-nserver." 1>&2
		exit 1
	fi
else
	echo "Adding group cvs GID=52."
	/usr/sbin/groupadd -g 52 -r -f cvs
fi
if [ -n "`getgid cvsadmin`" ]; then
	if [ "`getgid cvsadmin`" != "53" ]; then
		echo "Error: group cvsadmin doesn't have gid=53. Correct this before installing cvs-nserver." 1>&2
		exit 1
	fi
else
	echo "Adding group cvsadmin GID=53."
	/usr/sbin/groupadd -g 53 -r -f cvsadmin
fi
if [ -n "`id -u cvs 2>/dev/null`" ]; then
	if [ "`id -u cvs`" != "52" ]; then
		echo "Error: user cvs doesn't have uid=52. Correct this before installing cvs-nserver." 1>&2
		exit 1
	fi
else
	echo "Adding user cvs UID=52."
	/usr/sbin/useradd -u 52 -r -d %{_cvsroot} -s /bin/false -c "CVS user" -g cvs cvs 1>&2
fi
if [ -n "`id -u cvsadmin 2>/dev/null`" ]; then
	if [ "`id -u cvsadmin`" != "53" ]; then
		echo "Error: user cvsadmin doesn't have uid=53. Correct this before installing cvs-nserver." 1>&2
		exit 1
	fi
else
	echo "Adding user cvsadmin UID=53."
	/usr/sbin/useradd -u 53 -r -d %{_cvsroot} -s /bin/false -c "CVS user" -g cvsadmin -G cvs cvsadmin 1>&2
fi
if [ "$1" = 1 ]; then
	echo "Initializing repository..."
	%{_bindir}/cvs -d :local:%{_cvsroot} init
	chown -R cvsadmin:cvsadmin %{_cvsroot}/CVSROOT
fi

%postun common
if [ "$1" = "0" ]; then
	echo "Removing user cvs."
	/usr/sbin/userdel cvs
	echo "Removing user cvsadmin."
	/usr/sbin/userdel cvsadmin
	echo "Removing group cvs."
	/usr/sbin/groupdel cvs
	echo "Removing group cvsadmin."
	/usr/sbin/groupdel cvsadmin
fi

%post pserver
if [ -f /var/lock/subsys/rc-inetd ]; then
	/etc/rc.d/init.d/rc-inetd reload
fi

%postun pserver
if [ -f /var/lock/subsys/rc-inetd ]; then
	/etc/rc.d/init.d/rc-inetd reload
fi

%post nserver
if [ -f /var/lock/subsys/rc-inetd ]; then
	/etc/rc.d/init.d/rc-inetd reload
fi

%postun nserver
if [ -f /var/lock/subsys/rc-inetd ]; then
	/etc/rc.d/init.d/rc-inetd reload
fi

%files client
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog FAQ FAQ.nserver NEWS NEWS.nserver PROJECTS
%doc README README.checkpassword TODO
%attr(755,root,root) %{_bindir}/cvs
%attr(755,root,root) %{_bindir}/cvsbug
%{_infodir}/cvs*
%{_mandir}/man[15]/cvs.*
%{_mandir}/man8/cvsbug.8*

%files common
%defattr(644,root,root,755)
%attr(4754,cvsadmin,cvs) %{_bindir}/cvspasswd
%attr(755,root,root) %{_bindir}/cvschkpw
%attr(755,root,root) %{_bindir}/rcs2log
%dir %{_datadir}/cvs-nserver
%dir %{_datadir}/cvs-nserver/contrib
%{_datadir}/cvs-nserver/contrib/*
%attr(770,cvsadmin,cvs) %dir %{_cvsroot}
%{_mandir}/man8/cvs-server.8*

%files pserver
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cvs-pserver*
%config(noreplace) %verify(not size mtime md5) /etc/sysconfig/rc-inetd/cvs-pserver
%{_mandir}/man8/cvs-pserver.8*

%files nserver
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cvs-nserver*
%doc NEWS.nserver FAQ.nserver
%config(noreplace) %verify(not size mtime md5) /etc/sysconfig/rc-inetd/cvs-nserver
%{_mandir}/man8/cvs-nserver.8*
