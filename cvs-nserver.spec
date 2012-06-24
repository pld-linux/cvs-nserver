# TODO:
# - trigger for upgrade from old cvs - after that package stays without any
#   users and nserver-common is not installed...
Summary:	Concurrent Versions System - nserver
Summary(de):	Concurrent-Versioning-System - nserver
Summary(fr):	Un syst�me pour maintenir � jour des fichiers - nserver
Summary(pl):	Concurrent Versions System - nserver
Summary(tr):	S�r�m denetim sistemi - nserver
Name:		cvs-nserver
Version:	1.11.1.52
Release:	16
License:	GPL
Group:		Development/Version Control
Source0:	http://dl.sourceforge.net/cvs-nserver/%{name}-%{version}.tar.gz
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
Patch11:	%{name}-posix.patch
Patch12:	%{name}-CAN-2002-0844.patch
Patch13:	%{name}-CAN-2003-0015.patch
Patch14:	%{name}-CAN-2003-0977-and-CAN-2004-0180.patch
Patch15:	%{name}-CAN-2004-0396.patch
Patch16:	%{name}-CAN-2004-0414.patch
Patch17:	%{name}-CAN-2004-0416-0417-0418.patch
Patch18:	%{name}-dblshutdown.patch
URL:		http://cvs-nserver.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	texinfo
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_cvsroot	/var/lib/cvs

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
�r�d�owym opracowywanym przez nawet bardzo du�e zespo�y programist�w
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
Provides:	cvs = %{version}
Obsoletes:	cvs
Obsoletes:	cvs-npclient

%description client
CVS client.

%description client -l pl
Klient CVS.

%package common
Summary:	Concurrent Versions System - common files
Summary(pl):	Concurrent Versions System - wsp�lne pliki
Group:		Development/Version Control
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires(pre):	cvs-nserver-client
Requires(pre):	fileutils
Requires:	%{name}-client = %{version}-%{release}
Provides:	group(cvs)
Provides:	group(cvsadmin)
Provides:	user(cvs)
Provides:	user(cvsadmin)
Obsoletes:	cvs-nserver

%description common
CVS - common server files.

%description common -l pl
Wsp�lne pliki serwer�w CVS.

%package pserver
Summary:	Concurrent Versions System - pserver
Summary(pl):	Concurrent Versions System - pserver
Group:		Development/Version Control
Requires:	%{name}-common = %{version}-%{release}
Requires:	rc-inetd
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
Requires:	%{name}-common = %{version}-%{release}
Requires:	rc-inetd
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
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1

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
install -d $RPM_BUILD_ROOT{/etc/sysconfig/rc-inetd,%{_cvsroot},/var/lock/cvs}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/cvs-nserver
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/cvs-pserver

cat << EOF >$RPM_BUILD_ROOT%{_bindir}/cvs-pserver-script
#!/bin/sh
REPOSITORY="%{_cvsroot}"
if [ -f /etc/sysconfig/cvs ]; then
	. /etc/sysconfig/cvs
fi

CVSPASSWD=%{_bindir}/cvspasswd \
exec %{_bindir}/cvs-pserver \$REPOSITORY -- \
%{_bindir}/cvschkpw %{_bindir}/cvs pserver
EOF

cat << EOF >$RPM_BUILD_ROOT%{_bindir}/cvs-nserver-script
#!/bin/sh
REPOSITORY="%{_cvsroot}"
if [ -f /etc/sysconfig/cvs ]; then
	. /etc/sysconfig/cvs
fi

CVSPASSWD=%{_bindir}/cvspasswd \
exec %{_bindir}/cvs-nserver \$REPOSITORY -- \
%{_bindir}/cvschkpw %{_bindir}/cvs nserver
EOF

cat << EOF >$RPM_BUILD_ROOT/etc/sysconfig/cvs
# In this file you can specify additional repositories (separated with space)
# or just set different location.
# Default is "%{_cvsroot}".
#REPOSITORY="%{_cvsroot}"
# According to FHS 2.3 you can use some subdirectory in /srv, e.g.:
#REPOSITORY="/srv/cvs"
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
%groupadd -P %{name}-common -g 52 -r cvs
%groupadd -P %{name}-common -g 53 -r cvsadmin
%useradd -P %{name}-common -u 52 -r -d %{_cvsroot} -s /bin/false -c "CVS user" -g cvs cvs
%useradd -P %{name}-common -u 53 -r -d %{_cvsroot} -s /bin/false -c "CVS user" -g cvsadmin -G cvs cvsadmin

if [ "$1" = 1 ]; then
	echo "Initializing repository..."
	%{_bindir}/cvs -d :local:%{_cvsroot} init
	chown -R cvsadmin:cvsadmin %{_cvsroot}/CVSROOT
fi

%postun common
if [ "$1" = "0" ]; then
	%userremove cvs
	%userremove cvsadmin
	%groupremove cvs
	%groupremove cvsadmin
fi

%post pserver
%service -q rc-inetd reload

%postun pserver
%service -q rc-inetd reload

%post nserver
%service -q rc-inetd reload

%postun nserver
%service -q rc-inetd reload

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
%attr(640,root,cvs) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/cvs
%attr(4754,cvsadmin,cvs) %{_bindir}/cvspasswd
%attr(755,root,root) %{_bindir}/cvschkpw
%attr(755,root,root) %{_bindir}/rcs2log
%dir %{_datadir}/cvs-nserver
%dir %{_datadir}/cvs-nserver/contrib
%{_datadir}/cvs-nserver/contrib/*
%attr(770,cvsadmin,cvs) %dir %{_cvsroot}
%{_mandir}/man8/cvs-server.8*
%attr(770,cvsadmin,cvs) %dir /var/lock/cvs

%files pserver
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/rc-inetd/cvs-pserver
%attr(755,root,root) %{_bindir}/cvs-pserver*
%{_mandir}/man8/cvs-pserver.8*

%files nserver
%defattr(644,root,root,755)
%doc NEWS.nserver FAQ.nserver
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/rc-inetd/cvs-nserver
%attr(755,root,root) %{_bindir}/cvs-nserver*
%{_mandir}/man8/cvs-nserver.8*
